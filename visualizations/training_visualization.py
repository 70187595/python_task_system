"""
Визуализация процесса обучения нейронной сети

Скрипт создает следующие визуализации:
1. training_loss_baseline.png - график loss базовой модели по эпохам
2. training_loss_final.png - график loss финальной модели по эпохам
3. experiments_comparison.png - сравнение всех экспериментов
4. error_distribution.png - распределение ошибок предсказаний
5. network_architecture.png - архитектура нейронной сети

Автор: AI Assistant & Команда разработки
Дата: 2 декабря 2025
"""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
matplotlib.use('Agg')  # Для работы без GUI

# Настройка шрифтов для поддержки русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Путь к файлам
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'models')
EXPERIMENTS_DIR = os.path.join(PROJECT_DIR, 'experiments', 'results')
OUTPUT_DIR = SCRIPT_DIR


def load_json(file_path):
    """Загрузка JSON файла"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def plot_training_loss_baseline(output_path):
    """
    График loss базовой модели по эпохам
    """
    # Загрузка истории обучения baseline модели
    history_path = os.path.join(DATA_DIR, 'training_history.json')
    
    if not os.path.exists(history_path):
        print(f"⚠️  Файл не найден: {history_path}")
        return
    
    history = load_json(history_path)
    epochs = history['epochs']
    loss = history['loss']
    
    # Создание графика
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Основная линия loss
    ax.plot(epochs, loss, linewidth=2.5, color='#e74c3c', label='Training Loss', alpha=0.9)
    
    # Скользящее среднее для сглаживания
    window = 10
    if len(loss) >= window:
        moving_avg = np.convolve(loss, np.ones(window)/window, mode='valid')
        moving_epochs = epochs[window-1:]
        ax.plot(moving_epochs, moving_avg, linewidth=2, color='#3498db', 
                label=f'Скользящее среднее (окно={window})', linestyle='--', alpha=0.8)
    
    # Отметка финальной ошибки
    final_loss = loss[-1]
    ax.scatter([epochs[-1]], [final_loss], color='#2ecc71', s=150, zorder=5, 
               label=f'Финальная ошибка: {final_loss:.6f}')
    
    # Горизонтальная линия финальной ошибки
    ax.axhline(y=final_loss, color='#2ecc71', linestyle=':', alpha=0.5)
    
    # Аннотация начальной ошибки
    initial_loss = loss[0]
    improvement = (initial_loss - final_loss) / initial_loss * 100
    
    ax.annotate(f'Начало: {initial_loss:.4f}', 
                xy=(epochs[0], initial_loss), 
                xytext=(epochs[len(epochs)//4], initial_loss * 0.9),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    
    ax.annotate(f'Конец: {final_loss:.6f}\n(улучшение {improvement:.1f}%)', 
                xy=(epochs[-1], final_loss), 
                xytext=(epochs[-len(epochs)//3], final_loss * 1.5),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=1.5))
    
    # Настройка осей
    ax.set_xlabel('Эпоха', fontsize=12, fontweight='bold')
    ax.set_ylabel('Loss (MSE)', fontsize=12, fontweight='bold')
    ax.set_title('График обучения базовой модели (Baseline)\n' + 
                 f'Архитектура: 10→8→3 | LR: {history.get("learning_rate", 0.01)} | Эпохи: {len(epochs)}',
                 fontsize=14, fontweight='bold', pad=15)
    
    # Сетка
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)
    
    # Легенда
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    
    # Логарифмическая шкала для оси Y (опционально)
    if initial_loss / final_loss > 10:
        ax.set_yscale('log')
        ax.set_ylabel('Loss (MSE) - логарифмическая шкала', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def plot_training_loss_final(output_path):
    """
    График loss финальной модели по эпохам
    """
    # Загрузка истории обучения финальной модели
    history_path = os.path.join(DATA_DIR, 'training_history_final.json')
    
    if not os.path.exists(history_path):
        print(f"⚠️  Файл не найден: {history_path}")
        return
    
    history = load_json(history_path)
    epochs = history['epochs']
    loss = history['loss']
    
    # Создание графика с двумя подграфиками
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # График 1: Полная история обучения
    ax1.plot(epochs, loss, linewidth=2.5, color='#9b59b6', label='Training Loss', alpha=0.9)
    
    # Скользящее среднее
    window = 10
    if len(loss) >= window:
        moving_avg = np.convolve(loss, np.ones(window)/window, mode='valid')
        moving_epochs = epochs[window-1:]
        ax1.plot(moving_epochs, moving_avg, linewidth=2, color='#3498db', 
                label=f'Скользящее среднее (окно={window})', linestyle='--', alpha=0.8)
    
    final_loss = loss[-1]
    ax1.scatter([epochs[-1]], [final_loss], color='#2ecc71', s=150, zorder=5, 
               label=f'Финальная ошибка: {final_loss:.6f}')
    
    ax1.axhline(y=final_loss, color='#2ecc71', linestyle=':', alpha=0.5)
    
    # Аннотация
    initial_loss = loss[0]
    improvement = (initial_loss - final_loss) / initial_loss * 100
    
    ax1.annotate(f'Улучшение: {improvement:.1f}%', 
                xy=(epochs[-1], final_loss), 
                xytext=(epochs[-len(epochs)//3], final_loss * 1.8),
                fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=1.5))
    
    ax1.set_xlabel('Эпоха', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Loss (MSE)', fontsize=12, fontweight='bold')
    ax1.set_title('Полная история обучения', fontsize=12, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.legend(loc='upper right', fontsize=9)
    
    # Логарифмическая шкала если большой диапазон
    if initial_loss / final_loss > 10:
        ax1.set_yscale('log')
        ax1.set_ylabel('Loss (MSE) - лог. шкала', fontsize=12, fontweight='bold')
    
    # График 2: Последние эпохи (детальный вид)
    last_epochs = 100 if len(epochs) > 100 else len(epochs) // 2
    ax2.plot(epochs[-last_epochs:], loss[-last_epochs:], 
             linewidth=2.5, color='#e74c3c', alpha=0.9, label='Training Loss')
    
    # Тренд последних эпох
    if last_epochs > 10:
        z = np.polyfit(epochs[-last_epochs:], loss[-last_epochs:], 1)
        p = np.poly1d(z)
        ax2.plot(epochs[-last_epochs:], p(epochs[-last_epochs:]), 
                linestyle='--', color='orange', linewidth=2, label='Линейный тренд')
    
    ax2.scatter([epochs[-1]], [final_loss], color='#2ecc71', s=150, zorder=5)
    ax2.axhline(y=final_loss, color='#2ecc71', linestyle=':', alpha=0.5)
    
    ax2.set_xlabel('Эпоха', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Loss (MSE)', fontsize=12, fontweight='bold')
    ax2.set_title(f'Последние {last_epochs} эпох (детальный вид)', fontsize=12, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9)
    
    # Общий заголовок
    arch = history.get('architecture', {})
    arch_str = f"{arch.get('input_size', 10)}→{arch.get('hidden_size', 8)}→{arch.get('output_size', 3)}"
    
    fig.suptitle(f'График обучения финальной модели\n' + 
                 f'Архитектура: {arch_str} | LR: {history.get("learning_rate", 0.05)} | ' +
                 f'Финальная ошибка: {final_loss:.6f}',
                 fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def plot_experiments_comparison(output_path):
    """
    Сравнение всех экспериментов
    """
    # Список всех экспериментов
    experiments = [
        {'name': 'Baseline', 'file': 'training_history.json', 'dir': DATA_DIR, 'color': '#3498db'},
        {'name': 'Exp1: Hidden=4', 'file': 'history_exp1_hidden4.json', 'dir': EXPERIMENTS_DIR, 'color': '#e74c3c'},
        {'name': 'Exp2: Hidden=12', 'file': 'history_exp2_hidden12.json', 'dir': EXPERIMENTS_DIR, 'color': '#2ecc71'},
        {'name': 'Exp3: Hidden=16', 'file': 'history_exp3_hidden16.json', 'dir': EXPERIMENTS_DIR, 'color': '#f39c12'},
        {'name': 'Exp4: LR=0.001', 'file': 'history_exp4_lr0001.json', 'dir': EXPERIMENTS_DIR, 'color': '#9b59b6'},
        {'name': 'Exp5: LR=0.05', 'file': 'history_exp5_lr005.json', 'dir': EXPERIMENTS_DIR, 'color': '#1abc9c'},
        {'name': 'Exp6: 1000 эпох', 'file': 'history_exp6_epochs1000.json', 'dir': EXPERIMENTS_DIR, 'color': '#e67e22'},
        {'name': 'Exp7: 3000 эпох', 'file': 'history_exp7_epochs3000.json', 'dir': EXPERIMENTS_DIR, 'color': '#34495e'},
        {'name': 'Exp8: ReLU', 'file': 'history_exp8_relu.json', 'dir': EXPERIMENTS_DIR, 'color': '#c0392b'},
        {'name': 'Exp9: 2 слоя', 'file': 'history_exp9_two_layers.json', 'dir': EXPERIMENTS_DIR, 'color': '#16a085'},
        {'name': 'Exp10: Dropout', 'file': 'history_exp10_dropout.json', 'dir': EXPERIMENTS_DIR, 'color': '#d35400'},
    ]
    
    # Создание графика
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    final_errors = []
    exp_names = []
    
    # График 1: Loss по эпохам для всех экспериментов
    for exp in experiments:
        file_path = os.path.join(exp['dir'], exp['file'])
        
        if not os.path.exists(file_path):
            print(f"⚠️  Файл не найден: {file_path}")
            continue
        
        history = load_json(file_path)
        epochs = history['epochs']
        loss = history['loss']
        
        # Рисуем линию
        ax1.plot(epochs, loss, linewidth=2, label=exp['name'], 
                color=exp['color'], alpha=0.7)
        
        # Сохраняем финальную ошибку
        final_errors.append(loss[-1])
        exp_names.append(exp['name'])
    
    ax1.set_xlabel('Эпоха', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Loss (MSE)', fontsize=12, fontweight='bold')
    ax1.set_title('Сравнение loss всех экспериментов по эпохам', 
                  fontsize=13, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.legend(loc='upper right', fontsize=9, ncol=2)
    ax1.set_yscale('log')
    
    # График 2: Финальные ошибки
    sorted_indices = np.argsort(final_errors)
    sorted_names = [exp_names[i] for i in sorted_indices]
    sorted_errors = [final_errors[i] for i in sorted_indices]
    sorted_colors = [experiments[i]['color'] for i in sorted_indices]
    
    bars = ax2.barh(sorted_names, sorted_errors, color=sorted_colors, 
                    edgecolor='black', linewidth=0.8)
    
    # Добавление значений
    for i, (bar, error) in enumerate(zip(bars, sorted_errors)):
        width = bar.get_width()
        ax2.text(width + 0.0001, bar.get_y() + bar.get_height()/2,
                f'{error:.6f}', va='center', fontsize=9, fontweight='bold')
        
        # Отметка лучшего результата
        if i == 0:
            bar.set_edgecolor('#2ecc71')
            bar.set_linewidth(3)
            ax2.text(width/2, bar.get_y() + bar.get_height()/2,
                    '🏆 ЛУЧШИЙ', va='center', ha='center', 
                    fontsize=10, fontweight='bold', color='white')
    
    ax2.set_xlabel('Финальная ошибка (MSE)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Эксперимент', fontsize=12, fontweight='bold')
    ax2.set_title('Финальные ошибки экспериментов (отсортировано)', 
                  fontsize=13, fontweight='bold')
    ax2.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax2.set_axisbelow(True)
    
    # Общий заголовок
    fig.suptitle('Сравнение всех экспериментов\n(11 экспериментов на датасете из 210 примеров)',
                 fontsize=14, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def plot_error_distribution(output_path):
    """
    Распределение ошибок предсказаний
    """
    # Загрузка результатов тестирования
    test_results_path = os.path.join(EXPERIMENTS_DIR, 'test_results.json')
    
    if not os.path.exists(test_results_path):
        print(f"⚠️  Файл не найден: {test_results_path}")
        print("ℹ️  Создаю упрощенную визуализацию на основе доступных данных...")
        plot_error_distribution_alternative(output_path)
        return
    
    results = load_json(test_results_path)
    
    # Извлечение ошибок по каждому выходу
    errors_correctness = []
    errors_efficiency = []
    errors_readability = []
    
    for test in results.get('tests', []):
        pred = test.get('predicted', [0, 0, 0])
        actual = test.get('actual', [0, 0, 0])
        
        errors_correctness.append(abs(pred[0] - actual[0]))
        errors_efficiency.append(abs(pred[1] - actual[1]))
        errors_readability.append(abs(pred[2] - actual[2]))
    
    # Создание графика
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # График 1: Гистограмма ошибок correctness
    ax1 = axes[0, 0]
    ax1.hist(errors_correctness, bins=20, color='#3498db', edgecolor='black', alpha=0.7)
    ax1.axvline(x=np.mean(errors_correctness), color='red', linestyle='--', 
                linewidth=2, label=f'Среднее: {np.mean(errors_correctness):.4f}')
    ax1.set_title('Распределение ошибок: Correctness', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Абсолютная ошибка')
    ax1.set_ylabel('Частота')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # График 2: Гистограмма ошибок efficiency
    ax2 = axes[0, 1]
    ax2.hist(errors_efficiency, bins=20, color='#2ecc71', edgecolor='black', alpha=0.7)
    ax2.axvline(x=np.mean(errors_efficiency), color='red', linestyle='--', 
                linewidth=2, label=f'Среднее: {np.mean(errors_efficiency):.4f}')
    ax2.set_title('Распределение ошибок: Efficiency', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Абсолютная ошибка')
    ax2.set_ylabel('Частота')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # График 3: Гистограмма ошибок readability
    ax3 = axes[1, 0]
    ax3.hist(errors_readability, bins=20, color='#9b59b6', edgecolor='black', alpha=0.7)
    ax3.axvline(x=np.mean(errors_readability), color='red', linestyle='--', 
                linewidth=2, label=f'Среднее: {np.mean(errors_readability):.4f}')
    ax3.set_title('Распределение ошибок: Readability', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Абсолютная ошибка')
    ax3.set_ylabel('Частота')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # График 4: Сравнение средних ошибок
    ax4 = axes[1, 1]
    means = [np.mean(errors_correctness), np.mean(errors_efficiency), np.mean(errors_readability)]
    labels = ['Correctness', 'Efficiency', 'Readability']
    colors = ['#3498db', '#2ecc71', '#9b59b6']
    
    bars = ax4.bar(labels, means, color=colors, edgecolor='black', alpha=0.7)
    
    # Добавление значений на столбцы
    for bar, mean in zip(bars, means):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2, height,
                f'{mean:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax4.set_title('Средние абсолютные ошибки', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Средняя ошибка')
    ax4.grid(True, alpha=0.3, axis='y')
    
    # Общий заголовок
    total_tests = len(errors_correctness)
    overall_mse = np.mean([np.mean(errors_correctness)**2, 
                           np.mean(errors_efficiency)**2, 
                           np.mean(errors_readability)**2])
    
    fig.suptitle(f'Распределение ошибок предсказаний на тестовой выборке\n' + 
                 f'(всего тестов: {total_tests}, общая MSE: {overall_mse:.6f})',
                 fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def plot_error_distribution_alternative(output_path):
    """
    Альтернативная визуализация ошибок (если нет test_results.json)
    """
    # Используем данные из истории обучения для демонстрации
    history_path = os.path.join(DATA_DIR, 'training_history_final.json')
    
    if not os.path.exists(history_path):
        history_path = os.path.join(DATA_DIR, 'training_history.json')
    
    if not os.path.exists(history_path):
        print(f"❌ Не удалось создать график распределения ошибок")
        return
    
    history = load_json(history_path)
    loss = history['loss']
    
    # Создание графика
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # График 1: Распределение loss по эпохам
    ax1 = axes[0, 0]
    ax1.hist(loss, bins=30, color='#3498db', edgecolor='black', alpha=0.7)
    ax1.axvline(x=np.mean(loss), color='red', linestyle='--', 
                linewidth=2, label=f'Среднее: {np.mean(loss):.6f}')
    ax1.axvline(x=np.median(loss), color='green', linestyle='--', 
                linewidth=2, label=f'Медиана: {np.median(loss):.6f}')
    ax1.set_title('Распределение Loss по эпохам', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Loss (MSE)')
    ax1.set_ylabel('Частота')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # График 2: Box plot loss
    ax2 = axes[0, 1]
    bp = ax2.boxplot([loss], tick_labels=['Training Loss'], patch_artist=True)
    bp['boxes'][0].set_facecolor('#2ecc71')
    bp['boxes'][0].set_alpha(0.7)
    ax2.set_title('Box Plot: Распределение Loss', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Loss (MSE)')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # График 3: Улучшение по эпохам
    ax3 = axes[1, 0]
    improvements = [loss[0] - l for l in loss]
    ax3.plot(history['epochs'], improvements, linewidth=2, color='#9b59b6')
    ax3.fill_between(history['epochs'], 0, improvements, alpha=0.3, color='#9b59b6')
    ax3.set_title('Улучшение Loss относительно начала', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Эпоха')
    ax3.set_ylabel('Улучшение (начальный loss - текущий loss)')
    ax3.grid(True, alpha=0.3)
    
    # График 4: Статистика
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    stats_text = f"""
    📊 СТАТИСТИКА ОБУЧЕНИЯ
    
    Начальный Loss:    {loss[0]:.6f}
    Финальный Loss:    {loss[-1]:.6f}
    Улучшение:         {(loss[0]-loss[-1])/loss[0]*100:.1f}%
    
    Средний Loss:      {np.mean(loss):.6f}
    Медиана Loss:      {np.median(loss):.6f}
    Стд. отклонение:   {np.std(loss):.6f}
    
    Минимальный Loss:  {np.min(loss):.6f}
    Максимальный Loss: {np.max(loss):.6f}
    
    Всего эпох:        {len(loss)}
    """
    
    ax4.text(0.1, 0.5, stats_text, fontsize=11, family='monospace',
             verticalalignment='center', bbox=dict(boxstyle='round', 
             facecolor='wheat', alpha=0.3))
    
    # Общий заголовок
    fig.suptitle('Анализ ошибок и статистика обучения',
                 fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def plot_network_architecture(output_path):
    """
    Диаграмма архитектуры нейронной сети
    """
    # Параметры архитектуры
    input_size = 10
    hidden_size = 8
    output_size = 3
    
    # Создание графика
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Параметры для рисования
    layer_x = [2, 5, 8]  # X-координаты слоев
    neuron_radius = 0.2
    
    # Цвета слоев
    colors = ['#3498db', '#2ecc71', '#e74c3c']
    
    # Размеры слоев
    layer_sizes = [input_size, hidden_size, output_size]
    layer_names = ['Входной слой\n(10 признаков)', 
                   'Скрытый слой\n(8 нейронов)', 
                   'Выходной слой\n(3 выхода)']
    
    # Названия входных признаков
    input_labels = [
        'LOC', 'Func', 'Complexity', 'Nesting', 'VarLen',
        'Comments', 'Imports', 'Classes', 'ErrHandle', 'TestCov'
    ]
    
    # Названия выходов
    output_labels = ['Correctness', 'Efficiency', 'Readability']
    
    # Рисование связей между слоями
    for layer_idx in range(len(layer_sizes) - 1):
        from_size = layer_sizes[layer_idx]
        to_size = layer_sizes[layer_idx + 1]
        
        from_x = layer_x[layer_idx]
        to_x = layer_x[layer_idx + 1]
        
        # Вертикальное распределение нейронов
        from_y_start = 6 - from_size * 0.5
        to_y_start = 6 - to_size * 0.5
        
        # Рисуем только несколько связей для наглядности
        for i in range(min(from_size, 5)):
            from_y = from_y_start + i * 1.0 if from_size <= 10 else from_y_start + i * (10.0 / from_size)
            
            for j in range(min(to_size, 5)):
                to_y = to_y_start + j * 1.0 if to_size <= 10 else to_y_start + j * (10.0 / to_size)
                
                # Рисуем линию с прозрачностью
                ax.plot([from_x + neuron_radius, to_x - neuron_radius], 
                       [from_y, to_y], 
                       color='gray', alpha=0.1, linewidth=0.5, zorder=1)
    
    # Рисование нейронов
    neuron_positions = []
    
    for layer_idx, size in enumerate(layer_sizes):
        x = layer_x[layer_idx]
        color = colors[layer_idx]
        
        # Вертикальное распределение
        y_start = 6 - size * 0.5
        positions = []
        
        for i in range(size):
            y = y_start + i * 1.0 if size <= 10 else y_start + i * (10.0 / size)
            
            # Рисуем нейрон
            circle = patches.Circle((x, y), neuron_radius, 
                                   facecolor=color, edgecolor='black', 
                                   linewidth=2, zorder=3, alpha=0.8)
            ax.add_patch(circle)
            positions.append((x, y))
            
            # Добавляем подписи для входных и выходных нейронов
            if layer_idx == 0 and i < len(input_labels):
                ax.text(x - 0.8, y, input_labels[i], 
                       fontsize=9, ha='right', va='center', fontweight='bold')
            elif layer_idx == 2 and i < len(output_labels):
                ax.text(x + 0.8, y, output_labels[i], 
                       fontsize=10, ha='left', va='center', fontweight='bold')
        
        neuron_positions.append(positions)
        
        # Подпись слоя
        ax.text(x, 11, layer_names[layer_idx], 
               fontsize=12, ha='center', va='center', 
               fontweight='bold', 
               bbox=dict(boxstyle='round,pad=0.5', 
                        facecolor=color, alpha=0.3, edgecolor='black'))
    
    # Добавление информации об активациях
    ax.text(3.5, 0.5, 'Sigmoid\nActivation', 
           fontsize=10, ha='center', style='italic',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    ax.text(6.5, 0.5, 'Sigmoid\nActivation', 
           fontsize=10, ha='center', style='italic',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
    
    # Заголовок
    ax.text(5, 11.5, 'Архитектура нейронной сети для оценки качества кода', 
           fontsize=14, ha='center', fontweight='bold')
    
    # Информационная панель
    info_text = (
        f"Параметры модели:\n"
        f"• Входной слой: {input_size} признаков\n"
        f"• Скрытый слой: {hidden_size} нейронов\n"
        f"• Выходной слой: {output_size} выхода\n"
        f"• Всего весов: {input_size * hidden_size + hidden_size * output_size} = "
        f"{input_size * hidden_size + hidden_size * output_size}\n"
        f"• Всего bias: {hidden_size + output_size}\n"
        f"• Общее кол-во параметров: "
        f"{input_size * hidden_size + hidden_size * output_size + hidden_size + output_size}"
    )
    
    ax.text(5, -0.5, info_text, 
           fontsize=9, ha='center', va='top',
           bbox=dict(boxstyle='round,pad=0.8', 
                    facecolor='wheat', alpha=0.5, edgecolor='black'))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def main():
    """Главная функция"""
    print("="*60)
    print("🎨 ВИЗУАЛИЗАЦИЯ ПРОЦЕССА ОБУЧЕНИЯ")
    print("="*60)
    
    print("\n🎨 Создание визуализаций...\n")
    
    # 1. График loss базовой модели
    print("1️⃣  Создание графика loss базовой модели...")
    plot_training_loss_baseline(
        os.path.join(OUTPUT_DIR, 'training_loss_baseline.png')
    )
    
    # 2. График loss финальной модели
    print("\n2️⃣  Создание графика loss финальной модели...")
    plot_training_loss_final(
        os.path.join(OUTPUT_DIR, 'training_loss_final.png')
    )
    
    # 3. Сравнение экспериментов
    print("\n3️⃣  Создание графика сравнения экспериментов...")
    plot_experiments_comparison(
        os.path.join(OUTPUT_DIR, 'experiments_comparison.png')
    )
    
    # 4. Распределение ошибок
    print("\n4️⃣  Создание графика распределения ошибок...")
    plot_error_distribution(
        os.path.join(OUTPUT_DIR, 'error_distribution.png')
    )
    
    # 5. Архитектура сети
    print("\n5️⃣  Создание диаграммы архитектуры...")
    plot_network_architecture(
        os.path.join(OUTPUT_DIR, 'network_architecture.png')
    )
    
    print("\n" + "="*60)
    print("✅ Все визуализации процесса обучения созданы успешно!")
    print(f"📁 Сохранены в: {OUTPUT_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()

