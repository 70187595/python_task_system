"""
Генератор обучающих данных для нейронной сети анализа качества кода
"""

import json
import os
from typing import List, Dict, Any

def generate_string_excellent():
    """Генерация отличных примеров работы со строками"""
    return [
        {
            "code": """def reverse_string(text):
    \"\"\"Переворачивает строку.\"\"\"
    return text[::-1]""",
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
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def capitalize_words(text):
    \"\"\"Делает заглавной первую букву каждого слова.\"\"\"
    return text.title()""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def remove_whitespace(text):
    \"\"\"Удаляет все пробелы из строки.\"\"\"
    return text.replace(' ', '')""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.9, 0.95]
        },
        {
            "code": """def count_vowels(text):
    \"\"\"Подсчитывает количество гласных в строке.\"\"\"
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in text if char in vowels)""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def is_palindrome(text):
    \"\"\"Проверяет, является ли строка палиндромом.\"\"\"
    cleaned = text.lower().replace(' ', '')
    return cleaned == cleaned[::-1]""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def get_first_word(text):
    \"\"\"Извлекает первое слово из строки.\"\"\"
    words = text.split()
    return words[0] if words else ''""",
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
            "code": """def join_with_separator(words, separator=', '):
    \"\"\"Объединяет список слов с разделителем.\"\"\"
    return separator.join(words)""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def extract_digits(text):
    \"\"\"Извлекает все цифры из строки.\"\"\"
    return ''.join(char for char in text if char.isdigit())""",
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
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def truncate_string(text, max_length):
    \"\"\"Обрезает строку до заданной длины с многоточием.\"\"\"
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """def remove_duplicates(text):
    \"\"\"Удаляет повторяющиеся символы подряд.\"\"\"
    if not text:
        return text
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.11,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.85]
        }
    ]

def generate_string_good():
    """Генерация средних примеров работы со строками"""
    return [
        {
            "code": """def reverse_string(text):
    result = ''
    for char in text:
        result = char + result
    return result""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.6, 0.65]
        },
        {
            "code": """def capitalize_words(text):
    words = text.split()
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    return ' '.join(capitalized)""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def remove_whitespace(text):
    result = ''
    for char in text:
        if char != ' ':
            result = result + char
    return result""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.6, 0.65]
        },
        {
            "code": """def count_vowels(text):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in text:
        if char in vowels:
            count = count + 1
    return count""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
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
            "code": """def is_palindrome(text):
    text_lower = text.lower()
    reversed_text = ''
    for char in text_lower:
        reversed_text = char + reversed_text
    return text_lower == reversed_text""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.65, 0.7]
        },
        {
            "code": """def get_first_word(text):
    word = ''
    for char in text:
        if char == ' ':
            break
        word = word + char
    return word""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.6, 0.65]
        },
        {
            "code": """def join_with_separator(words, separator):
    result = ''
    for i in range(len(words)):
        result = result + words[i]
        if i < len(words) - 1:
            result = result + separator
    return result""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        {
            "code": """def extract_digits(text):
    digits = ''
    for char in text:
        if char >= '0' and char <= '9':
            digits = digits + char
    return digits""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
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
            "code": """def truncate_string(text, max_length):
    if len(text) > max_length:
        truncated = ''
        for i in range(max_length - 3):
            truncated = truncated + text[i]
        return truncated + '...'
    return text""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        {
            "code": """def remove_duplicates(text):
    result = ''
    prev_char = ''
    for char in text:
        if char != prev_char:
            result = result + char
            prev_char = char
    return result""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.65, 0.65]
        }
    ]

