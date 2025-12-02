"""
Скрипт для экспериментов с гиперпараметрами нейронной сети
"""

import sys
import os
import json
import numpy as np
from datetime import datetime

# Добавляем путь к приложению
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.neural_network import SimpleNeuralNetwork


def load_training_data():
    """Загрузка обучающих данных"""
    try:
        with open('data/training_data/training_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("❌ Файл с обучающими данными не найден!")
        return None


def prepare_training_data(data):
    """Подготовка данных для обучения"""
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
    
    return np.array(X), np.array(y)


def evaluate_model(network, X, y):
    """
    Оценка качества модели
    
    Args:
        network: Обученная нейронная сеть
        X: Входные данные
        y: Целевые значения
        
    Returns:
        dict: Метрики качества
    """
    predictions = []
    for i in range(len(X)):
        pred = network.predict(X[i:i+1])
        predictions.append(pred[0])
    
    predictions = np.array(predictions)
    
    # Средняя абсолютная ошибка (MAE)
    mae = np.mean(np.abs(y - predictions))
    
    # Среднеквадратичная ошибка (MSE)
    mse = np.mean(np.square(y - predictions))
    
    # Корень из среднеквадратичной ошибки (RMSE)
    rmse = np.sqrt(mse)
    
    # MAE для каждой метрики
    mae_correctness = np.mean(np.abs(y[:, 0] - predictions[:, 0]))
    mae_efficiency = np.mean(np.abs(y[:, 1] - predictions[:, 1]))
    mae_readability = np.mean(np.abs(y[:, 2] - predictions[:, 2]))
    
    return {
        'mae': float(mae),
        'mse': float(mse),
        'rmse': float(rmse),
        'mae_correctness': float(mae_correctness),
        'mae_efficiency': float(mae_efficiency),
        'mae_readability': float(mae_readability)
    }


def run_experiment(config, X, y):
    """
    Запуск одного эксперимента
    
    Args:
        config: Конфигурация эксперимента
        X: Входные данные
        y: Целевые значения
        
    Returns:
        dict: Результаты эксперимента
    """
    print(f"\n{'='*70}")
    print(f"🧪 Эксперимент: {config['name']}")
    print(f"{'='*70}")
    print(f"   Hidden size: {config['hidden_size']}")
    print(f"   Learning rate: {config['learning_rate']}")
    print(f"   Epochs: {config['epochs']}")
    
    # Создаем сеть с заданными параметрами
    network = SimpleNeuralNetwork(
        input_size=X.shape[1],
        hidden_size=config['hidden_size'],
        output_size=y.shape[1]
    )
    network.learning_rate = config['learning_rate']
    
    # Подготавливаем данные
    training_data = [(X[i:i+1], y[i:i+1]) for i in range(len(X))]
    
    # Обучаем
    start_time = datetime.now()
    history = network.train(training_data, epochs=config['epochs'])
    training_time = (datetime.now() - start_time).total_seconds()
    
    # Оцениваем
    metrics = evaluate_model(network, X, y)
    
    # Результаты
    results = {
        'config': config,
        'history': history,
        'metrics': metrics,
        'training_time': training_time,
        'final_loss': history['loss'][-1]
    }
    
    print(f"\n📊 Результаты:")
    print(f"   MAE: {metrics['mae']:.4f}")
    print(f"   RMSE: {metrics['rmse']:.4f}")
    print(f"   Final Loss: {results['final_loss']:.4f}")
    print(f"   Training Time: {training_time:.2f}s")
    
    return results


def hyperparameter_tuning():
    """Подбор гиперпараметров"""
    print("🔬 ЭКСПЕРИМЕНТЫ С ГИПЕРПАРАМЕТРАМИ")
    print("=" * 70)
    
    # Загружаем данные
    data = load_training_data()
    if data is None:
        return
    
    X, y = prepare_training_data(data)
    print(f"✅ Загружено {len(data)} примеров обучающих данных\n")
    
    # Конфигурации экспериментов
    experiments = [
        {
            'name': 'Baseline (lr=0.01, hidden=8)',
            'hidden_size': 8,
            'learning_rate': 0.01,
            'epochs': 2000
        },
        {
            'name': 'Увеличенный скрытый слой (hidden=12)',
            'hidden_size': 12,
            'learning_rate': 0.01,
            'epochs': 2000
        },
        {
            'name': 'Уменьшенный скрытый слой (hidden=5)',
            'hidden_size': 5,
            'learning_rate': 0.01,
            'epochs': 2000
        },
        {
            'name': 'Повышенная скорость обучения (lr=0.05)',
            'hidden_size': 8,
            'learning_rate': 0.05,
            'epochs': 2000
        },
        {
            'name': 'Пониженная скорость обучения (lr=0.005)',
            'hidden_size': 8,
            'learning_rate': 0.005,
            'epochs': 2000
        }
    ]
    
    # Запускаем эксперименты
    all_results = []
    for config in experiments:
        results = run_experiment(config, X, y)
        all_results.append(results)
    
    # Сохраняем результаты
    os.makedirs('experiments/results', exist_ok=True)
    output_file = f'experiments/results/hyperparameter_tuning_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*70}")
    print(f"✅ Все эксперименты завершены!")
    print(f"💾 Результаты сохранены в: {output_file}")
    
    # Сравнение результатов
    print(f"\n{'='*70}")
    print("📊 СРАВНЕНИЕ РЕЗУЛЬТАТОВ")
    print(f"{'='*70}")
    print(f"{'Эксперимент':<50} {'MAE':>8} {'RMSE':>8} {'Loss':>8}")
    print("-" * 70)
    
    for result in all_results:
        name = result['config']['name']
        mae = result['metrics']['mae']
        rmse = result['metrics']['rmse']
        loss = result['final_loss']
        print(f"{name:<50} {mae:>8.4f} {rmse:>8.4f} {loss:>8.4f}")
    
    # Находим лучший результат
    best_result = min(all_results, key=lambda x: x['metrics']['mae'])
    print(f"\n🏆 ЛУЧШИЙ РЕЗУЛЬТАТ: {best_result['config']['name']}")
    print(f"   MAE: {best_result['metrics']['mae']:.4f}")
    print(f"   Hidden size: {best_result['config']['hidden_size']}")
    print(f"   Learning rate: {best_result['config']['learning_rate']}")


if __name__ == '__main__':
    hyperparameter_tuning()

