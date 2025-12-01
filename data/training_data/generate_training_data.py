"""
Генератор обучающих данных для нейронной сети анализа качества кода
"""

import json
import os
from typing import List, Dict, Any

def generate_training_data():
    """Генерация обучающих данных для нейронной сети"""
    
    training_data = []
    
    # Отличные решения (высокое качество)
    excellent_solutions = [
        {
            "code": """def sort_list(numbers):
    \"\"\"Сортирует список чисел по возрастанию.\"\"\"
    return sorted(numbers)""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.9, 0.95]  # correctness, efficiency, readability
        },
        {
            "code": """def fibonacci(n):
    \"\"\"Вычисляет n-е число Фибоначчи.\"\"\"
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.9, 0.7, 0.85]
        },
        {
            "code": """def find_max(numbers):
    \"\"\"Находит максимальный элемент в списке.\"\"\"
    if not numbers:
        return None
    return max(numbers)""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.8, 0.9]
        },
        {
            "code": """def count_words(text):
    \"\"\"Подсчитывает количество слов в строке.\"\"\"
    if not text:
        return 0
    return len(text.split())""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """def filter_even(numbers):
    \"\"\"Фильтрует четные числа из списка.\"\"\"
    return [x for x in numbers if x % 2 == 0]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.9, 0.9, 0.85]
        }
    ]
    
    # Хорошие решения (среднее качество)
    good_solutions = [
        {
            "code": """def sort_list(numbers):
    result = []
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.6,
                "nested_levels": 2.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.6, 0.6]
        },
        {
            "code": """def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.85, 0.8, 0.7]
        },
        {
            "code": """def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.7, 0.75]
        },
        {
            "code": """def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.7, 0.75]
        }
    ]
    
    # Плохие решения (низкое качество)
    poor_solutions = [
        {
            "code": """def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.8,
                "nested_levels": 2.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.4, 0.3, 0.5]
        },
        {
            "code": """def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.6]
        },
        {
            "code": """def find_max(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i
    return max""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 4.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.6, 0.5]
        },
        {
            "code": """def count_words(text):
    count = 0
    for char in text:
        if char == ' ':
            count = count + 1
    return count + 1""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.4, 0.5, 0.5]
        },
        {
            "code": """def filter_even(numbers):
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
        i = i + 1
    return result""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.6, 0.6]
        }
    ]
    
    # Очень плохие решения (очень низкое качество)
    terrible_solutions = [
        {
            "code": """def sort_list(numbers):
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if numbers[i % len(numbers)] > numbers[j % len(numbers)]:
                    temp = numbers[i % len(numbers)]
                    numbers[i % len(numbers)] = numbers[j % len(numbers)]
                    numbers[j % len(numbers)] = temp""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 1.0,
                "nested_levels": 3.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.1, 0.1, 0.3]
        },
        {
            "code": """def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            for j in range(100):
                pass
        return b""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.7,
                "nested_levels": 2.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.2, 0.4]
        },
        {
            "code": """def find_max(numbers):
    x = 0
    y = 0
    z = 0
    for i in range(len(numbers)):
        if numbers[i] > x:
            x = numbers[i]
        y = y + 1
        z = z * 2
    return x""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 4.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.4]
        },
        {
            "code": """def count_words(text):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in text:
        if i == ' ':
            a = a + 1
        b = b + 1
        c = c + 1
        d = d + 1
        e = e + 1
    return a + 1""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 4.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.4, 0.3, 0.3]
        },
        {
            "code": """def filter_even(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
        else:
            pass
        for j in range(10):
            pass
    return result""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.5]
        }
    ]
    
    # Объединяем все данные
    training_data.extend(excellent_solutions)
    training_data.extend(good_solutions)
    training_data.extend(poor_solutions)
    training_data.extend(terrible_solutions)
    
    return training_data

def save_training_data():
    """Сохранение обучающих данных в файл"""
    data = generate_training_data()
    
    # Создаем папку если не существует
    os.makedirs('data/training_data', exist_ok=True)
    
    # Сохраняем данные
    with open('data/training_data/training_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Создано {len(data)} примеров обучающих данных")
    print("📁 Сохранено в: data/training_data/training_data.json")
    
    # Статистика
    excellent_count = len([d for d in data if all(score >= 0.8 for score in d['target'])])
    good_count = len([d for d in data if any(0.6 <= score < 0.8 for score in d['target'])])
    poor_count = len([d for d in data if all(score < 0.6 for score in d['target'])])
    
    print(f"\n📊 Статистика:")
    print(f"   Отличные решения: {excellent_count}")
    print(f"   Хорошие решения: {good_count}")
    print(f"   Плохие решения: {poor_count}")

if __name__ == '__main__':
    save_training_data()