def generate_string_poor():
    """Генерация плохих примеров работы со строками"""
    return [
        {
            "code": """def reverse_string(text):
    a = []
    for i in range(len(text)):
        a.append(text[i])
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    c = ''
    for x in b:
        c = c + x
    return c""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.4]
        },
        {
            "code": """def capitalize_words(text):
    x = text
    y = []
    z = ''
    for i in range(len(x)):
        if x[i] == ' ':
            y.append(z)
            z = ''
        else:
            z = z + x[i]
    y.append(z)
    result = []
    for w in y:
        result.append(w[0].upper() + w[1:])
    return ' '.join(result)""",
            "features": {
                "lines_of_code": 15.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
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
            "code": """def remove_whitespace(text):
    a = ''
    b = 0
    while b < len(text):
        c = text[b]
        if c != ' ':
            a = a + c
        b = b + 1
    return a""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.4]
        },
        {
            "code": """def count_vowels(text):
    a = 0
    b = 0
    c = 0
    for x in text:
        if x == 'a' or x == 'A':
            a = a + 1
        if x == 'e' or x == 'E':
            a = a + 1
        if x == 'i' or x == 'I':
            a = a + 1
        if x == 'o' or x == 'O':
            a = a + 1
        if x == 'u' or x == 'U':
            a = a + 1
        b = b + 1
        c = c + 2
    return a""",
            "features": {
                "lines_of_code": 18.0,
                "functions_count": 1.0,
                "complexity": 0.6,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def is_palindrome(text):
    a = text.lower()
    b = len(a)
    c = True
    for i in range(b):
        if a[i] != a[b-1-i]:
            c = False
    return c""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.4]
        },
        {
            "code": """def get_first_word(text):
    a = ''
    b = 0
    c = 0
    d = 0
    for x in text:
        if x == ' ':
            break
        a = a + x
        b = b + 1
        c = c + 1
        d = d + 1
    return a""",
            "features": {
                "lines_of_code": 13.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def join_with_separator(words, separator):
    a = ''
    b = 0
    for w in words:
        a = a + w
        b = b + 1
        if b < len(words):
            a = a + separator
        else:
            pass
    return a""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 5.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def extract_digits(text):
    a = ''
    b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in text:
        for y in b:
            if x == y:
                a = a + x
    return a""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.4]
        },
        {
            "code": """def truncate_string(text, max_length):
    a = len(text)
    b = max_length
    c = ''
    if a > b:
        for i in range(b - 3):
            c = c + text[i]
        c = c + '.'
        c = c + '.'
        c = c + '.'
    else:
        c = text
    return c""",
            "features": {
                "lines_of_code": 13.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
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
            "code": """def remove_duplicates(text):
    a = ''
    b = ''
    c = 0
    d = 0
    for x in text:
        if x != b:
            a = a + x
        b = x
        c = c + 1
        d = d + 1
    return a""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        }
    ]

def generate_lists_examples():
    """Генерация примеров работы со списками (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def sum_list(numbers):
    \"\"\"Возвращает сумму элементов списка.\"\"\"
    return sum(numbers)""",
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
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def get_unique(items):
    \"\"\"Возвращает список уникальных элементов.\"\"\"
    return list(set(items))""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def flatten_list(nested_list):
    \"\"\"Разворачивает вложенный список.\"\"\"
    return [item for sublist in nested_list for item in sublist]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def chunk_list(items, size):
    \"\"\"Разбивает список на части заданного размера.\"\"\"
    return [items[i:i+size] for i in range(0, len(items), size)]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def remove_none(items):
    \"\"\"Удаляет None из списка.\"\"\"
    return [item for item in items if item is not None]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.9, 0.95]
        },
        
        # Средние примеры (5)
        {
            "code": """def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.65, 0.7]
        },
        {
            "code": """def get_unique(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        {
            "code": """def flatten_list(nested_list):
    result = []
    for sublist in nested_list:
        for item in sublist:
            result.append(item)
    return result""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.65, 0.7]
        },
        {
            "code": """def chunk_list(items, size):
    chunks = []
    for i in range(0, len(items), size):
        chunk = items[i:i+size]
        chunks.append(chunk)
    return chunks""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def remove_none(items):
    result = []
    for item in items:
        if item != None:
            result.append(item)
    return result""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        
        # Плохие примеры (5)
        {
            "code": """def sum_list(numbers):
    a = 0
    b = 0
    c = 0
    for x in numbers:
        a = a + x
        b = b + 1
        c = c + 2
    return a""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def get_unique(items):
    a = []
    for i in range(len(items)):
        b = items[i]
        c = False
        for j in range(len(a)):
            if a[j] == b:
                c = True
        if c == False:
            a.append(b)
    return a""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 3.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def flatten_list(nested_list):
    a = []
    b = 0
    while b < len(nested_list):
        c = nested_list[b]
        d = 0
        while d < len(c):
            a.append(c[d])
            d = d + 1
        b = b + 1
    return a""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def chunk_list(items, size):
    a = []
    b = []
    c = 0
    for x in items:
        b.append(x)
        c = c + 1
        if c == size:
            a.append(b)
            b = []
            c = 0
    if len(b) > 0:
        a.append(b)
    return a""",
            "features": {
                "lines_of_code": 14.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def remove_none(items):
    a = []
    b = 0
    c = 0
    d = 0
    for x in items:
        if x != None:
            a.append(x)
        b = b + 1
        c = c + 1
        d = d + 1
    return a""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        }
    ]

def generate_dict_examples():
    """Генерация примеров работы со словарями (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def merge_dicts(dict1, dict2):
    \"\"\"Объединяет два словаря.\"\"\"
    return {**dict1, **dict2}""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def get_keys_by_value(dictionary, value):
    \"\"\"Возвращает ключи по значению.\"\"\"
    return [k for k, v in dictionary.items() if v == value]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def invert_dict(dictionary):
    \"\"\"Меняет местами ключи и значения.\"\"\"
    return {v: k for k, v in dictionary.items()}""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def filter_dict(dictionary, keys):
    \"\"\"Оставляет только указанные ключи.\"\"\"
    return {k: v for k, v in dictionary.items() if k in keys}""",
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
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def count_values(dictionary):
    \"\"\"Подсчитывает количество каждого значения.\"\"\"
    from collections import Counter
    return dict(Counter(dictionary.values()))""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.25,
                "imports_count": 1.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.95, 0.9]
        },
        
        # Средние примеры (5)
        {
            "code": """def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2:
        result[key] = dict2[key]
    return result""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.7, 0.7]
        },
        {
            "code": """def get_keys_by_value(dictionary, value):
    keys = []
    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)
    return keys""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def invert_dict(dictionary):
    inverted = {}
    for key in dictionary:
        inverted[dictionary[key]] = key
    return inverted""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.7, 0.7]
        },
        {
            "code": """def filter_dict(dictionary, keys):
    filtered = {}
    for key in dictionary:
        if key in keys:
            filtered[key] = dictionary[key]
    return filtered""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def count_values(dictionary):
    counts = {}
    for value in dictionary.values():
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
    return counts""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        
        # Плохие примеры (5)
        {
            "code": """def merge_dicts(dict1, dict2):
    a = {}
    b = list(dict1.keys())
    c = list(dict2.keys())
    for i in range(len(b)):
        a[b[i]] = dict1[b[i]]
    for j in range(len(c)):
        a[c[j]] = dict2[c[j]]
    return a""",
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
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def get_keys_by_value(dictionary, value):
    a = []
    b = list(dictionary.keys())
    c = 0
    for i in range(len(b)):
        if dictionary[b[i]] == value:
            a.append(b[i])
        c = c + 1
    return a""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
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
            "code": """def invert_dict(dictionary):
    a = {}
    b = []
    c = []
    for x in dictionary:
        b.append(x)
        c.append(dictionary[x])
    for i in range(len(b)):
        a[c[i]] = b[i]
    return a""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def filter_dict(dictionary, keys):
    a = {}
    b = 0
    c = 0
    for x in dictionary:
        if x in keys:
            a[x] = dictionary[x]
        b = b + 1
        c = c + 1
    return a""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def count_values(dictionary):
    a = {}
    b = list(dictionary.values())
    c = 0
    for i in range(len(b)):
        d = b[i]
        if d in a:
            a[d] = a[d] + 1
        else:
            a[d] = 1
        c = c + 1
    return a""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        }
    ]

def generate_recursion_examples():
    """Генерация примеров рекурсивных функций (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def factorial(n):
    \"\"\"Вычисляет факториал числа.\"\"\"
    if n <= 1:
        return 1
    return n * factorial(n - 1)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """def sum_recursive(numbers):
    \"\"\"Рекурсивно суммирует элементы списка.\"\"\"
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.8, 0.9]
        },
        {
            "code": """def power(base, exp):
    \"\"\"Возводит число в степень рекурсивно.\"\"\"
    if exp == 0:
        return 1
    return base * power(base, exp - 1)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.8, 0.9]
        },
        {
            "code": """def gcd(a, b):
    \"\"\"Наибольший общий делитель (алгоритм Евклида).\"\"\"
    if b == 0:
        return a
    return gcd(b, a % b)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 5.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.9, 0.9]
        },
        {
            "code": """def binary_search(arr, target, left=0, right=None):
    \"\"\"Бинарный поиск рекурсивно.\"\"\"
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.08,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.85]
        },
        
        # Средние примеры (5)
        {
            "code": """def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def sum_recursive(numbers):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_recursive(numbers[1:])""",
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
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """def gcd(a, b):
    if b == 0:
        result = a
    else:
        result = gcd(b, a % b)
    return result""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 6.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        
        # Плохие примеры (5)
        {
            "code": """def factorial(n):
    if n == 0:
        a = 1
        return a
    if n == 1:
        b = 1
        return b
    c = n
    d = n - 1
    e = factorial(d)
    f = c * e
    return f""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def sum_recursive(numbers):
    a = len(numbers)
    if a == 0:
        return 0
    b = numbers[0]
    c = []
    for i in range(1, a):
        c.append(numbers[i])
    d = sum_recursive(c)
    return b + d""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def power(base, exp):
    a = exp
    if a == 0:
        b = 1
        return b
    c = exp - 1
    d = power(base, c)
    e = base
    f = e * d
    return f""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def gcd(a, b):
    x = a
    y = b
    if y == 0:
        z = x
        return z
    w = x % y
    v = gcd(y, w)
    return v""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.4]
        },
        {
            "code": """def binary_search(arr, target, left, right):
    a = left
    b = right
    if a > b:
        return -1
    c = (a + b) // 2
    d = arr[c]
    if d == target:
        return c
    if d > target:
        e = c - 1
        return binary_search(arr, target, a, e)
    f = c + 1
    return binary_search(arr, target, f, b)""",
            "features": {
                "lines_of_code": 14.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        }
    ]

