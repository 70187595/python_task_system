"""
Эксперимент 10: Обучение модели с dropout 0.3
Цель: Уменьшить переобучение и улучшить обобщающую способность модели
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
    print("🧪 ЭКСПЕРИМЕНТ 10: Dropout 0.3")
    print("=" * 60)
    
    # Загружаем данные
    X, y, data_size = load_and_prepare_data()
    print(f"✅ Загружено {data_size} примеров")
    
    # Создаем сеть с dropout
    network = SimpleNeuralNetwork(
        input_size=10,
        hidden_size=8,
        output_size=3,
        activation='sigmoid',
        dropout_rate=0.3  # 30% нейронов будут "выключены" во время обучения
    )
    
    # Переинициализируем веса
    network.weights_input_hidden = np.random.randn(10, 8) * 0.1
    network.weights_hidden_output = np.random.randn(8, 3) * 0.1
    network.bias_hidden = np.zeros((1, 8))
    network.bias_output = np.zeros((1, 3))
    network.learning_rate = 0.01
    
    print(f"\n🔧 Параметры:")
    print(f"   Input: 10, Hidden: 8, Output: 3")
    print(f"   Learning rate: 0.01")
    print(f"   Epochs: 2000")
    print(f"   Activation: Sigmoid")
    print(f"   Dropout rate: 0.3 (30% нейронов отключаются)")
    
    print(f"\n📚 Что такое Dropout:")
    print(f"   Dropout - это техника регуляризации, которая случайным образом")
    print(f"   'выключает' нейроны во время обучения. Это помогает:")
    print(f"   • Предотвратить переобучение")
    print(f"   • Улучшить обобщающую способность")
    print(f"   • Заставить сеть учиться более устойчивым признакам")
    
    # Обучаем
    training_data = [(X[i:i+1], y[i:i+1]) for i in range(len(X))]
    print(f"\n🚀 Начинаем обучение...")
    
    history = network.train(training_data, epochs=2000)
    
    # Сохраняем модель
    os.makedirs('experiments/results', exist_ok=True)
    network.save_model('experiments/results/model_exp10_dropout.json')
    
    with open('experiments/results/history_exp10_dropout.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)
    
    # Результаты
    print(f"\n📊 Результаты:")
    print(f"   Начальная ошибка: {history['loss'][0]:.4f}")
    print(f"   Конечная ошибка: {history['loss'][-1]:.4f}")
    improvement = (1 - history['loss'][-1]/history['loss'][0])*100 if history['loss'][0] > 0 else 0
    print(f"   Улучшение: {improvement:.1f}%")
    
    # Тестирование на нескольких примерах (БЕЗ dropout)
    print(f"\n🧪 Тестирование на примерах (без dropout):")
    test_indices = [0, 50, 100, 150, 200]
    total_error = 0
    test_count = 0
    
    for idx in test_indices:
        if idx < len(X):
            # Важно: training=False, чтобы dropout не применялся во время инференса
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
    
    print(f"\n✅ Модель сохранена: experiments/results/model_exp10_dropout.json")
    print(f"✅ История сохранена: experiments/results/history_exp10_dropout.json")
    
    # Сравнение с предыдущими экспериментами
    print(f"\n📈 Сравнение с предыдущими экспериментами:")
    print(f"   Baseline (без dropout):            0.0056")
    print(f"   Эксперимент 5 (lr=0.05):           0.0038 🏆")
    print(f"   Эксперимент 8 (ReLU):              0.0047")
    print(f"   Эксперимент 9 (2 слоя):            0.0047")
    print(f"   Эксперимент 10 (dropout 0.3):      {history['loss'][-1]:.4f}")
    
    baseline_error = 0.0056
    if history['loss'][-1] < baseline_error:
        improvement_vs_baseline = ((baseline_error - history['loss'][-1])/baseline_error)*100
        print(f"   ✅ Dropout лучше baseline на {improvement_vs_baseline:.1f}%")
    elif history['loss'][-1] > baseline_error:
        degradation = ((history['loss'][-1] - baseline_error)/baseline_error)*100
        print(f"   ⚠️  Dropout хуже baseline на {degradation:.1f}%")
    else:
        print(f"   🔄 Результаты сопоставимы с baseline")
    
    print(f"\n💡 Выводы:")
    if history['loss'][-1] < 0.0045:
        print(f"   ✅ Dropout показал отличные результаты!")
        print(f"   ✅ Модель стала более устойчивой к переобучению")
    elif history['loss'][-1] < 0.0056:
        print(f"   ✅ Dropout помог стабилизировать обучение")
        print(f"   💡 Модель может лучше обобщаться на новых данных")
    else:
        print(f"   ⚠️  Dropout может быть слишком агрессивным для этой задачи")
        print(f"   💡 Возможно, стоит попробовать меньший dropout_rate (0.1-0.2)")
    
    # Дополнительная информация
    print(f"\n📖 Дополнительная информация:")
    print(f"   • Во время обучения: 30% нейронов случайно отключены")
    print(f"   • Во время тестирования: все нейроны активны")
    print(f"   • Используется 'inverted dropout' для корректного масштабирования")


if __name__ == '__main__':
    main()

