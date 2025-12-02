"""
Генератор учебных заданий по программированию на Python
"""

import random
import json
import os
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class Task:
    """Структура задания"""
    id: str
    title: str
    description: str
    difficulty: str  # 'easy', 'medium', 'hard'
    category: str
    test_cases: List[Dict[str, Any]]
    expected_output: str
    hints: List[str]
    solution_template: str


class TaskGenerator:
    """Генератор учебных заданий по Python"""
    
    def __init__(self):
        """Инициализация генератора"""
        self.task_templates = self._load_task_templates()
        self.difficulty_levels = {
            'easy': {'min_lines': 5, 'max_lines': 15, 'complexity': 1},
            'medium': {'min_lines': 10, 'max_lines': 30, 'complexity': 2},
            'hard': {'min_lines': 20, 'max_lines': 50, 'complexity': 3}
        }
    
    def _load_task_templates(self) -> Dict[str, List[Dict]]:
        """
        Загрузка шаблонов заданий по программированию
        
        Создает и возвращает словарь с шаблонами заданий, разделенных по категориям:
        - algorithms: алгоритмические задачи (сортировка, поиск)
        - data_processing: обработка данных (работа со строками, фильтрация)
        - functions: функциональное программирование (рекурсия, математические функции)
        
        Каждый шаблон содержит название, описание, тестовые случаи и эталонное решение.
        
        Returns:
            Словарь с категориями и списками шаблонов заданий
        """
        return {
            'algorithms': [
                {
                    'template': 'sort_list',
                    'title': 'Сортировка списка',
                    'description': 'Напишите функцию для сортировки списка чисел',
                    'test_cases': [
                        {'input': '[3, 1, 4, 1, 5]', 'expected': '[1, 1, 3, 4, 5]'},
                        {'input': '[5, 4, 3, 2, 1]', 'expected': '[1, 2, 3, 4, 5]'},
                        {'input': '[1]', 'expected': '[1]'}
                    ],
                    'solution': 'def sort_list(numbers):\n    return sorted(numbers)'
                },
                {
                    'template': 'find_max',
                    'title': 'Поиск максимального элемента',
                    'description': 'Найдите максимальный элемент в списке',
                    'test_cases': [
                        {'input': '[1, 5, 3, 9, 2]', 'expected': '9'},
                        {'input': '[-1, -5, -3]', 'expected': '-1'},
                        {'input': '[42]', 'expected': '42'}
                    ],
                    'solution': 'def find_max(numbers):\n    return max(numbers)'
                }
            ],
            'data_processing': [
                {
                    'template': 'count_words',
                    'title': 'Подсчет слов',
                    'description': 'Подсчитайте количество слов в строке',
                    'test_cases': [
                        {'input': '"Hello world"', 'expected': '2'},
                        {'input': '"Python programming is fun"', 'expected': '4'},
                        {'input': '""', 'expected': '0'}
                    ],
                    'solution': 'def count_words(text):\n    return len(text.split())'
                },
                {
                    'template': 'filter_even',
                    'title': 'Фильтрация четных чисел',
                    'description': 'Отфильтруйте четные числа из списка',
                    'test_cases': [
                        {'input': '[1, 2, 3, 4, 5, 6]', 'expected': '[2, 4, 6]'},
                        {'input': '[1, 3, 5]', 'expected': '[]'},
                        {'input': '[2, 4, 6]', 'expected': '[2, 4, 6]'}
                    ],
                    'solution': 'def filter_even(numbers):\n    return [x for x in numbers if x % 2 == 0]'
                }
            ],
            'functions': [
                {
                    'template': 'fibonacci',
                    'title': 'Числа Фибоначчи',
                    'description': 'Вычислите n-е число Фибоначчи',
                    'test_cases': [
                        {'input': '5', 'expected': '8'},
                        {'input': '0', 'expected': '0'},
                        {'input': '10', 'expected': '55'}
                    ],
                    'solution': 'def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)'
                }
            ]
        }
    
    def generate_task(self, category: str = None, difficulty: str = 'medium') -> Task:
        """
        Генерация случайного задания
        
        Args:
            category: Категория задания
            difficulty: Уровень сложности
            
        Returns:
            Объект задания
        """
        if category is None:
            category = random.choice(list(self.task_templates.keys()))
        
        if category not in self.task_templates:
            raise ValueError(f"Неизвестная категория: {category}")
        
        template = random.choice(self.task_templates[category])
        
        # Генерация уникального ID
        task_id = f"{category}_{template['template']}_{random.randint(1000, 9999)}"
        
        # Создание задания
        task = Task(
            id=task_id,
            title=template['title'],
            description=template['description'],
            difficulty=difficulty,
            category=category,
            test_cases=template['test_cases'],
            expected_output='',  # Будет заполнено при проверке
            hints=self._generate_hints(template, difficulty),
            solution_template=template['solution']
        )
        
        return task
    
    def _generate_hints(self, template: Dict, difficulty: str) -> List[str]:
        """
        Генерация подсказок для задания в зависимости от сложности
        
        Создает список подсказок, адаптированных под уровень сложности задания:
        - easy: базовые советы по использованию встроенных функций
        - medium: рекомендации по алгоритмам и граничным случаям
        - hard: советы по оптимизации и тестированию
        
        Также добавляет специфичные подсказки в зависимости от типа задания.
        
        Args:
            template: Шаблон задания с информацией о типе
            difficulty: Уровень сложности ('easy', 'medium', 'hard')
            
        Returns:
            Список строк с подсказками
        """
        hints = []
        
        if difficulty == 'easy':
            hints.append("Используйте встроенные функции Python")
            hints.append("Помните о типах данных")
        elif difficulty == 'medium':
            hints.append("Подумайте об алгоритме решения")
            hints.append("Обратите внимание на граничные случаи")
        else:  # hard
            hints.append("Рассмотрите оптимизацию решения")
            hints.append("Проверьте все возможные входные данные")
        
        # Специфичные подсказки для разных типов заданий
        if 'sort' in template['template']:
            hints.append("Можно использовать sorted() или .sort()")
        elif 'fibonacci' in template['template']:
            hints.append("Рассмотрите рекурсивное решение")
        elif 'filter' in template['template']:
            hints.append("Используйте list comprehension или filter()")
        
        return hints
    
    def generate_custom_task(self, requirements: Dict[str, Any]) -> Task:
        """
        Генерация задания по пользовательским требованиям
        
        Args:
            requirements: Словарь с требованиями
            
        Returns:
            Объект задания
        """
        # Извлечение требований
        category = requirements.get('category', 'algorithms')
        difficulty = requirements.get('difficulty', 'medium')
        topic = requirements.get('topic', '')
        custom_tests = requirements.get('test_cases', [])
        
        # Поиск подходящего шаблона
        suitable_templates = []
        for cat_templates in self.task_templates.values():
            for template in cat_templates:
                if topic.lower() in template['title'].lower() or topic.lower() in template['description'].lower():
                    suitable_templates.append(template)
        
        if not suitable_templates:
            # Если не найден подходящий шаблон, создаем базовое задание
            return self._create_custom_task(requirements)
        
        template = random.choice(suitable_templates)
        
        # Создание задания на основе найденного шаблона
        task_id = f"custom_{random.randint(1000, 9999)}"
        
        task = Task(
            id=task_id,
            title=requirements.get('title', template['title']),
            description=requirements.get('description', template['description']),
            difficulty=difficulty,
            category=category,
            test_cases=custom_tests if custom_tests else template['test_cases'],
            expected_output='',
            hints=self._generate_hints(template, difficulty),
            solution_template=template['solution']
        )
        
        return task
    
    def _create_custom_task(self, requirements: Dict[str, Any]) -> Task:
        """
        Создание полностью кастомного задания без использования шаблона
        
        Используется когда не найден подходящий шаблон в библиотеке заданий.
        Создает базовое задание на основе требований пользователя.
        
        Args:
            requirements: Словарь с требованиями к заданию (title, description, 
                         difficulty, category, test_cases)
                         
        Returns:
            Объект Task с пользовательским заданием
        """
        task_id = f"custom_{random.randint(1000, 9999)}"
        
        # Генерация базовых тестовых случаев
        test_cases = requirements.get('test_cases', [
            {'input': 'test_input', 'expected': 'expected_output'}
        ])
        
        task = Task(
            id=task_id,
            title=requirements.get('title', 'Пользовательское задание'),
            description=requirements.get('description', 'Решите поставленную задачу'),
            difficulty=requirements.get('difficulty', 'medium'),
            category=requirements.get('category', 'custom'),
            test_cases=test_cases,
            expected_output='',
            hints=['Внимательно прочитайте условие задачи'],
            solution_template='# Ваше решение здесь'
        )
        
        return task
    
    def get_available_categories(self) -> List[str]:
        """
        Получение списка доступных категорий заданий
        
        Returns:
            Список названий категорий (algorithms, data_processing, functions)
        """
        return list(self.task_templates.keys())
    
    def get_difficulty_levels(self) -> List[str]:
        """
        Получение списка уровней сложности
        
        Returns:
            Список уровней сложности (easy, medium, hard)
        """
        return list(self.difficulty_levels.keys())
    
    def save_task(self, task: Task, filepath: str):
        """
        Сохранение задания в JSON-файл
        
        Сериализует объект Task в JSON и сохраняет по указанному пути.
        
        Args:
            task: Объект задания для сохранения
            filepath: Путь к файлу для сохранения
        """
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'difficulty': task.difficulty,
            'category': task.category,
            'test_cases': task.test_cases,
            'expected_output': task.expected_output,
            'hints': task.hints,
            'solution_template': task.solution_template
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(task_data, f, ensure_ascii=False, indent=2)
    
    def load_task(self, filepath: str) -> Task:
        """Загрузка задания из файла"""
        with open(filepath, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        
        return Task(
            id=task_data['id'],
            title=task_data['title'],
            description=task_data['description'],
            difficulty=task_data['difficulty'],
            category=task_data['category'],
            test_cases=task_data['test_cases'],
            expected_output=task_data['expected_output'],
            hints=task_data['hints'],
            solution_template=task_data['solution_template']
        )
