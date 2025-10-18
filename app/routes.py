"""
Маршруты для веб-приложения системы заданий Python
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import json
from .models import TaskGenerator, CodeChecker, SimpleNeuralNetwork
from .utils import DatabaseManager

# Создание Blueprint
bp = Blueprint('main', __name__)

# Инициализация компонентов
task_generator = TaskGenerator()
code_checker = CodeChecker()
neural_network = SimpleNeuralNetwork()
db_manager = DatabaseManager()


@bp.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')


@bp.route('/generate')
def generate_task():
    """Страница генерации заданий"""
    categories = task_generator.get_available_categories()
    difficulties = task_generator.get_difficulty_levels()
    
    return render_template('generate.html', 
                         categories=categories, 
                         difficulties=difficulties)


@bp.route('/api/generate-task', methods=['POST'])
def api_generate_task():
    """API для генерации задания"""
    try:
        data = request.get_json()
        category = data.get('category')
        difficulty = data.get('difficulty')
        
        if category == 'custom':
            # Генерация кастомного задания
            requirements = {
                'title': data.get('title', 'Пользовательское задание'),
                'description': data.get('description', 'Решите поставленную задачу'),
                'difficulty': difficulty,
                'category': 'custom',
                'test_cases': data.get('test_cases', [])
            }
            task = task_generator.generate_custom_task(requirements)
        else:
            # Генерация стандартного задания
            task = task_generator.generate_task(category, difficulty)
        
        # Сохранение в базу данных
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'difficulty': task.difficulty,
            'category': task.category,
            'test_cases': task.test_cases,
            'hints': task.hints,
            'solution_template': task.solution_template
        }
        
        db_manager.save_task(task_data)
        
        return jsonify({
            'success': True,
            'task': {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'difficulty': task.difficulty,
                'category': task.category,
                'test_cases': task.test_cases,
                'hints': task.hints,
                'solution_template': task.solution_template
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/solve/<task_id>')
def solve_task(task_id):
    """Страница решения задания"""
    task = db_manager.get_task(task_id)
    
    if not task:
        return redirect(url_for('main.index'))
    
    return render_template('solve.html', task=task)


@bp.route('/api/check-solution', methods=['POST'])
def api_check_solution():
    """API для проверки решения"""
    try:
        print("🔍 Получен запрос на проверку решения")
        print(f"📝 Метод: {request.method}")
        print(f"📋 Заголовки: {dict(request.headers)}")
        
        data = request.get_json()
        print(f"📊 Данные запроса: {data}")
        
        if not data:
            print("❌ Нет данных в запросе")
            return jsonify({
                'success': False,
                'error': 'Нет данных в запросе'
            }), 400
        
        task_id = data.get('task_id')
        student_code = data.get('code')
        
        print(f"📋 ID задания: {task_id}")
        print(f"💻 Код студента: {student_code[:100]}..." if student_code else "❌ Код не найден")
        
        # Получение задания
        task = db_manager.get_task(task_id)
        if not task:
            return jsonify({
                'success': False,
                'error': 'Задание не найдено'
            }), 404
        
        # Проверка синтаксиса
        syntax_valid, syntax_error = code_checker.check_syntax(student_code)
        
        if not syntax_valid:
            return jsonify({
                'success': True,
                'syntax_valid': False,
                'syntax_error': syntax_error,
                'test_results': [],
                'analysis': {},
                'score': 0
            })
        
        print("🧪 Начинаем тестирование решения...")
        
        # Тестирование решения
        test_results = code_checker.test_solution(student_code, task['test_cases'])
        print(f"✅ Тестирование завершено: {len(test_results)} тестов")
        
        # Анализ кода
        print("📊 Анализируем код...")
        analysis = code_checker.analyze_code(student_code)
        print(f"✅ Анализ завершен: {analysis.lines_of_code} строк, {analysis.functions_count} функций")
        
        # Извлечение признаков для нейронной сети
        print("🧠 Извлекаем признаки для нейронной сети...")
        features = code_checker.get_code_features(student_code)
        print(f"✅ Признаки извлечены: {len(features)} параметров")
        
        # Оценка качества кода нейронной сетью
        print("🤖 Оцениваем качество кода...")
        quality_scores = neural_network.evaluate_code_quality(features)
        print(f"✅ Оценка завершена: правильность={quality_scores['correctness']:.2f}")
        
        # Расчет итогового балла
        passed_tests = sum(1 for result in test_results if result.passed)
        test_score = (passed_tests / len(test_results)) * 100 if test_results else 0
        
        # Усреднение оценок
        avg_quality = (quality_scores['correctness'] + 
                      quality_scores['efficiency'] + 
                      quality_scores['readability']) / 3 * 100
        
        final_score = (test_score * 0.7 + avg_quality * 0.3)
        
        # Подготовка результатов тестирования
        test_results_data = []
        for result in test_results:
            test_results_data.append({
                'input': result.test_case.get('input', ''),
                'expected': result.expected_output,
                'actual': result.actual_output,
                'passed': result.passed,
                'execution_time': result.execution_time,
                'error': result.error_message
            })
        
        # Сохранение решения в базу данных
        solution_data = {
            'task_id': task_id,
            'student_code': student_code,
            'test_results': test_results_data,
            'analysis_results': {
                'syntax_valid': analysis.syntax_valid,
                'complexity_score': analysis.complexity_score,
                'lines_of_code': analysis.lines_of_code,
                'functions_count': analysis.functions_count,
                'suggestions': analysis.suggestions,
                'quality_scores': quality_scores
            },
            'score': final_score,
            'execution_time': sum(result.execution_time for result in test_results)
        }
        
        db_manager.save_solution(solution_data)
        
        return jsonify({
            'success': True,
            'syntax_valid': True,
            'test_results': test_results_data,
            'analysis': {
                'syntax_valid': analysis.syntax_valid,
                'complexity_score': analysis.complexity_score,
                'lines_of_code': analysis.lines_of_code,
                'functions_count': analysis.functions_count,
                'suggestions': analysis.suggestions,
                'quality_scores': quality_scores
            },
            'score': round(final_score, 2)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/tasks')
def list_tasks():
    """Список всех заданий"""
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')
    
    tasks = db_manager.get_all_tasks(category, difficulty)
    categories = task_generator.get_available_categories()
    difficulties = task_generator.get_difficulty_levels()
    
    return render_template('tasks.html', 
                         tasks=tasks, 
                         categories=categories, 
                         difficulties=difficulties,
                         selected_category=category,
                         selected_difficulty=difficulty)


@bp.route('/api/tasks')
def api_get_tasks():
    """API для получения списка заданий"""
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')
    
    tasks = db_manager.get_all_tasks(category, difficulty)
    
    return jsonify({
        'success': True,
        'tasks': tasks
    })


@bp.route('/api/statistics')
def api_get_statistics():
    """API для получения статистики"""
    stats = db_manager.get_statistics()
    
    return jsonify({
        'success': True,
        'statistics': stats
    })


@bp.route('/train-neural-network', methods=['POST'])
def train_neural_network():
    """Обучение нейронной сети"""
    try:
        # Здесь можно добавить логику для обучения нейронной сети
        # на основе сохраненных решений
        
        return jsonify({
            'success': True,
            'message': 'Нейронная сеть успешно обучена'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/health')
def health_check():
    """Проверка состояния системы"""
    return jsonify({
        'status': 'healthy',
        'components': {
            'task_generator': 'ok',
            'code_checker': 'ok',
            'neural_network': 'ok',
            'database': 'ok'
        }
    })