def generate_loops_examples():
    """Генерация примеров с циклами (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def find_all_indices(items, value):
    \"\"\"Находит все индексы значения в списке.\"\"\"
    return [i for i, item in enumerate(items) if item == value]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def multiply_elements(numbers, multiplier):
    \"\"\"Умножает каждый элемент списка на число.\"\"\"
    return [num * multiplier for num in numbers]""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def create_matrix(rows, cols, default=0):
    \"\"\"Создает матрицу заданного размера.\"\"\"
    return [[default for _ in range(cols)] for _ in range(rows)]""",
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
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def group_by_length(words):
    \"\"\"Группирует слова по длине.\"\"\"
    result = {}
    for word in words:
        length = len(word)
        result.setdefault(length, []).append(word)
    return result""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.14,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """def running_average(numbers):
    \"\"\"Вычисляет скользящее среднее.\"\"\"
    result = []
    for i in range(len(numbers)):
        avg = sum(numbers[:i+1]) / (i+1)
        result.append(avg)
    return result""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.14,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.9, 0.8, 0.85]
        },
        
        # Средние примеры (5)
        {
            "code": """def find_all_indices(items, value):
    indices = []
    for i in range(len(items)):
        if items[i] == value:
            indices.append(i)
    return indices""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def multiply_elements(numbers, multiplier):
    result = []
    for num in numbers:
        result.append(num * multiplier)
    return result""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.7, 0.75]
        },
        {
            "code": """def create_matrix(rows, cols, default):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(default)
        matrix.append(row)
    return matrix""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.7, 0.75]
        },
        {
            "code": """def running_average(numbers):
    result = []
    for i in range(len(numbers)):
        total = 0
        for j in range(i + 1):
            total = total + numbers[j]
        avg = total / (i + 1)
        result.append(avg)
    return result""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        
        # Плохие примеры (5)
        {
            "code": """def find_all_indices(items, value):
    a = []
    b = 0
    c = 0
    while b < len(items):
        if items[b] == value:
            a.append(b)
        b = b + 1
        c = c + 1
    return a""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def multiply_elements(numbers, multiplier):
    a = []
    b = 0
    while b < len(numbers):
        c = numbers[b]
        d = c * multiplier
        a.append(d)
        b = b + 1
    return a""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 4.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def create_matrix(rows, cols, default):
    a = []
    b = 0
    while b < rows:
        c = []
        d = 0
        while d < cols:
            c.append(default)
            d = d + 1
        a.append(c)
        b = b + 1
    return a""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def group_by_length(words):
    a = {}
    b = 0
    for x in words:
        c = len(x)
        d = 0
        if c not in a:
            a[c] = []
        a[c].append(x)
        b = b + 1
        d = d + 1
    return a""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def running_average(numbers):
    a = []
    b = 0
    while b < len(numbers):
        c = 0
        d = 0
        e = 0
        while e <= b:
            c = c + numbers[e]
            d = d + 1
            e = e + 1
        f = c / (b + 1)
        a.append(f)
        b = b + 1
    return a""",
            "features": {
                "lines_of_code": 15.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        }
    ]

def generate_conditionals_examples():
    """Генерация примеров с условными операторами (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def get_grade(score):
    \"\"\"Возвращает буквенную оценку по баллу.\"\"\"
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.09,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """def classify_number(num):
    \"\"\"Классифицирует число.\"\"\"
    return 'positive' if num > 0 else 'negative' if num < 0 else 'zero'""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.9, 0.9]
        },
        {
            "code": """def is_valid_triangle(a, b, c):
    \"\"\"Проверяет, можно ли построить треугольник.\"\"\"
    return (a + b > c) and (a + c > b) and (b + c > a)""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 0.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def get_max_of_three(a, b, c):
    \"\"\"Возвращает максимум из трех чисел.\"\"\"
    return max(a, b, c)""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def safe_divide(a, b):
    \"\"\"Безопасное деление с обработкой нуля.\"\"\"
    return a / b if b != 0 else None""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        
        # Средние примеры (5)
        {
            "code": """def get_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def classify_number(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'""",
            "features": {
                "lines_of_code": 7.0,
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
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """def is_valid_triangle(a, b, c):
    if a + b > c:
        if a + c > b:
            if b + c > a:
                return True
    return False""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.65]
        },
        {
            "code": """def get_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.75]
        },
        {
            "code": """def safe_divide(a, b):
    if b != 0:
        result = a / b
    else:
        result = None
    return result""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        
        # Плохие примеры (5)
        {
            "code": """def get_grade(score):
    a = score
    b = ''
    if a >= 90:
        b = 'A'
    if a < 90 and a >= 80:
        b = 'B'
    if a < 80 and a >= 70:
        b = 'C'
    if a < 70 and a >= 60:
        b = 'D'
    if a < 60:
        b = 'F'
    return b""",
            "features": {
                "lines_of_code": 14.0,
                "functions_count": 1.0,
                "complexity": 0.6,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.4]
        },
        {
            "code": """def classify_number(num):
    a = num
    b = ''
    c = 0
    if a > c:
        b = 'positive'
    if a < c:
        b = 'negative'
    if a == c:
        b = 'zero'
    return b""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """def is_valid_triangle(a, b, c):
    x = a
    y = b
    z = c
    w = False
    if x + y > z:
        if x + z > y:
            if y + z > x:
                w = True
            else:
                w = False
    return w""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def get_max_of_three(a, b, c):
    x = a
    y = b
    z = c
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.4]
        },
        {
            "code": """def safe_divide(a, b):
    x = a
    y = b
    z = 0
    r = None
    if y != z:
        r = x / y
    else:
        r = None
    return r""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        }
    ]

