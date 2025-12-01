"""
Менеджер базы данных для системы заданий Python
"""

import sqlite3
import json
from typing import List, Dict, Any, Optional
from datetime import datetime


class DatabaseManager:
    """Менеджер базы данных SQLite"""
    
    def __init__(self, db_path: str = "tasks.db"):
        """
        Инициализация менеджера базы данных
        
        Args:
            db_path: Путь к файлу базы данных
        """
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Инициализация структуры базы данных"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Таблица заданий
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    category TEXT NOT NULL,
                    test_cases TEXT NOT NULL,
                    expected_output TEXT,
                    hints TEXT NOT NULL,
                    solution_template TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Таблица решений
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS solutions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    student_code TEXT NOT NULL,
                    test_results TEXT NOT NULL,
                    analysis_results TEXT NOT NULL,
                    score REAL NOT NULL,
                    execution_time REAL NOT NULL,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (task_id) REFERENCES tasks (id)
                )
            """)
            
            # Таблица пользователей (для будущего расширения)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
    
    def save_task(self, task_data: Dict[str, Any]) -> bool:
        """
        Сохранение задания в базу данных
        
        Args:
            task_data: Данные задания
            
        Returns:
            True если успешно сохранено
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    INSERT OR REPLACE INTO tasks 
                    (id, title, description, difficulty, category, test_cases, 
                     expected_output, hints, solution_template)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    task_data['id'],
                    task_data['title'],
                    task_data['description'],
                    task_data['difficulty'],
                    task_data['category'],
                    json.dumps(task_data['test_cases']),
                    task_data.get('expected_output', ''),
                    json.dumps(task_data['hints']),
                    task_data['solution_template']
                ))
                
                conn.commit()
                return True
        except Exception as e:
            print(f"Ошибка сохранения задания: {e}")
            return False
    
    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        """
        Получение задания по ID
        
        Args:
            task_id: ID задания
            
        Returns:
            Данные задания или None
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT id, title, description, difficulty, category, 
                           test_cases, expected_output, hints, solution_template, created_at
                    FROM tasks WHERE id = ?
                """, (task_id,))
                
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'title': row[1],
                        'description': row[2],
                        'difficulty': row[3],
                        'category': row[4],
                        'test_cases': json.loads(row[5]),
                        'expected_output': row[6],
                        'hints': json.loads(row[7]),
                        'solution_template': row[8],
                        'created_at': row[9]
                    }
                return None
        except Exception as e:
            print(f"Ошибка получения задания: {e}")
            return None
    
    def get_all_tasks(self, category: str = None, difficulty: str = None) -> List[Dict[str, Any]]:
        """
        Получение всех заданий с фильтрацией
        
        Args:
            category: Фильтр по категории
            difficulty: Фильтр по сложности
            
        Returns:
            Список заданий
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = """
                    SELECT id, title, description, difficulty, category, 
                           test_cases, expected_output, hints, solution_template, created_at
                    FROM tasks
                """
                params = []
                
                if category or difficulty:
                    conditions = []
                    if category:
                        conditions.append("category = ?")
                        params.append(category)
                    if difficulty:
                        conditions.append("difficulty = ?")
                        params.append(difficulty)
                    
                    query += " WHERE " + " AND ".join(conditions)
                
                query += " ORDER BY created_at DESC"
                
                cursor.execute(query, params)
                
                tasks = []
                for row in cursor.fetchall():
                    tasks.append({
                        'id': row[0],
                        'title': row[1],
                        'description': row[2],
                        'difficulty': row[3],
                        'category': row[4],
                        'test_cases': json.loads(row[5]),
                        'expected_output': row[6],
                        'hints': json.loads(row[7]),
                        'solution_template': row[8],
                        'created_at': row[9]
                    })
                
                return tasks
        except Exception as e:
            print(f"Ошибка получения заданий: {e}")
            return []
    
    def save_solution(self, solution_data: Dict[str, Any]) -> bool:
        """
        Сохранение решения в базу данных
        
        Args:
            solution_data: Данные решения
            
        Returns:
            True если успешно сохранено
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    INSERT INTO solutions 
                    (task_id, student_code, test_results, analysis_results, 
                     score, execution_time)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    solution_data['task_id'],
                    solution_data['student_code'],
                    json.dumps(solution_data['test_results']),
                    json.dumps(solution_data['analysis_results']),
                    solution_data['score'],
                    solution_data['execution_time']
                ))
                
                conn.commit()
                return True
        except Exception as e:
            print(f"Ошибка сохранения решения: {e}")
            return False
    
    def get_solutions(self, task_id: str = None) -> List[Dict[str, Any]]:
        """
        Получение решений
        
        Args:
            task_id: Фильтр по ID задания
            
        Returns:
            Список решений
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = """
                    SELECT id, task_id, student_code, test_results, 
                           analysis_results, score, execution_time, submitted_at
                    FROM solutions
                """
                params = []
                
                if task_id:
                    query += " WHERE task_id = ?"
                    params.append(task_id)
                
                query += " ORDER BY submitted_at DESC"
                
                cursor.execute(query, params)
                
                solutions = []
                for row in cursor.fetchall():
                    solutions.append({
                        'id': row[0],
                        'task_id': row[1],
                        'student_code': row[2],
                        'test_results': json.loads(row[3]),
                        'analysis_results': json.loads(row[4]),
                        'score': row[5],
                        'execution_time': row[6],
                        'submitted_at': row[7]
                    })
                
                return solutions
        except Exception as e:
            print(f"Ошибка получения решений: {e}")
            return []
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Получение статистики по базе данных
        
        Returns:
            Словарь со статистикой
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Количество заданий
                cursor.execute("SELECT COUNT(*) FROM tasks")
                total_tasks = cursor.fetchone()[0]
                
                # Количество решений
                cursor.execute("SELECT COUNT(*) FROM solutions")
                total_solutions = cursor.fetchone()[0]
                
                # Средняя оценка
                cursor.execute("SELECT AVG(score) FROM solutions")
                avg_score = cursor.fetchone()[0] or 0
                
                # Задания по категориям
                cursor.execute("""
                    SELECT category, COUNT(*) 
                    FROM tasks 
                    GROUP BY category
                """)
                tasks_by_category = dict(cursor.fetchall())
                
                # Задания по сложности
                cursor.execute("""
                    SELECT difficulty, COUNT(*) 
                    FROM tasks 
                    GROUP BY difficulty
                """)
                tasks_by_difficulty = dict(cursor.fetchall())
                
                return {
                    'total_tasks': total_tasks,
                    'total_solutions': total_solutions,
                    'average_score': round(avg_score, 2),
                    'tasks_by_category': tasks_by_category,
                    'tasks_by_difficulty': tasks_by_difficulty
                }
        except Exception as e:
            print(f"Ошибка получения статистики: {e}")
            return {}
    
    def delete_task(self, task_id: str) -> bool:
        """
        Удаление задания
        
        Args:
            task_id: ID задания
            
        Returns:
            True если успешно удалено
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Удаляем связанные решения
                cursor.execute("DELETE FROM solutions WHERE task_id = ?", (task_id,))
                
                # Удаляем задание
                cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
                
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Ошибка удаления задания: {e}")
            return False
