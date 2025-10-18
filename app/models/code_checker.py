"""
Система проверки и анализа кода Python
"""

import ast
import subprocess
import tempfile
import os
import sys
import time
import re
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum


class CheckResult(Enum):
    """Результаты проверки кода"""
    SUCCESS = "success"
    SYNTAX_ERROR = "syntax_error"
    RUNTIME_ERROR = "runtime_error"
    TIMEOUT = "timeout"
    WRONG_OUTPUT = "wrong_output"
    SECURITY_VIOLATION = "security_violation"


@dataclass
class TestResult:
    """Результат тестирования"""
    test_case: Dict[str, Any]
    passed: bool
    actual_output: str
    expected_output: str
    execution_time: float
    error_message: str = ""


@dataclass
class CodeAnalysis:
    """Анализ кода"""
    syntax_valid: bool
    complexity_score: float
    lines_of_code: int
    functions_count: int
    classes_count: int
    imports_count: int
    comments_ratio: float
    variable_names_length: float
    nested_levels: int
    error_handling: bool
    suggestions: List[str]


class CodeChecker:
    """Система проверки кода Python"""
    
    def __init__(self, timeout: int = 5):
        """
        Инициализация проверщика кода
        
        Args:
            timeout: Таймаут выполнения кода в секундах
        """
        self.timeout = timeout
        self.forbidden_imports = [
            'os', 'sys', 'subprocess', 'eval', 'exec', 'compile',
            'open', 'file', 'input', 'raw_input', '__import__'
        ]
        self.forbidden_functions = [
            'eval', 'exec', 'compile', 'open', 'file'
        ]
    
    def check_syntax(self, code: str) -> Tuple[bool, str]:
        """
        Проверка синтаксиса кода
        
        Args:
            code: Код для проверки
            
        Returns:
            Кортеж (валидность, сообщение об ошибке)
        """
        try:
            ast.parse(code)
            return True, ""
        except SyntaxError as e:
            return False, f"Синтаксическая ошибка: {e.msg} в строке {e.lineno}"
        except Exception as e:
            return False, f"Ошибка анализа: {str(e)}"
    
    def check_security(self, code: str) -> Tuple[bool, List[str]]:
        """
        Проверка безопасности кода
        
        Args:
            code: Код для проверки
            
        Returns:
            Кортеж (безопасность, список нарушений)
        """
        violations = []
        
        # Проверка на запрещенные импорты
        for forbidden in self.forbidden_imports:
            if f"import {forbidden}" in code or f"from {forbidden}" in code:
                violations.append(f"Запрещенный импорт: {forbidden}")
        
        # Проверка на запрещенные функции
        for forbidden in self.forbidden_functions:
            if forbidden in code:
                violations.append(f"Запрещенная функция: {forbidden}")
        
        # Проверка на exec и eval
        if 'exec(' in code or 'eval(' in code:
            violations.append("Использование exec() или eval() запрещено")
        
        return len(violations) == 0, violations
    
    def run_code(self, code: str, input_data: str = "") -> Tuple[bool, str, float, str]:
        """
        Безопасное выполнение кода
        
        Args:
            code: Код для выполнения
            input_data: Входные данные
            
        Returns:
            Кортеж (успех, результат, время выполнения, ошибка)
        """
        # Проверка безопасности
        is_safe, violations = self.check_security(code)
        if not is_safe:
            return False, "", 0.0, f"Нарушения безопасности: {', '.join(violations)}"
        
        # Создание временного файла
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            # Подготовка команды
            cmd = [sys.executable, temp_file]
            
            # Запуск с таймаутом
            start_time = time.time()
            result = subprocess.run(
                cmd,
                input=input_data,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                return True, result.stdout.strip(), execution_time, ""
            else:
                return False, "", execution_time, result.stderr.strip()
                
        except subprocess.TimeoutExpired:
            return False, "", self.timeout, "Превышено время выполнения"
        except Exception as e:
            return False, "", 0.0, f"Ошибка выполнения: {str(e)}"
        finally:
            # Удаление временного файла
            try:
                os.unlink(temp_file)
            except:
                pass
    
    def test_solution(self, code: str, test_cases: List[Dict[str, Any]]) -> List[TestResult]:
        """
        Тестирование решения
        
        Args:
            code: Код решения
            test_cases: Список тестовых случаев
            
        Returns:
            Список результатов тестирования
        """
        results = []
        
        for test_case in test_cases:
            input_data = str(test_case.get('input', ''))
            expected = str(test_case.get('expected', ''))
            
            # Создаем тестовый код
            test_code = f"""
{code}

# Тестирование
try:
    result = None
    if 'find_max' in globals():
        result = find_max({input_data})
    elif 'count_words' in globals():
        result = count_words("{input_data}")
    elif 'sort_list' in globals():
        result = sort_list({input_data})
    elif 'fibonacci' in globals():
        result = fibonacci({input_data})
    else:
        # Попробуем выполнить код напрямую
        exec('result = ' + repr({input_data}))
    
    print(result)
except Exception as e:
    print(f"Ошибка: {{e}}")
"""
            
            # Выполнение кода
            success, output, execution_time, error = self.run_code(test_code)
            
            # Очистка вывода
            if success:
                output = output.strip()
                # Убираем "Ошибка: " если есть
                if output.startswith("Ошибка: "):
                    success = False
                    error = output
                    output = ""
            
            # Проверка результата
            passed = success and str(output) == str(expected)
            
            result = TestResult(
                test_case=test_case,
                passed=passed,
                actual_output=output,
                expected_output=expected,
                execution_time=execution_time,
                error_message=error if not success else ""
            )
            
            results.append(result)
        
        return results
    
    def analyze_code(self, code: str) -> CodeAnalysis:
        """
        Анализ качества кода
        
        Args:
            code: Код для анализа
            
        Returns:
            Объект анализа кода
        """
        try:
            tree = ast.parse(code)
        except:
            return CodeAnalysis(
                syntax_valid=False,
                complexity_score=0.0,
                lines_of_code=len(code.splitlines()),
                functions_count=0,
                classes_count=0,
                imports_count=0,
                comments_ratio=0.0,
                variable_names_length=0.0,
                nested_levels=0,
                error_handling=False,
                suggestions=[]
            )
        
        # Подсчет различных элементов
        lines_of_code = len(code.splitlines())
        functions_count = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        classes_count = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
        imports_count = len([node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))])
        
        # Подсчет комментариев
        comment_lines = len([line for line in code.splitlines() if line.strip().startswith('#')])
        comments_ratio = comment_lines / lines_of_code if lines_of_code > 0 else 0.0
        
        # Анализ имен переменных
        variable_names = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
        variable_names_length = sum(len(name) for name in variable_names) / len(variable_names) if variable_names else 0.0
        
        # Анализ вложенности
        max_nested_level = self._calculate_nesting_level(tree)
        
        # Проверка обработки ошибок
        error_handling = any(isinstance(node, (ast.Try, ast.ExceptHandler)) for node in ast.walk(tree))
        
        # Расчет сложности
        complexity_score = self._calculate_complexity(tree)
        
        # Генерация предложений
        suggestions = self._generate_suggestions(code, tree)
        
        return CodeAnalysis(
            syntax_valid=True,
            complexity_score=complexity_score,
            lines_of_code=lines_of_code,
            functions_count=functions_count,
            classes_count=classes_count,
            imports_count=imports_count,
            comments_ratio=comments_ratio,
            variable_names_length=variable_names_length,
            nested_levels=max_nested_level,
            error_handling=error_handling,
            suggestions=suggestions
        )
    
    def _calculate_nesting_level(self, tree: ast.AST) -> int:
        """Расчет максимального уровня вложенности"""
        def get_nesting_level(node, current_level=0):
            max_level = current_level
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
                    max_level = max(max_level, get_nesting_level(child, current_level + 1))
                else:
                    max_level = max(max_level, get_nesting_level(child, current_level))
            return max_level
        
        return get_nesting_level(tree)
    
    def _calculate_complexity(self, tree: ast.AST) -> float:
        """Расчет сложности кода"""
        complexity = 0
        
        # Циклометрическая сложность
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(node, (ast.And, ast.Or)):
                complexity += 1
        
        # Нормализация
        lines = len([node for node in ast.walk(tree) if hasattr(node, 'lineno')])
        return complexity / max(lines, 1) if lines > 0 else 0
    
    def _generate_suggestions(self, code: str, tree: ast.AST) -> List[str]:
        """Генерация предложений по улучшению кода"""
        suggestions = []
        
        # Проверка длины функций
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:
                    suggestions.append(f"Функция '{node.name}' слишком длинная. Рассмотрите разбиение на более мелкие функции.")
        
        # Проверка имен переменных
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if len(node.id) < 3:
                    suggestions.append(f"Переменная '{node.id}' имеет слишком короткое имя.")
        
        # Проверка комментариев
        if self._calculate_complexity(tree) > 0.5:
            suggestions.append("Код имеет высокую сложность. Добавьте комментарии для улучшения читаемости.")
        
        # Проверка обработки ошибок
        if not any(isinstance(node, (ast.Try, ast.ExceptHandler)) for node in ast.walk(tree)):
            suggestions.append("Рассмотрите добавление обработки ошибок.")
        
        return suggestions
    
    def get_code_features(self, code: str) -> Dict[str, float]:
        """
        Извлечение признаков кода для нейронной сети
        
        Args:
            code: Код для анализа
            
        Returns:
            Словарь с признаками
        """
        analysis = self.analyze_code(code)
        
        return {
            'lines_of_code': float(analysis.lines_of_code),
            'functions_count': float(analysis.functions_count),
            'complexity': analysis.complexity_score,
            'nested_levels': float(analysis.nested_levels),
            'variable_names_length': analysis.variable_names_length,
            'comments_ratio': analysis.comments_ratio,
            'imports_count': float(analysis.imports_count),
            'class_count': float(analysis.classes_count),
            'error_handling': 1.0 if analysis.error_handling else 0.0,
            'test_coverage': 0.0  # Пока не реализовано
        }
