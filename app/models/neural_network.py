"""
Простая нейронная сеть для анализа качества кода Python
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
                 activation: str = 'sigmoid', hidden_size2: int = None):
        """
        Инициализация нейронной сети
        
        Args:
            input_size: Размер входного слоя (количество признаков)
            hidden_size: Размер первого скрытого слоя
            output_size: Размер выходного слоя (оценка качества)
            activation: Функция активации ('sigmoid' или 'relu')
            hidden_size2: Размер второго скрытого слоя (опционально, для глубокой сети)
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.hidden_size2 = hidden_size2  # Новый параметр для второго скрытого слоя
        self.output_size = output_size
        self.activation = activation
        
        # Определяем, используем ли два скрытых слоя
        self.use_two_hidden_layers = hidden_size2 is not None
        
        if self.use_two_hidden_layers:
            # Архитектура с двумя скрытыми слоями: Input → Hidden1 → Hidden2 → Output
            self.weights_input_hidden1 = np.random.randn(input_size, hidden_size) * 0.1
            self.weights_hidden1_hidden2 = np.random.randn(hidden_size, hidden_size2) * 0.1
            self.weights_hidden2_output = np.random.randn(hidden_size2, output_size) * 0.1
            
            self.bias_hidden1 = np.zeros((1, hidden_size))
            self.bias_hidden2 = np.zeros((1, hidden_size2))
            self.bias_output = np.zeros((1, output_size))
        else:
            # Архитектура с одним скрытым слоем: Input → Hidden → Output
            self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
            self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
            
            self.bias_hidden = np.zeros((1, hidden_size))
            self.bias_output = np.zeros((1, output_size))
        
        # Параметры обучения
        self.learning_rate = 0.01
        
        # Пытаемся загрузить обученную модель
        self.load_trained_model()
        
    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Функция активации sigmoid"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def sigmoid_derivative(self, x: np.ndarray) -> np.ndarray:
        """Производная функции sigmoid"""
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
    
    def forward(self, inputs: np.ndarray):
        """
        Прямое распространение
        
        Args:
            inputs: Входные данные
            
        Returns:
            Кортеж выходов всех слоёв (зависит от архитектуры)
            - Для одного скрытого слоя: (hidden_output, output)
            - Для двух скрытых слоёв: (hidden1_output, hidden2_output, output)
        """
        if self.use_two_hidden_layers:
            # Первый скрытый слой
            hidden1_input = np.dot(inputs, self.weights_input_hidden1) + self.bias_hidden1
            hidden1_output = self.activate(hidden1_input)
            
            # Второй скрытый слой
            hidden2_input = np.dot(hidden1_output, self.weights_hidden1_hidden2) + self.bias_hidden2
            hidden2_output = self.activate(hidden2_input)
            
            # Выходной слой (всегда sigmoid для значений 0-1)
            output_input = np.dot(hidden2_output, self.weights_hidden2_output) + self.bias_output
            output = self.sigmoid(output_input)
            
            return hidden1_output, hidden2_output, output
        else:
            # Скрытый слой (используем выбранную функцию активации)
            hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
            hidden_output = self.activate(hidden_input)
            
            # Выходной слой (всегда sigmoid для значений 0-1)
            output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            output = self.sigmoid(output_input)
            
            return hidden_output, output
    
    def backward(self, inputs: np.ndarray, *args):
        """
        Обратное распространение ошибки
        
        Args:
            inputs: Входные данные
            *args: Зависит от архитектуры:
                - Для одного слоя: hidden_output, output, target
                - Для двух слоёв: hidden1_output, hidden2_output, output, target
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
            
            # Ошибка выходного слоя (всегда sigmoid)
            output_error = target - output
            output_delta = output_error * self.sigmoid_derivative(output)
            
            # Ошибка скрытого слоя (используем выбранную функцию активации)
            hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.activate_derivative(hidden_output)
            
            # Обновление весов
            self.weights_hidden_output += np.dot(hidden_output.T, output_delta) * self.learning_rate
            self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * self.learning_rate
            
            # Обновление смещений
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate
    
    def train(self, training_data: List[Tuple[np.ndarray, np.ndarray]], epochs: int = 1000):
        """
        Обучение нейронной сети
        
        Args:
            training_data: Список кортежей (входные данные, ожидаемые выходы)
            epochs: Количество эпох обучения
            
        Returns:
            dict: История обучения с эпохами и ошибками
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
                # Прямое распространение
                forward_outputs = self.forward(inputs)
                output = forward_outputs[-1]  # Последний элемент всегда output
                
                # Обратное распространение
                self.backward(inputs, *forward_outputs, target)
                
                # Расчет ошибки
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
        """Загрузка обученной модели при инициализации"""
        try:
            # Ищем модель в разных местах
            model_paths = [
                'data/models/neural_network.json',
                'app/data/models/neural_network.json',
                '../data/models/neural_network.json'
            ]
            
            for path in model_paths:
                if os.path.exists(path):
                    self.load_model(path)
                    print(f"✅ Загружена обученная модель: {path}")
                    return True
            
            print("⚠️ Обученная модель не найдена, используется случайная инициализация")
            return False
            
        except Exception as e:
            print(f"⚠️ Ошибка загрузки модели: {e}")
            return False
    
    def _extract_features(self, code_features: Dict[str, float]) -> np.ndarray:
        """
        Извлечение признаков из анализа кода
        
        Args:
            code_features: Словарь с признаками
            
        Returns:
            Вектор признаков для нейронной сети
        """
        # Нормализация признаков
        features = np.array([
            code_features.get('lines_of_code', 0) / 100.0,  # Количество строк
            code_features.get('functions_count', 0) / 10.0,  # Количество функций
            code_features.get('complexity', 0) / 10.0,      # Сложность
            code_features.get('nested_levels', 0) / 5.0,    # Уровень вложенности
            code_features.get('variable_names_length', 0) / 20.0,  # Длина имен переменных
            code_features.get('comments_ratio', 0),         # Отношение комментариев
            code_features.get('imports_count', 0) / 10.0,   # Количество импортов
            code_features.get('class_count', 0) / 5.0,      # Количество классов
            code_features.get('error_handling', 0),         # Обработка ошибок
            code_features.get('test_coverage', 0)           # Покрытие тестами
        ])
        
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
