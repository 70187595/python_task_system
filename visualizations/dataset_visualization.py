"""
Визуализация датасета для анализа качества кода

Скрипт создает следующие визуализации:
1. dataset_distribution.png - распределение примеров по категориям
2. quality_distribution.png - распределение по уровням качества
3. features_correlation.png - тепловая карта корреляции признаков

Автор: AI Assistant & Команда разработки
Дата: 2 декабря 2025
"""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Для работы без GUI

# Настройка шрифтов для поддержки русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Путь к файлам
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, 'data', 'training_data', 'training_data.json')
OUTPUT_DIR = SCRIPT_DIR


def load_dataset():
    """
    Загрузка датасета из JSON файла
    
    Читает training_data.json, содержащий примеры кода Python
    с извлеченными признаками и целевыми значениями качества.
    
    Returns:
        list: Список словарей с полями 'code', 'features', 'target'
    """
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def classify_by_category(code):
    """
    Классификация примера кода по категории на основе содержимого
    
    Анализирует код и определяет его категорию по наличию
    ключевых слов и конструкций:
    - ООП (классы): наличие 'class' или магических методов
    - Сортировка: ключевые слова sort, bubble, quick, merge
    - Списки: работа с индексами, append, pop
    - Циклы: for, while
    - Условия: if, else
    - Функции: def (базовые функции)
    
    Args:
        code: Строка с исходным кодом Python
        
    Returns:
        str: Название категории
    """
    code_lower = code.lower()
    
    # Определяем категорию по ключевым словам в коде
    if 'class ' in code_lower:
        return 'ООП (классы)'
    elif 'def __' in code_lower:
        return 'ООП (классы)'
    elif any(word in code_lower for word in ['sort', 'сортир', 'bubble', 'quick', 'merge']):
        return 'Сортировка'
    elif any(word in code_lower for word in ['search', 'find', 'поиск', 'binary_search']):
        return 'Поиск'
    elif any(word in code_lower for word in ['fibonacci', 'factorial', 'recursive', 'рекурс']):
        return 'Рекурсия'
    elif 'dict' in code_lower or '{}' in code or any(word in code_lower for word in ['словар', 'dictionary', 'merge_dict', 'invert_dict']):
        return 'Словари'
    elif any(word in code_lower for word in ['list', 'array', 'спис', 'filter', 'map', 'reduce', 'flatten']):
        return 'Списки'
    elif any(word in code_lower for word in ['string', 'text', 'строк', 'str.', 'split', 'join', 'replace', 'capitalize', 'reverse_string']):
        return 'Строки'
    elif any(word in code_lower for word in ['for ', 'while ', 'цикл', 'iterate', 'loop']):
        return 'Циклы'
    elif any(word in code_lower for word in ['if ', 'else', 'условие', 'condition']):
        return 'Условия'
    elif any(word in code_lower for word in ['math', 'sqrt', 'pow', 'sin', 'cos', 'sum', 'avg', 'mean', 'prime', 'gcd', 'lcm']):
        return 'Математика'
    elif any(word in code_lower for word in ['file', 'open', 'read', 'write', 'файл']):
        return 'Файлы'
    else:
        return 'Другое'


def classify_quality(target):
    """
    Классификация качества кода по средней оценке
    
    target: [correctness, efficiency, readability]
    """
    avg_score = sum(target) / len(target)
    
    if avg_score >= 0.85:
        return 'Отличное'
    elif avg_score >= 0.65:
        return 'Хорошее'
    elif avg_score >= 0.45:
        return 'Среднее'
    else:
        return 'Плохое'