def generate_math_examples():
    """Генерация примеров математических функций (все уровни качества)"""
    return [
        # Отличные примеры (7)
        {
            "code": """def is_prime(n):
    \"\"\"Проверяет, является ли число простым.\"\"\"
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.2,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def is_even(number):
    \"\"\"Проверяет, является ли число четным.\"\"\"
    return number % 2 == 0""",
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
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def calculate_distance(x1, y1, x2, y2):
    \"\"\"Вычисляет евклидово расстояние между точками.\"\"\"
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 13.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def mean(numbers):
    \"\"\"Вычисляет среднее арифметическое.\"\"\"
    return sum(numbers) / len(numbers) if numbers else 0""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def lcm(a, b):
    \"\"\"Наименьшее общее кратное.\"\"\"
    from math import gcd
    return abs(a * b) // gcd(a, b) if a and b else 0""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 0.0,
                "variable_names_length": 5.0,
                "comments_ratio": 0.25,
                "imports_count": 1.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.95, 0.9]
        },
        {
            "code": """def is_perfect_square(n):
    \"\"\"Проверяет, является ли число точным квадратом.\"\"\"
    return int(n**0.5)**2 == n""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 13.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [1.0, 0.95, 0.95]
        },
        {
            "code": """def digits_sum(number):
    \"\"\"Вычисляет сумму цифр числа.\"\"\"
    return sum(int(digit) for digit in str(abs(number)))""",
            "features": {
                "lines_of_code": 3.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.33,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        
        # Средние примеры (7)
        {
            "code": """def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.5, 0.7]
        },
        {
            "code": """def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.7]
        },
        {
            "code": """def calculate_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx**2 + dy**2)**0.5
    return distance""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """def mean(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 7.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.65, 0.7]
        },
        {
            "code": """def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return (a * b) // gcd(a, b)""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 2.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 5.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """def is_perfect_square(n):
    sqrt = int(n**0.5)
    if sqrt * sqrt == n:
        return True
    return False""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def digits_sum(number):
    total = 0
    for digit in str(number):
        if digit.isdigit():
            total = total + int(digit)
    return total""",
            "features": {
                "lines_of_code": 6.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        
        # Плохие примеры (6)
        {
            "code": """def is_prime(n):
    a = n
    b = 2
    c = True
    if a < b:
        c = False
    d = b
    while d < a:
        if a % d == 0:
            c = False
        d = d + 1
    return c""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def is_even(number):
    a = number
    b = 2
    c = a % b
    d = 0
    if c == d:
        e = True
    else:
        e = False
    return e""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def calculate_distance(x1, y1, x2, y2):
    a = x2
    b = x1
    c = a - b
    d = y2
    e = y1
    f = d - e
    g = c * c
    h = f * f
    i = g + h
    j = i ** 0.5
    return j""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def mean(numbers):
    a = 0
    b = 0
    c = 0
    for x in numbers:
        a = a + x
        b = b + 1
        c = c + 1
    d = len(numbers)
    e = a / d
    return e""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def is_perfect_square(n):
    a = n
    b = 0
    c = 0.5
    d = a ** c
    e = int(d)
    f = e * e
    if f == a:
        return True
    else:
        return False""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def digits_sum(number):
    a = str(number)
    b = 0
    c = 0
    for x in a:
        if x.isdigit():
            d = int(x)
            b = b + d
        c = c + 1
    return b""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        }
    ]

