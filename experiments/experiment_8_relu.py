"""
Эксперимент 8: Обучение модели с ReLU активацией
Цель: Сравнить ReLU с sigmoid и проверить, улучшится ли качество
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
    print("🧪 ЭКСПЕРИМЕНТ 8: ReLU активация")
    print("=" * 60)
    
    # Загружаем данные
    X, y, data_size = load_and_prepare_data()
    print(f"✅ Загружено {data_size} примеров")
    
    # Создаем сеть с ReLU активацией
    network = SimpleNeuralNetwork(
        input_size=10,
        hidden_size=8,
        output_size=3,
        activation='relu'  # Используем ReLU вместо sigmoid
    )
    network.learning_rate = 0.01
    
    print(f"\n🔧 Параметры:")
    print(f"   Input: 10, Hidden: 8, Output: 3")
    print(f"   Learning rate: 0.01")
    print(f"   Epochs: 2000")
    print(f"   Activation: ReLU")
    
    # Обучаем
    training_data = [(X[i:i+1], y[i:i+1]) for i in range(len(X))]
    print(f"\n🚀 Начинаем обучение...")
    
    history = network.train(training_data, epochs=2000)
    
    # Сохраняем модель
    os.makedirs('experiments/results', exist_ok=True)
    network.save_model('experiments/results/model_exp8_relu.json')
    
    with open('experiments/results/history_exp8_relu.json', 'w', encoding='utf-8') as f:
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
    
    for idx in test_indices:
        if idx < len(X):
            prediction = network.predict(X[idx]).flatten()
            target = y[idx]
            error = np.mean(np.abs(prediction - target))
            total_error += error
            
            print(f"\n   Пример {idx}:")
            print(f"   Ожидаемое:    [{target[0]:.2f}, {target[1]:.2f}, {target[2]:.2f}]")
            print(f"   Предсказание: [{prediction[0]:.2f}, {prediction[1]:.2f}, {prediction[2]:.2f}]")
            print(f"   Ошибка: {error:.4f}")
    
    avg_test_error = total_error / len([idx for idx in test_indices if idx < len(X)])
    print(f"\n   📊 Средняя ошибка на тестах: {avg_test_error:.4f}")
    
    print(f"\n✅ Модель сохранена: experiments/results/model_exp8_relu.json")
    print(f"✅ История сохранена: experiments/results/history_exp8_relu.json")
    
    # Сравнение с baseline (sigmoid)
    print(f"\n📈 Сравнение с baseline (sigmoid):")
    print(f"   Baseline конечная ошибка: 0.0056")
    print(f"   ReLU конечная ошибка: {history['loss'][-1]:.4f}")
    
    if history['loss'][-1] < 0.0056:
        print(f"   ✅ ReLU лучше на {((0.0056 - history['loss'][-1])/0.0056)*100:.1f}%")
    elif history['loss'][-1] > 0.0056:
        print(f"   ⚠️  ReLU хуже на {((history['loss'][-1] - 0.0056)/0.0056)*100:.1f}%")
    else:
        print(f"   🔄 Результаты сопоставимы")


if __name__ == '__main__':
    main()

