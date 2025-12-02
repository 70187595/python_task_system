"""
Анализатор кода Python для извлечения признаков
"""

import ast
import re
from typing import Dict, List, Any, Set


class CodeAnalyzer:
    """Анализатор кода Python для извлечения признаков"""
    
    def __init__(self):
        """Инициализация анализатора"""
        self.reserved_keywords = {
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global',
            'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield'
        }
    
    def extract_features(self, code: str) -> Dict[str, Any]:
        """
        Извлечение признаков из кода
        
        Args:
            code: Код для анализа
            
        Returns:
            Словарь с признаками
        """
        try:
            tree = ast.parse(code)
        except:
            # Если код не парсится, возвращаем базовые признаки
            return self._extract_basic_features(code)
        
        features = {}
        
        # Базовые признаки
        features.update(self._extract_basic_features(code))
        
        # Структурные признаки
        features.update(self._extract_structural_features(tree))
        
        # Семантические признаки
        features.update(self._extract_semantic_features(tree, code))
        
        # Стилистические признаки
        features.update(self._extract_style_features(code))
        
        return features
    
    def _extract_basic_features(self, code: str) -> Dict[str, Any]:
        """
        Извлечение базовых статистических признаков кода
        
        Анализирует строковое представление кода и извлекает:
        - Общее количество строк
        - Количество непустых строк
        - Отношение пустых строк к общему числу
        - Среднюю и максимальную длину строки
        - Общий размер кода в символах
        
        Args:
            code: Исходный код в виде строки
            
        Returns:
            Словарь с базовыми признаками
        """
        lines = code.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        return {
            'total_lines': len(lines),
            'non_empty_lines': len(non_empty_lines),
            'empty_lines_ratio': (len(lines) - len(non_empty_lines)) / max(len(lines), 1),
            'avg_line_length': sum(len(line) for line in lines) / max(len(lines), 1),
            'max_line_length': max(len(line) for line in lines) if lines else 0,
            'file_size': len(code)
        }
    
    def _extract_structural_features(self, tree: ast.AST) -> Dict[str, Any]:
        """
        Извлечение структурных признаков кода из AST
        
        Анализирует абстрактное синтаксическое дерево и подсчитывает:
        - Количество функций и классов
        - Количество импортов
        - Количество циклов (for, while)
        - Количество условных операторов (if)
        - Максимальную глубину вложенности
        - Циклометрическую сложность
        
        Args:
            tree: AST-дерево кода
            
        Returns:
            Словарь со структурными признаками
        """
        features = {
            'functions_count': 0,
            'classes_count': 0,
            'imports_count': 0,
            'loops_count': 0,
            'conditionals_count': 0,
            'nested_depth': 0,
            'complexity_score': 0
        }
        
        # Подсчет различных элементов
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                features['functions_count'] += 1
            elif isinstance(node, ast.ClassDef):
                features['classes_count'] += 1
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                features['imports_count'] += 1
            elif isinstance(node, (ast.For, ast.While)):
                features['loops_count'] += 1
            elif isinstance(node, ast.If):
                features['conditionals_count'] += 1
        
        # Расчет сложности (циклометрическая сложность)
        features['complexity_score'] = self._calculate_cyclomatic_complexity(tree)
        
        # Расчет максимальной вложенности
        features['nested_depth'] = self._calculate_max_nesting(tree)
        
        return features
    
    def _extract_semantic_features(self, tree: ast.AST, code: str) -> Dict[str, Any]:
        """
        Извлечение семантических признаков кода
        
        Анализирует смысловое содержимое кода:
        - Количество переменных
        - Количество и типы вызовов функций (встроенные vs пользовательские)
        - Количество литералов (строковые, числовые)
        - Использование продвинутых конструкций (list comprehension, lambda)
        - Наличие обработки исключений
        - Наличие рекурсии
        
        Args:
            tree: AST-дерево кода
            code: Исходный код в виде строки
            
        Returns:
            Словарь с семантическими признаками
        """
        features = {
            'variable_count': 0,
            'function_calls_count': 0,
            'builtin_functions_count': 0,
            'user_functions_count': 0,
            'string_literals_count': 0,
            'numeric_literals_count': 0,
            'list_comprehensions_count': 0,
            'lambda_functions_count': 0,
            'exception_handling': False,
            'recursion_present': False
        }
        
        variables = set()
        function_calls = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                variables.add(node.id)
            elif isinstance(node, ast.Call):
                function_calls.append(node)
            elif isinstance(node, ast.ListComp):
                features['list_comprehensions_count'] += 1
            elif isinstance(node, ast.Lambda):
                features['lambda_functions_count'] += 1
            elif isinstance(node, (ast.Try, ast.ExceptHandler)):
                features['exception_handling'] = True
        
        features['variable_count'] = len(variables)
        features['function_calls_count'] = len(function_calls)
        
        # Анализ типов функций
        builtin_functions = {
            'print', 'len', 'range', 'enumerate', 'zip', 'map', 'filter',
            'sum', 'min', 'max', 'sorted', 'reversed', 'abs', 'round'
        }
        
        for call in function_calls:
            if isinstance(call.func, ast.Name):
                if call.func.id in builtin_functions:
                    features['builtin_functions_count'] += 1
                else:
                    features['user_functions_count'] += 1
        
        # Подсчет литералов
        for node in ast.walk(tree):
            if isinstance(node, ast.Str):
                features['string_literals_count'] += 1
            elif isinstance(node, ast.Num):
                features['numeric_literals_count'] += 1
        
        # Проверка на рекурсию
        features['recursion_present'] = self._detect_recursion(tree)
        
        return features
    
    def _extract_style_features(self, code: str) -> Dict[str, Any]:
        """
        Извлечение стилистических признаков кода
        
        Анализирует соответствие кода стилю PEP 8 и лучшим практикам:
        - Отношение комментариев к коду
        - Наличие docstring
        - Соблюдение соглашений именования (snake_case, PascalCase)
        - Консистентность отступов (4 пробела)
        - Правильное использование пустых строк
        
        Args:
            code: Исходный код в виде строки
            
        Returns:
            Словарь со стилистическими признаками
        """
        features = {
            'comment_ratio': 0.0,
            'docstring_present': False,
            'naming_convention_score': 0.0,
            'indentation_consistency': 0.0,
            'line_spacing_score': 0.0
        }
        
        lines = code.split('\n')
        
        # Анализ комментариев
        comment_lines = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
                comment_lines += 1
        
        features['comment_ratio'] = comment_lines / max(len(lines), 1)
        
        # Проверка наличия docstring
        features['docstring_present'] = '"""' in code or "'''" in code
        
        # Анализ соглашений именования
        features['naming_convention_score'] = self._analyze_naming_conventions(code)
        
        # Анализ отступов
        features['indentation_consistency'] = self._analyze_indentation(lines)
        
        # Анализ пробелов между строками
        features['line_spacing_score'] = self._analyze_line_spacing(lines)
        
        return features
    
    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """
        Расчет циклометрической сложности кода
        
        Вычисляет циклометрическую сложность по методу Маккейба.
        Базовая сложность = 1, увеличивается на 1 за каждую:
        - Условную конструкцию (if)
        - Цикл (for, while)
        - Обработчик исключений (except)
        - Логический оператор (and, or)
        
        Args:
            tree: AST-дерево кода
            
        Returns:
            Циклометрическая сложность (целое число)
        """
        complexity = 1  # Базовая сложность
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(node, (ast.And, ast.Or)):
                complexity += 1
        
        return complexity
    
    def _calculate_max_nesting(self, tree: ast.AST) -> int:
        """
        Расчет максимальной глубины вложенности кода
        
        Рекурсивно обходит AST и определяет максимальный уровень вложенности
        управляющих конструкций (if, for, while, try, with) и определений
        функций/классов.
        
        Args:
            tree: AST-дерево кода
            
        Returns:
            Максимальная глубина вложенности
        """
        def get_nesting_level(node, current_level=0):
            """
            Вспомогательная рекурсивная функция
            
            Args:
                node: Текущий узел AST
                current_level: Текущий уровень вложенности
                
            Returns:
                Максимальный уровень в поддереве
            """
            max_level = current_level
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.If, ast.For, ast.While, ast.Try, ast.With, ast.FunctionDef, ast.ClassDef)):
                    max_level = max(max_level, get_nesting_level(child, current_level + 1))
                else:
                    max_level = max(max_level, get_nesting_level(child, current_level))
            return max_level
        
        return get_nesting_level(tree)
    
    def _detect_recursion(self, tree: ast.AST) -> bool:
        """
        Обнаружение рекурсивных вызовов функций
        
        Анализирует AST и определяет, содержит ли код рекурсивные функции.
        Функция считается рекурсивной, если она вызывает саму себя.
        
        Args:
            tree: AST-дерево кода
            
        Returns:
            True если найдена хотя бы одна рекурсивная функция, False иначе
        """
        functions = {}
        
        # Сбор всех функций
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions[node.name] = node
        
        # Проверка вызовов функций внутри функций
        for func_name, func_node in functions.items():
            for node in ast.walk(func_node):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id == func_name:
                        return True
        
        return False
    
    def _analyze_naming_conventions(self, code: str) -> float:
        """
        Анализ соблюдения соглашений именования PEP 8
        
        Проверяет имена переменных, функций и констант на соответствие стандарту:
        - snake_case для переменных и функций (полный балл)
        - PascalCase для классов (половина балла, т.к. может быть переменная)
        - UPPER_CASE для констант (полный балл)
        
        Args:
            code: Исходный код в виде строки
            
        Returns:
            Оценка от 0.0 до 1.0 (доля правильно названных идентификаторов)
        """
        try:
            tree = ast.parse(code)
        except:
            return 0.0
        
        score = 0.0
        total_names = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                total_names += 1
                name = node.id
                
                # Проверка snake_case для переменных
                if isinstance(node.ctx, ast.Store) and not name.isupper():
                    if re.match(r'^[a-z_][a-z0-9_]*$', name):
                        score += 1.0
                    elif re.match(r'^[A-Z][a-zA-Z0-9]*$', name):
                        score += 0.5  # PascalCase тоже приемлем для классов
                
                # Проверка UPPER_CASE для констант
                elif name.isupper() and '_' in name:
                    score += 1.0
        
        return score / max(total_names, 1)
    
    def _analyze_indentation(self, lines: List[str]) -> float:
        """
        Анализ консистентности отступов в коде
        
        Проверяет соответствие отступов стандарту PEP 8 (4 пробела).
        Все отступы должны быть кратны 4 для максимальной оценки.
        
        Args:
            lines: Список строк кода
            
        Returns:
            1.0 если все отступы консистентны (кратны 4), 0.5 иначе, 
            1.0 для кода без отступов
        """
        if not lines:
            return 1.0
        
        indentations = []
        for line in lines:
            if line.strip():  # Пропускаем пустые строки
                indent = len(line) - len(line.lstrip())
                if indent > 0:
                    indentations.append(indent)
        
        if not indentations:
            return 1.0
        
        # Проверяем, что все отступы кратны 4 (стандарт Python)
        consistent = all(indent % 4 == 0 for indent in indentations)
        
        return 1.0 if consistent else 0.5
    
    def _analyze_line_spacing(self, lines: List[str]) -> float:
        """
        Анализ использования пустых строк между блоками кода
        
        Оценивает правильность использования пустых строк в соответствии с PEP 8.
        Хорошая практика - использовать пустые строки для разделения
        логических блоков кода, функций и классов.
        
        Args:
            lines: Список строк кода
            
        Returns:
            Оценка от 0.0 до 1.0 (доля строк с правильным окружением)
        """
        if len(lines) < 3:
            return 1.0
        
        # Подсчет пустых строк между непустыми
        spacing_score = 0.0
        non_empty_count = 0
        
        for i in range(1, len(lines) - 1):
            if lines[i].strip():  # Непустая строка
                non_empty_count += 1
                
                # Проверяем пробелы до и после
                prev_empty = not lines[i-1].strip()
                next_empty = not lines[i+1].strip()
                
                # Хорошая практика: пустые строки между функциями/классами
                if prev_empty or next_empty:
                    spacing_score += 1.0
        
        return spacing_score / max(non_empty_count, 1)
    
    def get_complexity_level(self, features: Dict[str, Any]) -> str:
        """
        Определение уровня сложности на основе признаков
        
        Args:
            features: Словарь с признаками
            
        Returns:
            Уровень сложности: 'easy', 'medium', 'hard'
        """
        complexity_score = features.get('complexity_score', 0)
        lines = features.get('total_lines', 0)
        functions = features.get('functions_count', 0)
        nesting = features.get('nested_depth', 0)
        
        # Простая эвристика для определения сложности
        if complexity_score <= 3 and lines <= 20 and functions <= 2 and nesting <= 2:
            return 'easy'
        elif complexity_score <= 8 and lines <= 50 and functions <= 5 and nesting <= 4:
            return 'medium'
        else:
            return 'hard'
    
    def generate_suggestions(self, features: Dict[str, Any]) -> List[str]:
        """
        Генерация предложений по улучшению кода
        
        Args:
            features: Словарь с признаками
            
        Returns:
            Список предложений
        """
        suggestions = []
        
        # Проверка сложности
        if features.get('complexity_score', 0) > 10:
            suggestions.append("Код имеет высокую циклометрическую сложность. Рассмотрите разбиение на более мелкие функции.")
        
        # Проверка длины функций
        if features.get('functions_count', 0) == 1 and features.get('total_lines', 0) > 30:
            suggestions.append("Функция слишком длинная. Разбейте её на более мелкие функции.")
        
        # Проверка комментариев
        if features.get('comment_ratio', 0) < 0.1:
            suggestions.append("Добавьте больше комментариев для улучшения читаемости кода.")
        
        # Проверка обработки ошибок
        if not features.get('exception_handling', False):
            suggestions.append("Рассмотрите добавление обработки исключений.")
        
        # Проверка соглашений именования
        if features.get('naming_convention_score', 0) < 0.7:
            suggestions.append("Улучшите соглашения именования переменных (используйте snake_case).")
        
        # Проверка вложенности
        if features.get('nested_depth', 0) > 4:
            suggestions.append("Уменьшите уровень вложенности кода.")
        
        return suggestions
