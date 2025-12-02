"""
Тестирование финальной модели на тестовой выборке

Скрипт:
1. Разделяет датасет на обучающую (80%) и тестовую (20%) выборки
2. Тестирует финальную модель на тестовых данных
3. Вычисляет метрики: MAE, MSE, RMSE, точность по каждой метрике
4. Сохраняет результаты тестирования
"""

import sys
import os
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.neural_network import SimpleNeuralNetwork


def load_data():
    """Загрузка данных"""
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
    
    return np.array(X), np.array(y)


def split_data(X, y, test_ratio=0.2, seed=42):
    """Разделение данных на обучающую и тестовую выборки"""
    np.random.seed(seed)
    indices = np.random.permutation(len(X))
    test_size = int(len(X) * test_ratio)
    
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    
    return (X[train_indices], y[train_indices], 
            X[test_indices], y[test_indices])


def calculate_metrics(y_true, y_pred):
    """Вычисление метрик качества"""
    # MAE - Mean Absolute Error
    mae = np.mean(np.abs(y_true - y_pred))
    
    # MSE - Mean Squared Error
    mse = np.mean(np.square(y_true - y_pred))
    
    # RMSE - Root Mean Squared Error
    rmse = np.sqrt(mse)
    
    # R² - коэффициент детерминации
    ss_res = np.sum(np.square(y_true - y_pred))
    ss_tot = np.sum(np.square(y_true - np.mean(y_true)))
    r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    return {
        'mae': float(mae),
        'mse': float(mse),
        'rmse': float(rmse),
        'r2': float(r2)
    }


