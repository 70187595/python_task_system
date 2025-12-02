"""
Эксперимент 9: Обучение модели с двумя скрытыми слоями
Архитектура: 10 → 16 → 8 → 3
Цель: Проверить, улучшит ли добавление второго скрытого слоя качество предсказаний
"""

import sys
import os
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.neural_network import SimpleNeuralNetwork


def load_and_prepare_data():
    """Загрузка и подготовка данных"""
    with open('data/training_data/training_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    X = []
    y = []
    
    for item in data:
        features = item['features']
        target = item['target']
        
        feature_vector = [
            features['lines_of_code'] / 100.0,
            features['functions_count'] / 10.0,
            features['complexity'],
            features['nested_levels'] / 5.0,
            features['variable_names_length'] / 20.0,
            features['comments_ratio'],
            features['imports_count'] / 10.0,
            features['class_count'] / 5.0,
            features['error_handling'],
            features['test_coverage']
        ]
        
        X.append(feature_vector)
        y.append(target)
    
    return np.array(X), np.array(y), len(data)


def main():
    print("🧪 ЭКСПЕРИМЕНТ 9: Два скрытых слоя (10→16→8→3)")
    print("=" * 60)
    
    # Загружаем данные
    X, y, data_size = load_and_prepare_data()
    print(f"✅ Загружено {data_size} примеров")
    
    # Создаем сеть с двумя скрытыми слоями
    # НЕ загружаем предобученную модель - создаем новую с нуля
    network = SimpleNeuralNetwork(
        input_size=10,
        hidden_size=16,      # Первый скрытый слой
        output_size=3,
        activation='sigmoid',
        hidden_size2=8       # Второй скрытый слой
    )
    
    # Переинициализируем веса, чтобы не использовать загруженную модель
    if network.use_two_hidden_layers:
        network.weights_input_hidden1 = np.random.randn(10, 16) * 0.1
        network.weights_hidden1_hidden2 = np.random.randn(16, 8) * 0.1
        network.weights_hidden2_output = np.random.randn(8, 3) * 0.1
        network.bias_hidden1 = np.zeros((1, 16))
        network.bias_hidden2 = np.zeros((1, 8))
        network.bias_output = np.zeros((1, 3))
    
    network.learning_rate = 0.01
    
    print(f"\n🔧 Параметры:")
    print(f"   Архитектура: 10 → 16 → 8 → 3")
    print(f"   Learning rate: 0.01")
    print(f"   Epochs: 2000")
    print(f"   Activation: Sigmoid")
    print(f"   Тип: Двухслойная глубокая сеть")
    
    # Подсчет параметров модели
    params_w1 = 10 * 16
    params_b1 = 16
    params_w2 = 16 * 8
    params_b2 = 8
    params_w3 = 8 * 3
    params_b3 = 3
    total_params = params_w1 + params_b1 + params_w2 + params_b2 + params_w3 + params_b3
    
    print(f"\n📊 Количество параметров:")
    print(f"   W1 (10×16): {params_w1}")
    print(f"   b1: {params_b1}")
    print(f"   W2 (16×8): {params_w2}")
    print(f"   b2: {params_b2}")
    print(f"   W3 (8×3): {params_w3}")
    print(f"   b3: {params_b3}")
    print(f"   Всего: {total_params} параметров")
    print(f"   Сравнение с baseline (115 параметров): +{total_params - 115} (+{((total_params - 115)/115)*100:.1f}%)")
    
    # Обучаем
    training_data = [(X[i:i+1], y[i:i+1]) for i in range(len(X))]
    print(f"\n🚀 Начинаем обучение...")
    
    history = network.train(training_data, epochs=2000)
    
    # Сохраняем модель
    os.makedirs('experiments/results', exist_ok=True)
    network.save_model('experiments/results/model_exp9_two_layers.json')
    
    with open('experiments/results/history_exp9_two_layers.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)
    
    # Результаты
    print(f"\n📊 Результаты:")
    print(f"   Начальная ошибка: {history['loss'][0]:.4f}")
    print(f"   Конечная ошибка: {history['loss'][-1]:.4f}")
    improvement = (1 - history['loss'][-1]/history['loss'][0])*100 if history['loss'][0] > 0 else 0
    print(f"   Улучшение: {improvement:.1f}%")
    
    # Тестирование на нескольких примерах
    print(f"\n🧪 Тестирование на примерах:")
    test_indices = [0, 50, 100, 150, 200]
    total_error = 0
    test_count = 0
    
    for idx in test_indices:
        if idx < len(X):
            prediction = network.predict(X[idx]).flatten()
            target = y[idx]
            error = np.mean(np.abs(prediction - target))
            total_error += error
            test_count += 1
            
            print(f"\n   Пример {idx}:")
            print(f"   Ожидаемое:    [{target[0]:.2f}, {target[1]:.2f}, {target[2]:.2f}]")
            print(f"   Предсказание: [{prediction[0]:.2f}, {prediction[1]:.2f}, {prediction[2]:.2f}]")
            print(f"   Ошибка: {error:.4f}")
    
    avg_test_error = total_error / test_count if test_count > 0 else 0
    print(f"\n   📊 Средняя ошибка на тестах: {avg_test_error:.4f}")
    
    print(f"\n✅ Модель сохранена: experiments/results/model_exp9_two_layers.json")
    print(f"✅ История сохранена: experiments/results/history_exp9_two_layers.json")
    
    # Сравнение с baseline
    print(f"\n📈 Сравнение с предыдущими экспериментами:")
    print(f"   Baseline (8 нейронов, 1 слой):     0.0056")
    print(f"   Эксперимент 5 (lr=0.05):           0.0038 🏆")
    print(f"   Эксперимент 8 (ReLU):              0.0047")
    print(f"   Эксперимент 9 (2 слоя):            {history['loss'][-1]:.4f}")
    
    baseline_error = 0.0056
    if history['loss'][-1] < baseline_error:
        improvement_vs_baseline = ((baseline_error - history['loss'][-1])/baseline_error)*100
        print(f"   ✅ Два слоя лучше baseline на {improvement_vs_baseline:.1f}%")
    elif history['loss'][-1] > baseline_error:
        degradation = ((history['loss'][-1] - baseline_error)/baseline_error)*100
        print(f"   ⚠️  Два слоя хуже baseline на {degradation:.1f}%")
    else:
        print(f"   🔄 Результаты сопоставимы с baseline")
    
    print(f"\n💡 Выводы:")
    if history['loss'][-1] < 0.0045:
        print(f"   ✅ Глубокая архитектура показала отличные результаты!")
        print(f"   ✅ Дополнительный слой помог улучшить качество")
    elif history['loss'][-1] < 0.0056:
        print(f"   ✅ Глубокая архитектура работает хорошо")
        print(f"   ⚠️  Но выигрыш небольшой по сравнению с увеличением параметров")
    else:
        print(f"   ⚠️  Глубокая архитектура не показала преимущества")
        print(f"   💡 Возможно, нужно больше данных для обучения {total_params} параметров")


if __name__ == '__main__':
    main()

