"""
Эксперимент 7: Обучение модели с увеличенным количеством эпох (3000)
Цель: Проверить, даст ли дополнительное обучение лучшие результаты
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
    print("🧪 ЭКСПЕРИМЕНТ 7: epochs=3000")
    print("=" * 60)
    
    # Загружаем данные
    X, y, data_size = load_and_prepare_data()
    print(f"✅ Загружено {data_size} примеров")
    
    # Создаем сеть с увеличенным количеством эпох
    network = SimpleNeuralNetwork(
        input_size=10,
        hidden_size=8,
        output_size=3
    )
    network.learning_rate = 0.01
    
    print(f"\n🔧 Параметры:")
    print(f"   Input: 10, Hidden: 8, Output: 3")
    print(f"   Learning rate: 0.01")
    print(f"   Epochs: 3000 (увеличено)")
    
    # Обучаем
    training_data = [(X[i:i+1], y[i:i+1]) for i in range(len(X))]
    print(f"\n🚀 Начинаем обучение...")
    
    history = network.train(training_data, epochs=3000)
    
    # Сохраняем модель
    os.makedirs('experiments/results', exist_ok=True)
    network.save_model('experiments/results/model_exp7_epochs3000.json')
    
    with open('experiments/results/history_exp7_epochs3000.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)
    
    # Результаты
    print(f"\n📊 Результаты:")
    print(f"   Начальная ошибка: {history['loss'][0]:.4f}")
    print(f"   Конечная ошибка: {history['loss'][-1]:.4f}")
    print(f"   Улучшение: {(1 - history['loss'][-1]/history['loss'][0])*100:.1f}%")
    
    print(f"\n✅ Модель сохранена: experiments/results/model_exp7_epochs3000.json")
    print(f"✅ История сохранена: experiments/results/history_exp7_epochs3000.json")


if __name__ == '__main__':
    main()

