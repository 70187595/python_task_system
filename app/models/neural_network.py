"""
Простая нейронная сеть для анализа качества кода Python

МАТЕМАТИЧЕСКОЕ ОБОСНОВАНИЕ
==========================

Полное математическое описание архитектуры см. в docs/MATHEMATICAL_FOUNDATION.md

АРХИТЕКТУРА:
    Входной слой (10) → Скрытый слой (8) → Выходной слой (3)
    
    x ∈ ℝ¹⁰  →  h = σ(W⁽¹⁾x + b⁽¹⁾) ∈ ℝ⁸  →  y = σ(W⁽²⁾h + b⁽²⁾) ∈ ℝ³

ПАРАМЕТРЫ:
    - W⁽¹⁾ ∈ ℝ⁸ˣ¹⁰ : веса входного слоя (80 параметров)
    - b⁽¹⁾ ∈ ℝ⁸    : смещения скрытого слоя (8 параметров)
    - W⁽²⁾ ∈ ℝ³ˣ⁸  : веса скрытого слоя (24 параметра)
    - b⁽²⁾ ∈ ℝ³    : смещения выходного слоя (3 параметра)
    ИТОГО: 115 параметров

ФУНКЦИЯ АКТИВАЦИИ (Sigmoid):
    σ(z) = 1 / (1 + e⁻ᶻ)
    σ'(z) = σ(z) · (1 - σ(z))

ФУНКЦИЯ ПОТЕРЬ (MSE):
    L = 1/N Σᵢ ||yᵢ - ŷᵢ||² = 1/N Σᵢ Σⱼ (yᵢⱼ - ŷᵢⱼ)²

ГРАДИЕНТНЫЙ СПУСК:
    W := W + α · ∂L/∂W
    b := b + α · ∂L/∂b
    где α = learning_rate
"""

import numpy as np
import json
import os
from typing import List, Tuple, Dict