def plot_category_distribution(data, output_path):
    """
    Создание графика распределения по категориям
    """
    # Классификация по категориям
    categories = {}
    for item in data:
        category = classify_by_category(item['code'])
        categories[category] = categories.get(category, 0) + 1
    
    # Сортировка по количеству
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    names = [x[0] for x in sorted_categories]
    values = [x[1] for x in sorted_categories]
    
    # Создание графика
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Цветовая палитра
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(names)))
    
    bars = ax.barh(names, values, color=colors, edgecolor='black', linewidth=0.5)
    
    # Добавление значений на столбцы
    for bar, value in zip(bars, values):
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                f'{value} ({value/len(data)*100:.1f}%)',
                va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Количество примеров', fontsize=12)
    ax.set_ylabel('Категория', fontsize=12)
    ax.set_title(f'Распределение датасета по категориям\n(всего {len(data)} примеров)', 
                 fontsize=14, fontweight='bold')
    
    # Сетка
    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")
    return categories


def plot_quality_distribution(data, output_path):
    """
    Создание графика распределения по качеству кода
    """
    # Классификация по качеству
    quality_counts = {
        'Отличное': 0,
        'Хорошее': 0,
        'Среднее': 0,
        'Плохое': 0
    }
    
    for item in data:
        quality = classify_quality(item['target'])
        quality_counts[quality] += 1
    
    # Данные для графика
    labels = list(quality_counts.keys())
    sizes = list(quality_counts.values())
    
    # Цвета для категорий качества
    colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c']
    explode = (0.05, 0.02, 0.02, 0.05)
    
    # Создание графика
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Круговая диаграмма
    wedges, texts, autotexts = ax1.pie(
        sizes, 
        explode=explode,
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90,
        textprops={'fontsize': 11}
    )
    
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    
    ax1.set_title('Распределение по качеству\n(круговая диаграмма)', 
                  fontsize=12, fontweight='bold')
    
    # Столбчатая диаграмма
    bars = ax2.bar(labels, sizes, color=colors, edgecolor='black', linewidth=1)
    
    # Добавление значений на столбцы
    for bar, value in zip(bars, sizes):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{value}', ha='center', fontsize=12, fontweight='bold')
    
    ax2.set_xlabel('Уровень качества', fontsize=12)
    ax2.set_ylabel('Количество примеров', fontsize=12)
    ax2.set_title('Распределение по качеству\n(столбчатая диаграмма)', 
                  fontsize=12, fontweight='bold')
    ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax2.set_axisbelow(True)
    
    # Легенда с описанием
    legend_text = [
        'Отличное: 0.85 - 1.0',
        'Хорошее: 0.65 - 0.85', 
        'Среднее: 0.45 - 0.65',
        'Плохое: 0.0 - 0.45'
    ]
    
    fig.text(0.5, 0.02, 
             'Качество определяется как среднее от [correctness, efficiency, readability]',
             ha='center', fontsize=10, style='italic')
    
    plt.suptitle(f'Распределение датасета по уровням качества кода\n(всего {len(data)} примеров)', 
                 fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")
    return quality_counts


def plot_features_correlation(data, output_path):
    """
    Создание тепловой карты корреляции признаков
    """
    # Извлечение признаков в матрицу
    feature_names = [
        'lines_of_code',
        'functions_count', 
        'complexity',
        'nested_levels',
        'variable_names_length',
        'comments_ratio',
        'imports_count',
        'class_count',
        'error_handling',
        'test_coverage'
    ]
    
    # Короткие названия для графика
    short_names = [
        'LOC',           # lines_of_code
        'Functions',     # functions_count
        'Complexity',    # complexity
        'Nesting',       # nested_levels
        'Var Names',     # variable_names_length
        'Comments',      # comments_ratio
        'Imports',       # imports_count
        'Classes',       # class_count
        'Err Handle',    # error_handling
        'Test Cov'       # test_coverage
    ]
    
    # Добавляем целевые переменные
    target_names = ['correctness', 'efficiency', 'readability']
    all_names = short_names + ['Correct', 'Effic', 'Read']
    
    # Создание матрицы данных
    n_samples = len(data)
    n_features = len(feature_names) + 3  # +3 для target
    
    matrix = np.zeros((n_samples, n_features))
    
    for i, item in enumerate(data):
        for j, fname in enumerate(feature_names):
            matrix[i, j] = item['features'].get(fname, 0)
        
        # Добавляем target
        for j, tval in enumerate(item['target']):
            matrix[i, len(feature_names) + j] = tval
    
    # Вычисление корреляционной матрицы
    # Подавляем предупреждения о делении на ноль для признаков с нулевым std
    with np.errstate(divide='ignore', invalid='ignore'):
        correlation_matrix = np.corrcoef(matrix.T)
        # Заменяем NaN на 0 для признаков с нулевой дисперсией
        correlation_matrix = np.nan_to_num(correlation_matrix, nan=0.0)
    
    # Создание графика
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Тепловая карта
    im = ax.imshow(correlation_matrix, cmap='RdYlBu_r', aspect='auto', vmin=-1, vmax=1)
    
    # Добавление цветовой шкалы
    cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
    cbar.ax.set_ylabel('Коэффициент корреляции', rotation=-90, va="bottom", fontsize=11)
    
    # Настройка осей
    ax.set_xticks(np.arange(len(all_names)))
    ax.set_yticks(np.arange(len(all_names)))
    ax.set_xticklabels(all_names, fontsize=10)
    ax.set_yticklabels(all_names, fontsize=10)
    
    # Поворот подписей
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Добавление значений в ячейки
    for i in range(len(all_names)):
        for j in range(len(all_names)):
            value = correlation_matrix[i, j]
            color = 'white' if abs(value) > 0.5 else 'black'
            text = ax.text(j, i, f'{value:.2f}',
                          ha="center", va="center", color=color, fontsize=8)
    
    # Разделительные линии для target
    ax.axhline(y=9.5, color='black', linewidth=2)
    ax.axvline(x=9.5, color='black', linewidth=2)
    
    ax.set_title('Корреляционная матрица признаков и целевых переменных\n' + 
                 f'(датасет: {len(data)} примеров)',
                 fontsize=14, fontweight='bold', pad=20)
    
    # Аннотации
    ax.annotate('Признаки', xy=(4.5, -1.5), fontsize=11, fontweight='bold', ha='center')
    ax.annotate('Target', xy=(11.5, -1.5), fontsize=11, fontweight='bold', ha='center')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")
    return correlation_matrix


def plot_features_statistics(data, output_path):
    """
    Создание графика статистики признаков (дополнительная визуализация)
    """
    feature_names = [
        'lines_of_code',
        'functions_count', 
        'complexity',
        'nested_levels',
        'variable_names_length',
        'comments_ratio',
        'imports_count',
        'class_count',
        'error_handling',
        'test_coverage'
    ]
    
    short_names = [
        'LOC', 'Func', 'Compl', 'Nest', 'VarLen',
        'Comm', 'Import', 'Class', 'ErrH', 'Test'
    ]
    
    # Сбор статистики по каждому признаку
    stats = {name: [] for name in feature_names}
    
    for item in data:
        for name in feature_names:
            stats[name].append(item['features'].get(name, 0))
    
    # Вычисление статистик
    means = [np.mean(stats[name]) for name in feature_names]
    stds = [np.std(stats[name]) for name in feature_names]
    mins = [np.min(stats[name]) for name in feature_names]
    maxs = [np.max(stats[name]) for name in feature_names]
    
    # Создание графика
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Средние значения
    ax1 = axes[0, 0]
    bars = ax1.bar(short_names, means, color='steelblue', edgecolor='black')
    ax1.errorbar(short_names, means, yerr=stds, fmt='none', color='red', capsize=3)
    ax1.set_title('Средние значения признаков (±std)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Значение')
    ax1.tick_params(axis='x', rotation=45)
    ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    # 2. Диапазон значений (min-max)
    ax2 = axes[0, 1]
    x = np.arange(len(short_names))
    width = 0.35
    ax2.bar(x - width/2, mins, width, label='Min', color='#3498db', edgecolor='black')
    ax2.bar(x + width/2, maxs, width, label='Max', color='#e74c3c', edgecolor='black')
    ax2.set_xticks(x)
    ax2.set_xticklabels(short_names, rotation=45)
    ax2.set_title('Диапазон значений признаков', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Значение')
    ax2.legend()
    ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    # 3. Распределение целевых переменных
    ax3 = axes[1, 0]
    target_stats = {'correctness': [], 'efficiency': [], 'readability': []}
    for item in data:
        for i, name in enumerate(['correctness', 'efficiency', 'readability']):
            target_stats[name].append(item['target'][i])
    
    bp = ax3.boxplot([target_stats['correctness'], target_stats['efficiency'], target_stats['readability']],
                      tick_labels=['Correctness', 'Efficiency', 'Readability'],
                      patch_artist=True)
    
    colors_box = ['#2ecc71', '#3498db', '#9b59b6']
    for patch, color in zip(bp['boxes'], colors_box):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax3.set_title('Распределение целевых переменных', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Значение')
    ax3.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    # 4. Гистограмма средней оценки качества
    ax4 = axes[1, 1]
    avg_qualities = [(item['target'][0] + item['target'][1] + item['target'][2]) / 3 for item in data]
    
    ax4.hist(avg_qualities, bins=20, color='#9b59b6', edgecolor='black', alpha=0.7)
    ax4.axvline(x=0.85, color='green', linestyle='--', label='Отличное (0.85)')
    ax4.axvline(x=0.65, color='blue', linestyle='--', label='Хорошее (0.65)')
    ax4.axvline(x=0.45, color='orange', linestyle='--', label='Среднее (0.45)')
    ax4.set_title('Распределение средней оценки качества', fontsize=11, fontweight='bold')
    ax4.set_xlabel('Средняя оценка')
    ax4.set_ylabel('Количество примеров')
    ax4.legend(fontsize=8)
    ax4.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    plt.suptitle(f'Статистика датасета ({len(data)} примеров)', 
                 fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Сохранено: {output_path}")


def print_dataset_summary(data, categories, quality_counts):
    """Вывод сводки о датасете"""
    print("\n" + "="*60)
    print("📊 СВОДКА ПО ДАТАСЕТУ")
    print("="*60)
    
    print(f"\n📁 Всего примеров: {len(data)}")
    
    print("\n📂 Распределение по категориям:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {cat}: {count} ({count/len(data)*100:.1f}%)")
    
    print("\n⭐ Распределение по качеству:")
    for quality, count in quality_counts.items():
        print(f"   • {quality}: {count} ({count/len(data)*100:.1f}%)")
    
    print("\n" + "="*60)


def main():
    """Главная функция"""
    print("="*60)
    print("🎨 ВИЗУАЛИЗАЦИЯ ДАТАСЕТА")
    print("="*60)
    
    # Проверка существования файла датасета
    if not os.path.exists(DATA_PATH):
        print(f"❌ Файл датасета не найден: {DATA_PATH}")
        return
    
    # Загрузка данных
    print(f"\n📂 Загрузка датасета из: {DATA_PATH}")
    data = load_dataset()
    print(f"✅ Загружено {len(data)} примеров")
    
    # Создание визуализаций
    print("\n🎨 Создание визуализаций...\n")
    
    # 1. Распределение по категориям
    categories = plot_category_distribution(
        data, 
        os.path.join(OUTPUT_DIR, 'dataset_distribution.png')
    )
    
    # 2. Распределение по качеству
    quality_counts = plot_quality_distribution(
        data,
        os.path.join(OUTPUT_DIR, 'quality_distribution.png')
    )
    
    # 3. Корреляционная матрица
    plot_features_correlation(
        data,
        os.path.join(OUTPUT_DIR, 'features_correlation.png')
    )
    
    # 4. Статистика признаков (бонус)
    plot_features_statistics(
        data,
        os.path.join(OUTPUT_DIR, 'features_statistics.png')
    )
    
    # Вывод сводки
    print_dataset_summary(data, categories, quality_counts)
    
    print("\n✅ Все визуализации созданы успешно!")
    print(f"📁 Сохранены в: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