def main():
    print("=" * 70)
    print("🧪 ТЕСТИРОВАНИЕ ФИНАЛЬНОЙ МОДЕЛИ")
    print("=" * 70)
    
    # Загружаем данные
    print("\n📊 Загрузка данных...")
    X, y = load_data()
    print(f"   Всего примеров: {len(X)}")
    
    # Разделяем на обучающую и тестовую выборки
    print("\n📂 Разделение данных...")
    X_train, y_train, X_test, y_test = split_data(X, y, test_ratio=0.2)
    print(f"   Обучающая выборка: {len(X_train)} примеров (80%)")
    print(f"   Тестовая выборка:  {len(X_test)} примеров (20%)")
    
    # Загружаем финальную модель
    print("\n🧠 Загрузка финальной модели...")
    network = SimpleNeuralNetwork()
    
    # Тестирование на тестовой выборке
    print("\n🧪 Тестирование на тестовой выборке...")
    print("-" * 50)
    
    predictions = []
    targets = []
    errors = []
    
    for i, (x, y_true) in enumerate(zip(X_test, y_test)):
        y_pred = network.predict(x).flatten()
        predictions.append(y_pred)
        targets.append(y_true)
        
        error = np.mean(np.abs(y_true - y_pred))
        errors.append(error)
    
    predictions = np.array(predictions)
    targets = np.array(targets)
    
    # Общие метрики
    print("\n📊 ОБЩИЕ МЕТРИКИ")
    print("=" * 50)
    
    overall_metrics = calculate_metrics(targets, predictions)
    
    print(f"\n   MAE  (Mean Absolute Error):    {overall_metrics['mae']:.4f}")
    print(f"   MSE  (Mean Squared Error):     {overall_metrics['mse']:.6f}")
    print(f"   RMSE (Root MSE):               {overall_metrics['rmse']:.4f}")
    print(f"   R²   (Коэффициент детерминации): {overall_metrics['r2']:.4f}")
    
    accuracy = (1 - overall_metrics['mae']) * 100
    print(f"\n   🎯 Общая точность:              ~{accuracy:.1f}%")
    
    # Метрики по каждому выходу
    print("\n📊 МЕТРИКИ ПО КАЖДОЙ МЕТРИКЕ КАЧЕСТВА")
    print("=" * 50)
    
    metric_names = ['Correctness (Правильность)', 
                    'Efficiency (Эффективность)', 
                    'Readability (Читаемость)']
    
    per_metric_results = {}
    
    for j, name in enumerate(metric_names):
        y_true_j = targets[:, j]
        y_pred_j = predictions[:, j]
        
        metrics = calculate_metrics(y_true_j, y_pred_j)
        per_metric_results[name] = metrics
        
        acc = (1 - metrics['mae']) * 100
        
        print(f"\n   {name}:")
        print(f"      MAE:  {metrics['mae']:.4f}")
        print(f"      RMSE: {metrics['rmse']:.4f}")
        print(f"      R²:   {metrics['r2']:.4f}")
        print(f"      Точность: ~{acc:.1f}%")
    
    # Распределение ошибок
    print("\n📊 РАСПРЕДЕЛЕНИЕ ОШИБОК")
    print("=" * 50)
    
    errors = np.array(errors)
    
    excellent = np.sum(errors < 0.05)
    good = np.sum((errors >= 0.05) & (errors < 0.10))
    acceptable = np.sum((errors >= 0.10) & (errors < 0.15))
    poor = np.sum(errors >= 0.15)
    
    print(f"\n   ✅ Отличные (ошибка < 0.05):     {excellent:2d} ({excellent/len(errors)*100:.1f}%)")
    print(f"   ✅ Хорошие (0.05 - 0.10):        {good:2d} ({good/len(errors)*100:.1f}%)")
    print(f"   ⚠️  Приемлемые (0.10 - 0.15):    {acceptable:2d} ({acceptable/len(errors)*100:.1f}%)")
    print(f"   ❌ Плохие (> 0.15):              {poor:2d} ({poor/len(errors)*100:.1f}%)")
    
    print(f"\n   Минимальная ошибка: {np.min(errors):.4f}")
    print(f"   Максимальная ошибка: {np.max(errors):.4f}")
    print(f"   Медианная ошибка:   {np.median(errors):.4f}")
    print(f"   Стандартное откл.:  {np.std(errors):.4f}")
    
    # Примеры предсказаний
    print("\n🔍 ПРИМЕРЫ ПРЕДСКАЗАНИЙ")
    print("=" * 50)
    
    # Лучшие предсказания
    best_indices = np.argsort(errors)[:3]
    print("\n   ✅ Лучшие предсказания:")
    for idx in best_indices:
        print(f"\n      Пример {idx}:")
        print(f"      Ожидаемое:    [{targets[idx][0]:.2f}, {targets[idx][1]:.2f}, {targets[idx][2]:.2f}]")
        print(f"      Предсказание: [{predictions[idx][0]:.2f}, {predictions[idx][1]:.2f}, {predictions[idx][2]:.2f}]")
        print(f"      Ошибка:       {errors[idx]:.4f}")
    
    # Худшие предсказания
    worst_indices = np.argsort(errors)[-3:][::-1]
    print("\n   ❌ Худшие предсказания:")
    for idx in worst_indices:
        print(f"\n      Пример {idx}:")
        print(f"      Ожидаемое:    [{targets[idx][0]:.2f}, {targets[idx][1]:.2f}, {targets[idx][2]:.2f}]")
        print(f"      Предсказание: [{predictions[idx][0]:.2f}, {predictions[idx][1]:.2f}, {predictions[idx][2]:.2f}]")
        print(f"      Ошибка:       {errors[idx]:.4f}")
    
    # Сохранение результатов
    print("\n💾 Сохранение результатов...")
    
    test_results = {
        'test_size': len(X_test),
        'train_size': len(X_train),
        'overall_metrics': overall_metrics,
        'per_metric_results': {
            'correctness': per_metric_results[metric_names[0]],
            'efficiency': per_metric_results[metric_names[1]],
            'readability': per_metric_results[metric_names[2]]
        },
        'error_distribution': {
            'excellent': int(excellent),
            'good': int(good),
            'acceptable': int(acceptable),
            'poor': int(poor)
        },
        'error_stats': {
            'min': float(np.min(errors)),
            'max': float(np.max(errors)),
            'median': float(np.median(errors)),
            'std': float(np.std(errors)),
            'mean': float(np.mean(errors))
        },
        'accuracy_percent': float(accuracy)
    }
    
    os.makedirs('experiments/results', exist_ok=True)
    with open('experiments/results/test_results.json', 'w', encoding='utf-8') as f:
        json.dump(test_results, f, indent=2, ensure_ascii=False)
    
    print("   ✅ Сохранено: experiments/results/test_results.json")
    
    print("\n" + "=" * 70)
    print("🎉 ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!")
    print("=" * 70)
    
    print(f"\n📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
    print(f"   • Тестовая выборка: {len(X_test)} примеров")
    print(f"   • Общая точность:   ~{accuracy:.1f}%")
    print(f"   • MAE:              {overall_metrics['mae']:.4f}")
    print(f"   • R²:               {overall_metrics['r2']:.4f}")
    print(f"   • Отличных результатов: {excellent} ({excellent/len(errors)*100:.1f}%)")
    
    if accuracy >= 90:
        print(f"\n   ✅ Модель показывает ОТЛИЧНЫЕ результаты!")
    elif accuracy >= 85:
        print(f"\n   ✅ Модель показывает ХОРОШИЕ результаты!")
    else:
        print(f"\n   ⚠️  Модель требует дополнительного обучения")


if __name__ == '__main__':
    main()