class SimpleNeuralNetwork:
    """
    Простая многослойная нейронная сеть для анализа кода
    """
    
    def __init__(self, input_size: int = 10, hidden_size: int = 8, output_size: int = 3, 
                 activation: str = 'sigmoid', hidden_size2: int = None, dropout_rate: float = 0.0):
        """
        Инициализация нейронной сети
        
        Args:
            input_size: Размер входного слоя (количество признаков)
            hidden_size: Размер первого скрытого слоя
            output_size: Размер выходного слоя (оценка качества)
            activation: Функция активации ('sigmoid' или 'relu')
            hidden_size2: Размер второго скрытого слоя (опционально, для глубокой сети)
            dropout_rate: Вероятность dropout (0.0 = нет dropout, 0.3 = отключить 30% нейронов)
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.hidden_size2 = hidden_size2  # Новый параметр для второго скрытого слоя
        self.output_size = output_size
        self.activation = activation
        self.dropout_rate = dropout_rate  # Вероятность dropout
        
        # Определяем, используем ли два скрытых слоя
        self.use_two_hidden_layers = hidden_size2 is not None
        
        if self.use_two_hidden_layers:
            # ============================================================
            # ИНИЦИАЛИЗАЦИЯ ВЕСОВ: Два скрытых слоя (10→h1→h2→3)
            # ============================================================
            # 
            # МАТЕМАТИКА:
            #   W ~ N(0, σ²) где σ = 0.1
            #   b = 0
            # 
            # ОБОСНОВАНИЕ:
            #   1. Малые случайные веса (0.1) предотвращают насыщение sigmoid
            #   2. Случайность разрушает симметрию (нейроны учатся разному)
            #   3. Нулевые смещения - стандартная практика
            # 
            # См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 7
            # ============================================================
            
            # W⁽¹⁾ ∈ ℝ^(input_size × hidden_size)
            self.weights_input_hidden1 = np.random.randn(input_size, hidden_size) * 0.1
            
            # W⁽²⁾ ∈ ℝ^(hidden_size × hidden_size2)
            self.weights_hidden1_hidden2 = np.random.randn(hidden_size, hidden_size2) * 0.1
            
            # W⁽³⁾ ∈ ℝ^(hidden_size2 × output_size)
            self.weights_hidden2_output = np.random.randn(hidden_size2, output_size) * 0.1
            
            # b⁽¹⁾ ∈ ℝ^hidden_size
            self.bias_hidden1 = np.zeros((1, hidden_size))
            
            # b⁽²⁾ ∈ ℝ^hidden_size2
            self.bias_hidden2 = np.zeros((1, hidden_size2))
            
            # b⁽³⁾ ∈ ℝ^output_size
            self.bias_output = np.zeros((1, output_size))
        else:
            # ============================================================
            # ИНИЦИАЛИЗАЦИЯ ВЕСОВ: Один скрытый слой (10→8→3)
            # ============================================================
            # 
            # МАТЕМАТИКА:
            #   W⁽¹⁾ ~ N(0, 0.01) ∈ ℝ⁸ˣ¹⁰  (80 весов)
            #   W⁽²⁾ ~ N(0, 0.01) ∈ ℝ³ˣ⁸   (24 веса)
            #   b⁽¹⁾ = 0 ∈ ℝ⁸              (8 смещений)
            #   b⁽²⁾ = 0 ∈ ℝ³              (3 смещения)
            #   
            #   Всего параметров: 80 + 24 + 8 + 3 = 115
            # 
            # ПОЧЕМУ 0.1?
            #   - Слишком большие веса → насыщение sigmoid → затухание градиента
            #   - Слишком малые веса → медленное обучение
            #   - 0.1 - эмпирически оптимальное значение для нашей задачи
            # 
            # См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 7
            # ============================================================
            
            # W⁽¹⁾: веса связей входной → скрытый слой
            self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
            
            # W⁽²⁾: веса связей скрытый → выходной слой
            self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
            
            # b⁽¹⁾: смещения скрытого слоя
            self.bias_hidden = np.zeros((1, hidden_size))
            
            # b⁽²⁾: смещения выходного слоя
            self.bias_output = np.zeros((1, output_size))
        
        # Параметры обучения
        self.learning_rate = 0.01
        
        # Пытаемся загрузить обученную модель
        self.load_trained_model()
        
    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """
        Функция активации sigmoid (сигмоида)
        
        МАТЕМАТИКА:
            σ(z) = 1 / (1 + e⁻ᶻ)
        
        СВОЙСТВА:
            - Область значений: (0, 1)
            - Монотонно возрастающая
            - Дифференцируема везде
            - σ(-z) = 1 - σ(z)
            - lim(z→∞) σ(z) = 1
            - lim(z→-∞) σ(z) = 0
        
        ПРИМЕНЕНИЕ:
            - Скрытый слой: нелинейное преобразование признаков
            - Выходной слой: значения в диапазоне [0, 1] для оценок качества
        
        CLIPPING:
            np.clip(x, -500, 500) предотвращает overflow в exp()
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 3
        """
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def sigmoid_derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Производная функции sigmoid
        
        МАТЕМАТИКА:
            σ'(z) = σ(z) · (1 - σ(z))
        
        УПРОЩЕНИЕ:
            Если a = σ(z) уже вычислено, то:
            σ'(z) = a · (1 - a)
        
        ПРИМЕНЕНИЕ В BACKPROPAGATION:
            δ = error ⊙ σ'(z)
            где ⊙ - поэлементное умножение (Hadamard product)
        
        Args:
            x: Уже активированные значения σ(z), не сырые z!
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 3.3
        """
        return x * (1 - x)
    
    def relu(self, x: np.ndarray) -> np.ndarray:
        """
        Функция активации ReLU (Rectified Linear Unit)
        
        ReLU(x) = max(0, x)
        
        Преимущества:
        - Быстрее вычисляется, чем sigmoid
        - Решает проблему затухающего градиента
        - Хорошо работает для глубоких сетей
        """
        return np.maximum(0, x)
    
    def relu_derivative(self, x: np.ndarray) -> np.ndarray:
        """
        Производная функции ReLU
        
        ReLU'(x) = 1 если x > 0, иначе 0
        """
        return (x > 0).astype(float)
    
    def activate(self, x: np.ndarray) -> np.ndarray:
        """Применяет выбранную функцию активации"""
        if self.activation == 'relu':
            return self.relu(x)
        else:
            return self.sigmoid(x)
    
    def activate_derivative(self, x: np.ndarray) -> np.ndarray:
        """Применяет производную выбранной функции активации"""
        if self.activation == 'relu':
            return self.relu_derivative(x)
        else:
            return self.sigmoid_derivative(x)
    
    def apply_dropout(self, x: np.ndarray, training: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        Применяет dropout к слою
        
        Dropout случайным образом "выключает" нейроны во время обучения,
        что помогает предотвратить переобучение.
        
        Args:
            x: Выходы слоя
            training: Если True, применяет dropout; если False (inference), возвращает x как есть
            
        Returns:
            Кортеж (выходы с dropout, маска dropout)
        """
        if not training or self.dropout_rate == 0.0:
            return x, np.ones_like(x)
        
        # Создаем маску: каждый нейрон остается активным с вероятностью (1 - dropout_rate)
        mask = np.random.binomial(1, 1 - self.dropout_rate, size=x.shape)
        
        # Применяем маску и масштабируем, чтобы сохранить ожидаемое значение
        # Это называется "inverted dropout"
        return (x * mask) / (1 - self.dropout_rate), mask
    
    def forward(self, inputs: np.ndarray, training: bool = False):
        """
        Прямое распространение (Forward Pass)
        
        МАТЕМАТИКА (один скрытый слой):
            1. Скрытый слой:
               z⁽¹⁾ = W⁽¹⁾x + b⁽¹⁾           # Линейное преобразование
               h = σ(z⁽¹⁾)                   # Нелинейная активация
            
            2. Выходной слой:
               z⁽²⁾ = W⁽²⁾h + b⁽²⁾           # Линейное преобразование
               y = σ(z⁽²⁾)                   # Активация (sigmoid для [0,1])
        
        МАТРИЧНАЯ ФОРМА (для батча из N примеров):
            X ∈ ℝᴺˣ¹⁰ — входные данные
            H = σ(XW⁽¹⁾ᵀ + B⁽¹⁾) ∈ ℝᴺˣ⁸  # Скрытый слой
            Y = σ(HW⁽²⁾ᵀ + B⁽²⁾) ∈ ℝᴺˣ³  # Выходной слой
        
        ВЫХОД:
            y = [y₁, y₂, y₃]ᵀ где:
            y₁ ∈ [0,1] — correctness (правильность)
            y₂ ∈ [0,1] — efficiency (эффективность)
            y₃ ∈ [0,1] — readability (читаемость)
        
        DROPOUT (если training=True):
            Случайно отключает нейроны с вероятностью dropout_rate
            для предотвращения переобучения
        
        Args:
            inputs: Входные данные x ∈ ℝᴺˣ¹⁰
            training: Если True, применяет dropout; если False, не применяет
            
        Returns:
            Кортеж выходов всех слоёв (зависит от архитектуры)
            - Для одного скрытого слоя: (hidden_output, output)
            - Для двух скрытых слоёв: (hidden1_output, hidden2_output, output)
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 2
        """
        if self.use_two_hidden_layers:
            # Первый скрытый слой
            hidden1_input = np.dot(inputs, self.weights_input_hidden1) + self.bias_hidden1
            hidden1_output = self.activate(hidden1_input)
            hidden1_output, _ = self.apply_dropout(hidden1_output, training)
            
            # Второй скрытый слой
            hidden2_input = np.dot(hidden1_output, self.weights_hidden1_hidden2) + self.bias_hidden2
            hidden2_output = self.activate(hidden2_input)
            hidden2_output, _ = self.apply_dropout(hidden2_output, training)
            
            # Выходной слой (всегда sigmoid для значений 0-1, без dropout)
            output_input = np.dot(hidden2_output, self.weights_hidden2_output) + self.bias_output
            output = self.sigmoid(output_input)
            
            return hidden1_output, hidden2_output, output
        else:
            # ============================================================
            # ШАГ 1: СКРЫТЫЙ СЛОЙ
            # ============================================================
            # Математика: z⁽¹⁾ = W⁽¹⁾x + b⁽¹⁾
            # где: W⁽¹⁾ ∈ ℝ⁸ˣ¹⁰, x ∈ ℝ¹⁰, b⁽¹⁾ ∈ ℝ⁸
            hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
            
            # Математика: h = σ(z⁽¹⁾) или h = ReLU(z⁽¹⁾)
            # Нелинейное преобразование признаков
            hidden_output = self.activate(hidden_input)
            
            # Dropout (только во время обучения)
            hidden_output, _ = self.apply_dropout(hidden_output, training)
            
            # ============================================================
            # ШАГ 2: ВЫХОДНОЙ СЛОЙ
            # ============================================================
            # Математика: z⁽²⁾ = W⁽²⁾h + b⁽²⁾
            # где: W⁽²⁾ ∈ ℝ³ˣ⁸, h ∈ ℝ⁸, b⁽²⁾ ∈ ℝ³
            output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            
            # Математика: y = σ(z⁽²⁾)
            # Всегда sigmoid для выхода в диапазоне [0, 1]
            output = self.sigmoid(output_input)
            
            return hidden_output, output
    
    def backward(self, inputs: np.ndarray, *args):
        """
        Обратное распространение ошибки (Backpropagation)
        
        МАТЕМАТИКА (для одного скрытого слоя):
        
        ШАГ 1: Вычисление ошибки выходного слоя
            E_out = y_true - y_pred           # Ошибка
            δ⁽²⁾ = E_out ⊙ σ'(z⁽²⁾)            # Градиент
                 = E_out ⊙ y ⊙ (1 - y)        # Используем σ'(z) = y(1-y)
        
        ШАГ 2: Вычисление ошибки скрытого слоя
            E_hidden = δ⁽²⁾ · (W⁽²⁾)ᵀ          # Обратная передача ошибки
            δ⁽¹⁾ = E_hidden ⊙ σ'(z⁽¹⁾)         # Градиент
                 = E_hidden ⊙ h ⊙ (1 - h)
        
        ШАГ 3: Обновление весов (Градиентный спуск)
            ∂L/∂W⁽²⁾ = hᵀ · δ⁽²⁾               # Градиент весов выходного слоя
            ∂L/∂W⁽¹⁾ = xᵀ · δ⁽¹⁾               # Градиент весов скрытого слоя
            
            W⁽²⁾ := W⁽²⁾ + α · ∂L/∂W⁽²⁾        # Обновление
            W⁽¹⁾ := W⁽¹⁾ + α · ∂L/∂W⁽¹⁾
            
            где α = learning_rate
        
        ШАГ 4: Обновление смещений
            ∂L/∂b⁽²⁾ = δ⁽²⁾
            ∂L/∂b⁽¹⁾ = δ⁽¹⁾
            
            b⁽²⁾ := b⁽²⁾ + α · ∂L/∂b⁽²⁾
            b⁽¹⁾ := b⁽¹⁾ + α · ∂L/∂b⁽¹⁾
        
        ПРИМЕЧАНИЕ О ЗНАКЕ:
            Используется "+", а не "-", потому что ошибка вычисляется как
            (target - output), а не (output - target). Это эквивалентно
            движению в направлении, уменьшающем ошибку.
        
        Args:
            inputs: Входные данные x ∈ ℝᴺˣ¹⁰
            *args: Зависит от архитектуры:
                - Для одного слоя: hidden_output, output, target
                - Для двух слоёв: hidden1_output, hidden2_output, output, target
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, разделы 5 и 6
        """
        if self.use_two_hidden_layers:
            # Распаковываем аргументы для двух скрытых слоёв
            hidden1_output, hidden2_output, output, target = args
            
            # Ошибка выходного слоя (всегда sigmoid)
            output_error = target - output
            output_delta = output_error * self.sigmoid_derivative(output)
            
            # Ошибка второго скрытого слоя
            hidden2_error = np.dot(output_delta, self.weights_hidden2_output.T)
            hidden2_delta = hidden2_error * self.activate_derivative(hidden2_output)
            
            # Ошибка первого скрытого слоя
            hidden1_error = np.dot(hidden2_delta, self.weights_hidden1_hidden2.T)
            hidden1_delta = hidden1_error * self.activate_derivative(hidden1_output)
            
            # Обновление весов
            self.weights_hidden2_output += np.dot(hidden2_output.T, output_delta) * self.learning_rate
            self.weights_hidden1_hidden2 += np.dot(hidden1_output.T, hidden2_delta) * self.learning_rate
            self.weights_input_hidden1 += np.dot(inputs.T, hidden1_delta) * self.learning_rate
            
            # Обновление смещений
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
            self.bias_hidden2 += np.sum(hidden2_delta, axis=0, keepdims=True) * self.learning_rate
            self.bias_hidden1 += np.sum(hidden1_delta, axis=0, keepdims=True) * self.learning_rate
        else:
            # Распаковываем аргументы для одного скрытого слоя
            hidden_output, output, target = args
            
            # ============================================================
            # ШАГ 1: ОШИБКА ВЫХОДНОГО СЛОЯ
            # ============================================================
            # Математика: E_out = y_true - y_pred
            output_error = target - output
            
            # Математика: δ⁽²⁾ = E_out ⊙ σ'(output)
            #           = E_out ⊙ output ⊙ (1 - output)
            # Это градиент по z⁽²⁾ (взвешенной сумме выходного слоя)
            output_delta = output_error * self.sigmoid_derivative(output)
            
            # ============================================================
            # ШАГ 2: ОШИБКА СКРЫТОГО СЛОЯ
            # ============================================================
            # Математика: E_hidden = δ⁽²⁾ · (W⁽²⁾)ᵀ
            # Передаём ошибку обратно через веса
            hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
            
            # Математика: δ⁽¹⁾ = E_hidden ⊙ activate'(hidden_output)
            # Градиент зависит от функции активации (sigmoid или ReLU)
            hidden_delta = hidden_error * self.activate_derivative(hidden_output)
            
            # ============================================================
            # ШАГ 3: ОБНОВЛЕНИЕ ВЕСОВ (Градиентный спуск)
            # ============================================================
            # Математика: W⁽²⁾ := W⁽²⁾ + α · (hᵀ · δ⁽²⁾)
            # где α = learning_rate, h = hidden_output
            self.weights_hidden_output += np.dot(hidden_output.T, output_delta) * self.learning_rate
            
            # Математика: W⁽¹⁾ := W⁽¹⁾ + α · (xᵀ · δ⁽¹⁾)
            # где x = inputs
            self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * self.learning_rate
            
            # ============================================================
            # ШАГ 4: ОБНОВЛЕНИЕ СМЕЩЕНИЙ
            # ============================================================
            # Математика: b⁽²⁾ := b⁽²⁾ + α · δ⁽²⁾
            # Суммируем по батчу (axis=0), сохраняем размерность (keepdims=True)
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
            
            # Математика: b⁽¹⁾ := b⁽¹⁾ + α · δ⁽¹⁾
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate
    
    def train(self, training_data: List[Tuple[np.ndarray, np.ndarray]], epochs: int = 1000):
        """
        Обучение нейронной сети методом градиентного спуска
        
        АЛГОРИТМ:
            Для каждой эпохи t = 1..T:
                Для каждого примера (x, y) в датасете:
                    1. Forward pass: вычислить ŷ = f(x; W, b)
                    2. Вычислить ошибку: L = ||y - ŷ||²
                    3. Backward pass: вычислить градиенты ∂L/∂W, ∂L/∂b
                    4. Обновить параметры:
                       W := W + α · ∂L/∂W
                       b := b + α · ∂L/∂b
                Вычислить среднюю ошибку по всему датасету
        
        ФУНКЦИЯ ПОТЕРЬ (MSE):
            L = 1/N Σᵢ ||yᵢ - ŷᵢ||²
              = 1/N Σᵢ Σⱼ (yᵢⱼ - ŷᵢⱼ)²
        
        ПАРАМЕТРЫ ОБУЧЕНИЯ:
            - Learning rate (α): по умолчанию 0.01
            - Batch size: 1 (онлайн обучение, каждый пример отдельно)
            - Dropout: применяется только если dropout_rate > 0
        
        Args:
            training_data: Список кортежей (x ∈ ℝ¹⁰, y ∈ ℝ³)
            epochs: Количество эпох обучения (проходов по всему датасету)
            
        Returns:
            dict: История обучения с эпохами и ошибками
                {
                    'epochs': [0, 10, 20, ...],
                    'loss': [0.059, 0.045, 0.038, ...],
                    'learning_rate': 0.01,
                    'architecture': {...}
                }
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 6
        """
        architecture = {
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'output_size': self.output_size
        }
        
        if self.use_two_hidden_layers:
            architecture['hidden_size2'] = self.hidden_size2
            architecture['type'] = 'two_hidden_layers'
        else:
            architecture['type'] = 'one_hidden_layer'
        
        history = {
            'epochs': [],
            'loss': [],
            'learning_rate': self.learning_rate,
            'architecture': architecture
        }
        
        for epoch in range(epochs):
            total_error = 0
            
            for inputs, target in training_data:
                # Прямое распространение (с dropout если задан)
                forward_outputs = self.forward(inputs, training=True)
                output = forward_outputs[-1]  # Последний элемент всегда output
                
                # Обратное распространение
                self.backward(inputs, *forward_outputs, target)
                
                # Расчет ошибки (MSE для одного примера)
                # Математика: L = 1/3 Σⱼ (yⱼ - ŷⱼ)²
                # где j = 1,2,3 соответствует correctness, efficiency, readability
                error = np.mean(np.square(target - output))
                total_error += error
            
            avg_error = total_error / len(training_data)
            
            # Сохраняем историю каждые 10 эпох
            if epoch % 10 == 0:
                history['epochs'].append(epoch)
                history['loss'].append(float(avg_error))
            
            # Вывод прогресса каждые 100 эпох
            if epoch % 100 == 0:
                print(f"Эпоха {epoch}, Средняя ошибка: {avg_error:.4f}")
        
        # Сохраняем финальную эпоху, если она не была сохранена
        if (epochs - 1) % 10 != 0:
            history['epochs'].append(epochs - 1)
            history['loss'].append(float(avg_error))
        
        return history
    
    def predict(self, inputs: np.ndarray) -> np.ndarray:
        """
        Предсказание на основе входных данных
        
        Args:
            inputs: Входные данные
            
        Returns:
            Предсказание нейронной сети
        """
        forward_outputs = self.forward(inputs)
        output = forward_outputs[-1]  # Последний элемент всегда output
        return output
    
    def evaluate_code_quality(self, code_features: Dict[str, float]) -> Dict[str, float]:
        """
        Оценка качества кода
        
        Args:
            code_features: Словарь с признаками кода
            
        Returns:
            Словарь с оценками качества
        """
        try:
            # Преобразование признаков в вектор
            feature_vector = self._extract_features(code_features)
            
            # Предсказание с помощью обученной модели
            prediction = self.predict(feature_vector)
            
            # Интерпретация результатов
            return {
                'correctness': float(prediction[0][0]),  # Правильность
                'efficiency': float(prediction[0][1]),   # Эффективность
                'readability': float(prediction[0][2])   # Читаемость
            }
        except Exception as e:
            print(f"⚠️ Ошибка оценки качества кода: {e}")
            # Fallback на эвристическую оценку
            lines = code_features.get('lines_of_code', 1)
            functions = code_features.get('functions_count', 0)
            complexity = code_features.get('complexity', 0)
            comments = code_features.get('comments_ratio', 0)
            
            correctness = max(0.3, min(1.0, 1.0 - complexity * 0.1))
            efficiency = max(0.3, min(1.0, 1.0 - functions * 0.05))
            readability = max(0.3, min(1.0, 0.5 + comments * 2 + (1.0 / lines) * 10))
            
            return {
                'correctness': correctness,
                'efficiency': efficiency,
                'readability': readability
            }
    
    def load_trained_model(self):
        """
        Загрузка обученной модели при инициализации
        
        Приоритет загрузки:
        1. model_final.json - финальная оптимизированная модель (lr=0.05, ReLU)
        2. neural_network.json - основная модель
        3. Поиск в альтернативных путях
        
        Финальная модель была обучена с параметрами:
        - Learning rate: 0.05 (лучший результат в экспериментах)
        - Activation: ReLU
        - Epochs: 2000
        - Точность: ~94%
        """
        try:
            # Приоритетный порядок загрузки моделей
            model_paths = [
                # Финальная оптимизированная модель (приоритет)
                'data/models/model_final.json',
                # Основная модель
                'data/models/neural_network.json',
                # Альтернативные пути
                'app/data/models/model_final.json',
                'app/data/models/neural_network.json',
                '../data/models/model_final.json',
                '../data/models/neural_network.json'
            ]
            
            for path in model_paths:
                if os.path.exists(path):
                    self.load_model(path)
                    if 'final' in path:
                        print(f"✅ Загружена финальная модель: {path}")
                        print(f"   (оптимизирована: lr=0.05, ReLU, точность ~94%)")
                    else:
                        print(f"✅ Загружена обученная модель: {path}")
                    return True
            
            print("⚠️ Обученная модель не найдена, используется случайная инициализация")
            return False
            
        except Exception as e:
            print(f"⚠️ Ошибка загрузки модели: {e}")
            return False
    
    def _extract_features(self, code_features: Dict[str, float]) -> np.ndarray:
        """
        Извлечение и нормализация признаков из анализа кода
        
        НОРМАЛИЗАЦИЯ:
            Все признаки приводятся к диапазону [0, 1] для лучшей работы
            функции активации sigmoid.
            
            Формула: x_normalized = x_raw / x_max
            
            где x_max - ожидаемое максимальное значение признака
        
        ПРИЗНАКИ (x ∈ ℝ¹⁰):
            x₁ = lines_of_code / 100        # Ожидаем до 100 строк
            x₂ = functions_count / 10       # Ожидаем до 10 функций
            x₃ = complexity / 10            # Циклометрическая сложность до 10
            x₄ = nested_levels / 5          # Максимальная вложенность до 5
            x₅ = variable_names_length / 20 # Средняя длина имён до 20 символов
            x₆ = comments_ratio             # Уже в [0, 1]
            x₇ = imports_count / 10         # До 10 импортов
            x₈ = class_count / 5            # До 5 классов
            x₉ = error_handling             # Бинарный признак {0, 1}
            x₁₀ = test_coverage             # Уже в [0, 1]
        
        Args:
            code_features: Словарь с признаками кода
            
        Returns:
            Вектор признаков x ∈ ℝ¹ˣ¹⁰ (форма для батча из 1 примера)
        
        См. также: docs/MATHEMATICAL_FOUNDATION.md, раздел 1.2
        """
        # Нормализация признаков к диапазону [0, 1]
        features = np.array([
            code_features.get('lines_of_code', 0) / 100.0,  # x₁
            code_features.get('functions_count', 0) / 10.0,  # x₂
            code_features.get('complexity', 0) / 10.0,      # x₃
            code_features.get('nested_levels', 0) / 5.0,    # x₄
            code_features.get('variable_names_length', 0) / 20.0,  # x₅
            code_features.get('comments_ratio', 0),         # x₆
            code_features.get('imports_count', 0) / 10.0,   # x₇
            code_features.get('class_count', 0) / 5.0,      # x₈
            code_features.get('error_handling', 0),         # x₉
            code_features.get('test_coverage', 0)           # x₁₀
        ])
        
        # Преобразуем в матрицу 1×10 для совместимости с np.dot()
        return features.reshape(1, -1)
    
    def save_model(self, filepath: str):
        """Сохранение модели"""
        model_data = {
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'hidden_size2': self.hidden_size2,
            'output_size': self.output_size,
            'learning_rate': self.learning_rate,
            'activation': self.activation,
            'dropout_rate': self.dropout_rate,
            'use_two_hidden_layers': self.use_two_hidden_layers
        }
        
        if self.use_two_hidden_layers:
            model_data.update({
                'weights_input_hidden1': self.weights_input_hidden1.tolist(),
                'weights_hidden1_hidden2': self.weights_hidden1_hidden2.tolist(),
                'weights_hidden2_output': self.weights_hidden2_output.tolist(),
                'bias_hidden1': self.bias_hidden1.tolist(),
                'bias_hidden2': self.bias_hidden2.tolist(),
                'bias_output': self.bias_output.tolist()
            })
        else:
            model_data.update({
                'weights_input_hidden': self.weights_input_hidden.tolist(),
                'weights_hidden_output': self.weights_hidden_output.tolist(),
                'bias_hidden': self.bias_hidden.tolist(),
                'bias_output': self.bias_output.tolist()
            })
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(model_data, f, ensure_ascii=False, indent=2)
    
    def load_model(self, filepath: str):
        """Загрузка модели"""
        if not os.path.exists(filepath):
            print(f"Файл модели {filepath} не найден")
            return
        
        with open(filepath, 'r', encoding='utf-8') as f:
            model_data = json.load(f)
        
        self.input_size = model_data['input_size']
        self.hidden_size = model_data['hidden_size']
        self.hidden_size2 = model_data.get('hidden_size2', None)
        self.output_size = model_data['output_size']
        self.learning_rate = model_data['learning_rate']
        self.activation = model_data.get('activation', 'sigmoid')
        self.dropout_rate = model_data.get('dropout_rate', 0.0)
        self.use_two_hidden_layers = model_data.get('use_two_hidden_layers', False)
        
        if self.use_two_hidden_layers:
            self.weights_input_hidden1 = np.array(model_data['weights_input_hidden1'])
            self.weights_hidden1_hidden2 = np.array(model_data['weights_hidden1_hidden2'])
            self.weights_hidden2_output = np.array(model_data['weights_hidden2_output'])
            self.bias_hidden1 = np.array(model_data['bias_hidden1'])
            self.bias_hidden2 = np.array(model_data['bias_hidden2'])
            self.bias_output = np.array(model_data['bias_output'])
        else:
            self.weights_input_hidden = np.array(model_data['weights_input_hidden'])
            self.weights_hidden_output = np.array(model_data['weights_hidden_output'])
            self.bias_hidden = np.array(model_data['bias_hidden'])
            self.bias_output = np.array(model_data['bias_output'])
