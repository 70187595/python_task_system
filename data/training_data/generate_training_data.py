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