def generate_file_examples():
    """Генерация примеров работы с файлами (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def read_file_lines(filename):
    \"\"\"Читает все строки из файла.\"\"\"
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def write_to_file(filename, content):
    \"\"\"Записывает содержимое в файл.\"\"\"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def count_lines(filename):
    \"\"\"Подсчитывает количество строк в файле.\"\"\"
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.95, 0.95]
        },
        {
            "code": """def append_to_file(filename, text):
    \"\"\"Добавляет текст в конец файла.\"\"\"
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\\n')""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """def find_in_file(filename, search_text):
    \"\"\"Находит строки, содержащие текст.\"\"\"
    with open(filename, 'r', encoding='utf-8') as f:
        return [line for line in f if search_text in line]""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.25,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        
        # Средние примеры (5)
        {
            "code": """def read_file_lines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.6, 0.65]
        },
        {
            "code": """def write_to_file(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()""",
            "features": {
                "lines_of_code": 4.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.65, 0.7]
        },
        {
            "code": """def count_lines(filename):
    f = open(filename, 'r')
    count = 0
    for line in f:
        count = count + 1
    f.close()
    return count""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        {
            "code": """def append_to_file(filename, text):
    file = open(filename, 'a')
    file.write(text)
    file.write('\\n')
    file.close()""",
            "features": {
                "lines_of_code": 5.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def find_in_file(filename, search_text):
    f = open(filename, 'r')
    result = []
    for line in f:
        if search_text in line:
            result.append(line)
    f.close()
    return result""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        
        # Плохие примеры (5)
        {
            "code": """def read_file_lines(filename):
    a = filename
    b = open(a, 'r')
    c = []
    d = 0
    for x in b:
        c.append(x)
        d = d + 1
    b.close()
    return c""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def write_to_file(filename, content):
    a = filename
    b = content
    c = open(a, 'w')
    d = b
    c.write(d)
    e = 0
    c.close()""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def count_lines(filename):
    a = filename
    b = open(a, 'r')
    c = 0
    d = 0
    e = 0
    for x in b:
        c = c + 1
        d = d + 1
        e = e + 1
    b.close()
    return c""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """def append_to_file(filename, text):
    a = filename
    b = text
    c = open(a, 'a')
    d = b + '\\n'
    e = d
    c.write(e)
    f = 0
    c.close()""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.1,
                "nested_levels": 0.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def find_in_file(filename, search_text):
    a = filename
    b = search_text
    c = open(a, 'r')
    d = []
    e = 0
    for x in c:
        if b in x:
            d.append(x)
        e = e + 1
    c.close()
    return d""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        }
    ]

def generate_oop_examples():
    """Генерация примеров ООП с классами (все уровни качества)"""
    return [
        # Отличные примеры (7)
        {
            "code": """class Rectangle:
    \"\"\"Прямоугольник с шириной и высотой.\"\"\"
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        \"\"\"Вычисляет площадь.\"\"\"
        return self.width * self.height""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.22,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """class Counter:
    \"\"\"Счётчик с методами увеличения и сброса.\"\"\"
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def reset(self):
        self.count = 0""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 3.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.1,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """class Point:
    \"\"\"Точка в 2D пространстве.\"\"\"
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        \"\"\"Расстояние до другой точки.\"\"\"
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.22,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """class BankAccount:
    \"\"\"Банковский счёт.\"\"\"
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False""",
            "features": {
                "lines_of_code": 14.0,
                "functions_count": 3.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.07,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.9]
        },
        {
            "code": """class Person:
    \"\"\"Человек с именем и возрастом.\"\"\"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f\"{self.name}, {self.age} лет\"""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.125,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.95]
        },
        {
            "code": """class Stack:
    \"\"\"Стек (LIFO).\"\"\"
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop() if self._items else None""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 3.0,
                "complexity": 0.2,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.1,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """class Car:
    \"\"\"Автомобиль с маркой и годом.\"\"\"
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    @property
    def age(self):
        from datetime import datetime
        return datetime.now().year - self.year""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.1,
                "imports_count": 1.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        
        # Средние примеры (7)
        {
            "code": """class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        result = self.width * self.height
        return result""",
            "features": {
                "lines_of_code": 8.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1
    
    def reset(self):
        self.count = 0""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 3.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 3.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return self.name + ', ' + str(self.age) + ' лет'""",
            "features": {
                "lines_of_code": 7.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 3.0,
                "complexity": 0.2,
                "nested_levels": 2.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def get_age(self):
        current_year = 2024
        age = current_year - self.year
        return age""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 8.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.7, 0.65, 0.7]
        },
        
        # Плохие примеры (6)
        {
            "code": """class Rectangle:
    def __init__(self, width, height):
        self.a = width
        self.b = height
    
    def area(self):
        c = self.a
        d = self.b
        e = c * d
        f = e
        return f""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.3]
        },
        {
            "code": """class Counter:
    def __init__(self):
        self.a = 0
        self.b = 0
    
    def increment(self):
        self.a = self.a + 1
        self.b = self.b + 1
    
    def reset(self):
        self.a = 0
        self.b = 0""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 3.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """class Point:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def distance_to(self, other):
        c = self.a
        d = other.a
        e = c - d
        f = self.b
        g = other.b
        h = f - g
        i = e * e
        j = h * h
        k = i + j
        m = k ** 0.5
        return m""",
            "features": {
                "lines_of_code": 17.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        },
        {
            "code": """class BankAccount:
    def __init__(self):
        self.a = 0
        self.b = 0
    
    def deposit(self, amount):
        c = amount
        if c > 0:
            self.a = self.a + c
        self.b = self.b + 1
    
    def withdraw(self, amount):
        d = amount
        if d > 0:
            if d <= self.a:
                self.a = self.a - d""",
            "features": {
                "lines_of_code": 16.0,
                "functions_count": 3.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """class Stack:
    def __init__(self):
        self.a = []
        self.b = 0
    
    def push(self, item):
        self.a.append(item)
        self.b = self.b + 1
    
    def pop(self):
        c = len(self.a)
        if c > 0:
            d = self.a.pop()
            self.b = self.b - 1
            return d
        return None""",
            "features": {
                "lines_of_code": 16.0,
                "functions_count": 3.0,
                "complexity": 0.2,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.4]
        },
        {
            "code": """class Car:
    def __init__(self, brand, year):
        self.a = brand
        self.b = year
        self.c = 0
    
    def get_age(self):
        d = 2024
        e = self.b
        f = d - e
        g = f
        return g""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 2.0,
                "complexity": 0.1,
                "nested_levels": 1.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 1.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.3]
        }
    ]

def generate_sorting_examples():
    """Генерация примеров алгоритмов сортировки (все уровни качества)"""
    return [
        # Отличные примеры (5)
        {
            "code": """def quick_sort(arr):
    \"\"\"Быстрая сортировка.\"\"\"
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 1.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.11,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.9, 0.9]
        },
        {
            "code": """def merge_sort(arr):
    \"\"\"Сортировка слиянием.\"\"\"
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result""",
            "features": {
                "lines_of_code": 22.0,
                "functions_count": 2.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.045,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.95, 0.85]
        },
        {
            "code": """def insertion_sort(arr):
    \"\"\"Сортировка вставками.\"\"\"
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr""",
            "features": {
                "lines_of_code": 10.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.1,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.9, 0.8, 0.85]
        },
        {
            "code": """def selection_sort(arr):
    \"\"\"Сортировка выбором.\"\"\"
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.11,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.9, 0.7, 0.85]
        },
        {
            "code": """def counting_sort(arr):
    \"\"\"Сортировка подсчетом (для неотрицательных чисел).\"\"\"
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    return [i for i, cnt in enumerate(count) for _ in range(cnt)]""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 1.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.11,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.95, 0.85, 0.85]
        },
        
        # Средние примеры (5)
        {
            "code": """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr""",
            "features": {
                "lines_of_code": 9.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.6, 0.7]
        },
        {
            "code": """def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j = j - 1
            else:
                break
        arr[j + 1] = key
    return arr""",
            "features": {
                "lines_of_code": 12.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 11.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        {
            "code": """def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    return arr""",
            "features": {
                "lines_of_code": 11.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 3.0,
                "variable_names_length": 12.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.65, 0.7]
        },
        {
            "code": """def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = []
    equal = []
    greater = []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return quick_sort(less) + equal + quick_sort(greater)""",
            "features": {
                "lines_of_code": 16.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 9.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.8, 0.75, 0.75]
        },
        {
            "code": """def counting_sort(arr):
    if len(arr) == 0:
        return arr
    max_value = max(arr)
    counts = []
    for i in range(max_value + 1):
        counts.append(0)
    for number in arr:
        counts[number] = counts[number] + 1
    result = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            result.append(i)
    return result""",
            "features": {
                "lines_of_code": 14.0,
                "functions_count": 1.0,
                "complexity": 0.3,
                "nested_levels": 2.0,
                "variable_names_length": 10.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.75, 0.7, 0.7]
        },
        
        # Плохие примеры (5)
        {
            "code": """def bubble_sort(arr):
    a = len(arr)
    b = 0
    for i in range(a):
        c = 0
        for j in range(0, a - i - 1):
            if arr[j] > arr[j + 1]:
                d = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = d
            c = c + 1
        b = b + 1
    return arr""",
            "features": {
                "lines_of_code": 13.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def insertion_sort(arr):
    a = 1
    while a < len(arr):
        b = arr[a]
        c = a - 1
        d = 0
        while c >= 0 and arr[c] > b:
            arr[c + 1] = arr[c]
            c = c - 1
            d = d + 1
        arr[c + 1] = b
        a = a + 1
    return arr""",
            "features": {
                "lines_of_code": 13.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.5, 0.3]
        },
        {
            "code": """def selection_sort(arr):
    a = 0
    b = len(arr)
    while a < b:
        c = a
        d = a + 1
        while d < b:
            if arr[d] < arr[c]:
                c = d
            d = d + 1
        e = arr[a]
        arr[a] = arr[c]
        arr[c] = e
        a = a + 1
    return arr""",
            "features": {
                "lines_of_code": 15.0,
                "functions_count": 1.0,
                "complexity": 0.4,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.6, 0.4, 0.3]
        },
        {
            "code": """def quick_sort(arr):
    a = len(arr)
    if a <= 1:
        return arr
    b = arr[0]
    c = []
    d = []
    e = []
    f = 0
    for x in arr:
        if x < b:
            c.append(x)
        if x == b:
            d.append(x)
        if x > b:
            e.append(x)
        f = f + 1
    g = quick_sort(c)
    h = quick_sort(e)
    return g + d + h""",
            "features": {
                "lines_of_code": 21.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 0.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.4, 0.3]
        },
        {
            "code": """def counting_sort(arr):
    a = arr
    if len(a) == 0:
        return a
    b = max(a)
    c = []
    d = 0
    while d <= b:
        c.append(0)
        d = d + 1
    e = 0
    for x in a:
        c[x] = c[x] + 1
        e = e + 1
    f = []
    g = 0
    while g < len(c):
        h = 0
        while h < c[g]:
            f.append(g)
            h = h + 1
        g = g + 1
    return f""",
            "features": {
                "lines_of_code": 23.0,
                "functions_count": 1.0,
                "complexity": 0.5,
                "nested_levels": 2.0,
                "variable_names_length": 3.0,
                "comments_ratio": 0.0,
                "imports_count": 0.0,
                "class_count": 0.0,
                "error_handling": 1.0,
                "test_coverage": 0.0
            },
            "target": [0.5, 0.3, 0.3]
        }
    ]

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
    
    # Добавляем новые примеры работы со строками (отличное качество)
    training_data.extend(generate_string_excellent())
    
    # Добавляем новые примеры работы со строками (среднее качество)
    training_data.extend(generate_string_good())
    
    # Добавляем новые примеры работы со строками (плохое качество)
    training_data.extend(generate_string_poor())
    
    # Добавляем примеры работы со списками (все уровни)
    training_data.extend(generate_lists_examples())
    
    # Добавляем примеры работы со словарями (все уровни)
    training_data.extend(generate_dict_examples())
    
    # Добавляем примеры рекурсивных функций (все уровни)
    training_data.extend(generate_recursion_examples())
    
    # Добавляем примеры с циклами (все уровни)
    training_data.extend(generate_loops_examples())
    
    # Добавляем примеры с условными операторами (все уровни)
    training_data.extend(generate_conditionals_examples())
    
    # Добавляем примеры математических функций (все уровни)
    training_data.extend(generate_math_examples())
    
    # Добавляем примеры работы с файлами (все уровни)
    training_data.extend(generate_file_examples())
    
    # Добавляем примеры ООП с классами (все уровни)
    training_data.extend(generate_oop_examples())
    
    # Добавляем примеры алгоритмов сортировки (все уровни)
    training_data.extend(generate_sorting_examples())
    
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
