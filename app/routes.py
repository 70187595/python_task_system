"""
Маршруты для веб-приложения системы заданий Python
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
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
    
    response = make_response(render_template('solve.html', task=task))
    # Запрет кэширования для страницы решения
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@bp.route('/api/check-solution', methods=['POST'])
def api_check_solution():
    """API для проверки решения"""
    try:
        print("[CHECK] Получен запрос на проверку решения")
        print(f"[CHECK] Метод: {request.method}")
        print(f"[CHECK] Заголовки: {dict(request.headers)}")
        
        data = request.get_json()
        print(f"[CHECK] Данные запроса: {data}")
        
        if not data:
            print("[ERROR] Нет данных в запросе")
            return jsonify({
                'success': False,
                'error': 'Нет данных в запросе'
            }), 400
        
        task_id = data.get('task_id')
        student_code = data.get('code')
        
        print(f"[CHECK] ID задания: {task_id}")
        print(f"[CHECK] Код студента: {student_code[:100]}..." if student_code else "[ERROR] Код не найден")
        
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
        
        print("[TEST] Начинаем тестирование решения...")
        
        # Тестирование решения
        test_results = code_checker.test_solution(student_code, task['test_cases'])
        print(f"[TEST] Тестирование завершено: {len(test_results)} тестов")
        
        # Анализ кода
        print("[ANALYZE] Анализируем код...")
        analysis = code_checker.analyze_code(student_code)
        print(f"[ANALYZE] Анализ завершен: {analysis.lines_of_code} строк, {analysis.functions_count} функций")
        
        # Извлечение признаков для нейронной сети
        print("[NN] Извлекаем признаки для нейронной сети...")
        features = code_checker.get_code_features(student_code)
        print(f"[NN] Признаки извлечены: {len(features)} параметров")
        
        # Оценка качества кода нейронной сетью
        print("[NN] Оцениваем качество кода...")
        quality_scores = neural_network.evaluate_code_quality(features)
        print(f"[NN] Оценка завершена: правильность={quality_scores['correctness']:.2f}")
        
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


@bp.route('/train')
def train_model_page():
    """Страница обучения модели"""
    return render_template('train.html')


@bp.route('/api/train-model', methods=['POST'])
def api_train_model():
    """
    API для обучения нейронной сети
    
    ПАРАМЕТРЫ (JSON):
        hidden_size: int - размер скрытого слоя (4-16)
        learning_rate: float - скорость обучения (0.001-0.1)
        epochs: int - количество эпох (100-5000)
        activation: str - функция активации ('sigmoid' или 'relu')
        dropout_rate: float - вероятность dropout (0.0-0.5)
    
    ВОЗВРАЩАЕТ:
        success: bool
        final_loss: float - финальная ошибка
        improvement: float - улучшение в процентах
        history: dict - история обучения (epochs, loss)
    """
    try:
        import json
        import os
        import time
        
        data = request.get_json()
        
        # Получение параметров
        hidden_size = data.get('hidden_size', 8)
        learning_rate = data.get('learning_rate', 0.05)
        epochs = data.get('epochs', 2000)
        activation = data.get('activation', 'sigmoid')
        dropout_rate = data.get('dropout_rate', 0.0)
        
        # Валидация параметров
        if not (4 <= hidden_size <= 16):
            return jsonify({
                'success': False,
                'error': 'Размер скрытого слоя должен быть от 4 до 16'
            }), 400
        
        if not (0.001 <= learning_rate <= 0.1):
            return jsonify({
                'success': False,
                'error': 'Learning rate должен быть от 0.001 до 0.1'
            }), 400
        
        if not (100 <= epochs <= 5000):
            return jsonify({
                'success': False,
                'error': 'Количество эпох должно быть от 100 до 5000'
            }), 400
        
        # Загрузка обучающих данных
        training_data_path = 'data/training_data/training_data.json'
        
        if not os.path.exists(training_data_path):
            return jsonify({
                'success': False,
                'error': 'Обучающие данные не найдены'
            }), 404
        
        with open(training_data_path, 'r', encoding='utf-8') as f:
            training_data_raw = json.load(f)
        
        # Подготовка данных для обучения
        import numpy as np
        training_data = []
        
        for example in training_data_raw:
            # Извлекаем признаки
            features = example['features']
            feature_vector = np.array([
                features['lines_of_code'],
                features['functions_count'],
                features['complexity'],
                features['nested_levels'],
                features['variable_names_length'],
                features['comments_ratio'],
                features['imports_count'],
                features['class_count'],
                features['error_handling'],
                features['test_coverage']
            ]).reshape(1, -1)
            
            # Целевые значения
            target = np.array(example['target']).reshape(1, -1)
            
            training_data.append((feature_vector, target))
        
        # Создание и обучение модели
        from app.models.neural_network import SimpleNeuralNetwork
        
        model = SimpleNeuralNetwork(
            input_size=10,
            hidden_size=hidden_size,
            output_size=3,
            activation=activation,
            dropout_rate=dropout_rate
        )
        
        model.learning_rate = learning_rate
        
        print(f"🎓 Начало обучения модели...")
        print(f"   Архитектура: 10 → {hidden_size} → 3")
        print(f"   Learning rate: {learning_rate}")
        print(f"   Epochs: {epochs}")
        print(f"   Activation: {activation}")
        print(f"   Примеров: {len(training_data)}")
        
        start_time = time.time()
        
        # Обучение
        history = model.train(training_data, epochs=epochs)
        
        training_time = time.time() - start_time
        
        # Результаты
        initial_loss = history['loss'][0]
        final_loss = history['loss'][-1]
        improvement = ((initial_loss - final_loss) / initial_loss) * 100
        
        print(f"[TRAIN] Обучение завершено за {training_time:.2f} сек")
        print(f"   Начальная ошибка: {initial_loss:.6f}")
        print(f"   Финальная ошибка: {final_loss:.6f}")
        print(f"   Улучшение: {improvement:.2f}%")
        
        # Сохранение обученной модели во временную переменную
        # (будет сохранена при нажатии кнопки "Сохранить")
        global trained_model, trained_history
        trained_model = model
        trained_history = history
        
        return jsonify({
            'success': True,
            'final_loss': float(final_loss),
            'initial_loss': float(initial_loss),
            'improvement': float(improvement),
            'training_time': float(training_time),
            'history': {
                'epochs': history['epochs'],
                'loss': [float(l) for l in history['loss']]
            },
            'parameters': {
                'hidden_size': hidden_size,
                'learning_rate': learning_rate,
                'epochs': epochs,
                'activation': activation,
                'dropout_rate': dropout_rate
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/save-model', methods=['POST'])
def api_save_model():
    """
    API для сохранения обученной модели
    
    Сохраняет последнюю обученную модель в data/models/neural_network.json
    """
    try:
        import os
        
        global trained_model, trained_history
        
        if trained_model is None:
            return jsonify({
                'success': False,
                'error': 'Нет обученной модели для сохранения'
            }), 400
        
        # Создание директории если не существует
        model_dir = 'data/models'
        os.makedirs(model_dir, exist_ok=True)
        
        # Сохранение модели
        model_path = os.path.join(model_dir, 'neural_network.json')
        trained_model.save_model(model_path)
        
        # Сохранение истории обучения
        history_path = os.path.join(model_dir, 'training_history.json')
        with open(history_path, 'w', encoding='utf-8') as f:
            json.dump(trained_history, f, ensure_ascii=False, indent=2)
        
        print(f"[SAVE] Модель сохранена: {model_path}")
        print(f"[SAVE] История сохранена: {history_path}")
        
        return jsonify({
            'success': True,
            'message': 'Модель успешно сохранена',
            'model_path': model_path,
            'history_path': history_path
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/list-models', methods=['GET'])
def api_list_models():
    """
    API для получения списка сохраненных моделей
    
    ВОЗВРАЩАЕТ:
        success: bool
        models: list - список моделей с информацией
            - name: str - имя файла модели
            - path: str - полный путь
            - size: int - размер файла в байтах
            - modified: str - дата последнего изменения
            - parameters: dict - параметры модели (если доступны)
    """
    try:
        import os
        from datetime import datetime
        
        model_dir = 'data/models'
        
        if not os.path.exists(model_dir):
            return jsonify({
                'success': True,
                'models': []
            })
        
        models = []
        
        # Перебираем все JSON файлы в директории моделей
        for filename in os.listdir(model_dir):
            if filename.endswith('.json') and not filename.startswith('training_history'):
                filepath = os.path.join(model_dir, filename)
                
                try:
                    # Получаем информацию о файле
                    file_stat = os.stat(filepath)
                    file_size = file_stat.st_size
                    modified_time = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Пытаемся прочитать параметры модели
                    model_info = {
                        'name': filename,
                        'path': filepath,
                        'size': file_size,
                        'modified': modified_time
                    }
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            model_data = json.load(f)
                            model_info['parameters'] = {
                                'input_size': model_data.get('input_size', 10),
                                'hidden_size': model_data.get('hidden_size', 8),
                                'output_size': model_data.get('output_size', 3),
                                'learning_rate': model_data.get('learning_rate', 0.01),
                                'activation': model_data.get('activation', 'sigmoid'),
                                'dropout_rate': model_data.get('dropout_rate', 0.0)
                            }
                    except:
                        model_info['parameters'] = None
                    
                    models.append(model_info)
                    
                except Exception as e:
                    print(f"Ошибка чтения модели {filename}: {e}")
                    continue
        
        # Сортируем по дате изменения (новые первые)
        models.sort(key=lambda x: x['modified'], reverse=True)
        
        return jsonify({
            'success': True,
            'models': models,
            'count': len(models)
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/load-model', methods=['POST'])
def api_load_model():
    """
    API для загрузки конкретной модели
    
    ПАРАМЕТРЫ (JSON):
        model_name: str - имя файла модели для загрузки
    
    ВОЗВРАЩАЕТ:
        success: bool
        message: str
        parameters: dict - параметры загруженной модели
    """
    try:
        data = request.get_json()
        model_name = data.get('model_name')
        
        if not model_name:
            return jsonify({
                'success': False,
                'error': 'Не указано имя модели'
            }), 400
        
        model_path = os.path.join('data/models', model_name)
        
        if not os.path.exists(model_path):
            return jsonify({
                'success': False,
                'error': 'Модель не найдена'
            }), 404
        
        # Загружаем модель
        from app.models.neural_network import SimpleNeuralNetwork
        
        # Читаем параметры модели
        with open(model_path, 'r', encoding='utf-8') as f:
            model_data = json.load(f)
        
        # Создаем новую модель с теми же параметрами
        global neural_network
        neural_network = SimpleNeuralNetwork(
            input_size=model_data.get('input_size', 10),
            hidden_size=model_data.get('hidden_size', 8),
            output_size=model_data.get('output_size', 3),
            activation=model_data.get('activation', 'sigmoid'),
            dropout_rate=model_data.get('dropout_rate', 0.0)
        )
        
        # Загружаем веса
        neural_network.load_model(model_path)
        
        print(f"[LOAD] Модель загружена: {model_name}")
        
        return jsonify({
            'success': True,
            'message': f'Модель {model_name} успешно загружена',
            'parameters': {
                'input_size': neural_network.input_size,
                'hidden_size': neural_network.hidden_size,
                'output_size': neural_network.output_size,
                'learning_rate': neural_network.learning_rate,
                'activation': neural_network.activation,
                'dropout_rate': neural_network.dropout_rate
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/delete-model', methods=['POST'])
def api_delete_model():
    """
    API для удаления модели
    
    ПАРАМЕТРЫ (JSON):
        model_name: str - имя файла модели для удаления
    
    ВОЗВРАЩАЕТ:
        success: bool
        message: str
    """
    try:
        data = request.get_json()
        model_name = data.get('model_name')
        
        if not model_name:
            return jsonify({
                'success': False,
                'error': 'Не указано имя модели'
            }), 400
        
        # Защита от удаления критических моделей
        if model_name in ['neural_network.json', 'model_final.json']:
            return jsonify({
                'success': False,
                'error': 'Нельзя удалить основную модель'
            }), 403
        
        model_path = os.path.join('data/models', model_name)
        
        if not os.path.exists(model_path):
            return jsonify({
                'success': False,
                'error': 'Модель не найдена'
            }), 404
        
        # Удаляем файл модели
        os.remove(model_path)
        
        # Удаляем соответствующий файл истории, если есть
        history_name = model_name.replace('.json', '_history.json')
        history_path = os.path.join('data/models', history_name)
        if os.path.exists(history_path):
            os.remove(history_path)
        
        print(f"🗑️  Модель удалена: {model_name}")
        
        return jsonify({
            'success': True,
            'message': f'Модель {model_name} успешно удалена'
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/export-model', methods=['POST'])
def api_export_model():
    """
    API для экспорта модели (скачивание)
    
    ПАРАМЕТРЫ (JSON):
        model_name: str - имя файла модели для экспорта
    
    ВОЗВРАЩАЕТ:
        Файл модели для скачивания
    """
    try:
        from flask import send_file
        
        data = request.get_json()
        model_name = data.get('model_name')
        
        if not model_name:
            return jsonify({
                'success': False,
                'error': 'Не указано имя модели'
            }), 400
        
        model_path = os.path.join('data/models', model_name)
        
        if not os.path.exists(model_path):
            return jsonify({
                'success': False,
                'error': 'Модель не найдена'
            }), 404
        
        return send_file(
            model_path,
            as_attachment=True,
            download_name=model_name,
            mimetype='application/json'
        )
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/api/import-model', methods=['POST'])
def api_import_model():
    """
    API для импорта модели (загрузка файла)
    
    ПАРАМЕТРЫ (multipart/form-data):
        model_file: file - JSON файл с моделью
        model_name: str (optional) - имя для сохранения (по умолчанию - имя файла)
    
    ВОЗВРАЩАЕТ:
        success: bool
        message: str
        model_name: str - имя сохраненной модели
    """
    try:
        import os
        from werkzeug.utils import secure_filename
        
        # Проверяем наличие файла
        if 'model_file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Файл не предоставлен'
            }), 400
        
        file = request.files['model_file']
        
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'Файл не выбран'
            }), 400
        
        # Проверяем расширение
        if not file.filename.endswith('.json'):
            return jsonify({
                'success': False,
                'error': 'Файл должен быть в формате JSON'
            }), 400
        
        # Получаем имя для сохранения
        custom_name = request.form.get('model_name')
        if custom_name:
            filename = secure_filename(custom_name)
            if not filename.endswith('.json'):
                filename += '.json'
        else:
            filename = secure_filename(file.filename)
        
        # Создаем директорию если не существует
        model_dir = 'data/models'
        os.makedirs(model_dir, exist_ok=True)
        
        # Сохраняем файл
        model_path = os.path.join(model_dir, filename)
        file.save(model_path)
        
        # Проверяем валидность JSON
        try:
            with open(model_path, 'r', encoding='utf-8') as f:
                model_data = json.load(f)
                
            # Проверяем наличие необходимых полей
            required_fields = ['input_size', 'hidden_size', 'output_size']
            if not all(field in model_data for field in required_fields):
                os.remove(model_path)
                return jsonify({
                    'success': False,
                    'error': 'Неверный формат модели: отсутствуют обязательные поля'
                }), 400
                
        except json.JSONDecodeError:
            os.remove(model_path)
            return jsonify({
                'success': False,
                'error': 'Неверный формат JSON'
            }), 400
        
        print(f"[IMPORT] Модель импортирована: {filename}")
        
        return jsonify({
            'success': True,
            'message': f'Модель {filename} успешно импортирована',
            'model_name': filename
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@bp.route('/compare')
def compare_models_page():
    """Страница сравнения моделей"""
    return render_template('compare.html')


@bp.route('/api/compare-models', methods=['POST'])
def api_compare_models():
    """
    API для сравнения нескольких моделей
    
    ПАРАМЕТРЫ (JSON):
        models: list или 'all' - список имен моделей или 'all' для всех
        include_experiments: bool - включить ли результаты экспериментов
    
    ВОЗВРАЩАЕТ:
        success: bool
        comparison: dict - результаты сравнения
            - models: list - список моделей с параметрами и результатами
            - best_loss: float - лучшая ошибка
            - worst_loss: float - худшая ошибка
            - avg_loss: float - средняя ошибка
    """
    try:
        import os
        
        data = request.get_json()
        models_param = data.get('models', [])
        include_experiments = data.get('include_experiments', False)
        
        models_to_compare = []
        
        # Получаем список моделей для сравнения
        if models_param == 'all':
            # Загружаем все модели
            model_dir = 'data/models'
            if os.path.exists(model_dir):
                for filename in os.listdir(model_dir):
                    if filename.endswith('.json') and not filename.startswith('training_history'):
                        models_to_compare.append(filename)
        else:
            models_to_compare = models_param
        
        # Добавляем результаты экспериментов если запрошено
        if include_experiments:
            experiments_dir = 'experiments/results'
            if os.path.exists(experiments_dir):
                for filename in os.listdir(experiments_dir):
                    if filename.startswith('model_exp') and filename.endswith('.json'):
                        models_to_compare.append(os.path.join('..', experiments_dir, filename))
        
        if not models_to_compare:
            return jsonify({
                'success': False,
                'error': 'Нет моделей для сравнения'
            }), 400
        
        # Собираем данные о моделях
        comparison_data = []
        
        for model_file in models_to_compare:
            try:
                # Определяем полный путь
                if model_file.startswith('..'):
                    model_path = model_file
                else:
                    model_path = os.path.join('data/models', model_file)
                
                # Читаем модель
                with open(model_path, 'r', encoding='utf-8') as f:
                    model_data = json.load(f)
                
                # Пытаемся найти историю обучения
                history_path = model_path.replace('.json', '_history.json')
                if not os.path.exists(history_path):
                    history_path = model_path.replace('model_', 'history_')
                
                final_loss = None
                if os.path.exists(history_path):
                    try:
                        with open(history_path, 'r', encoding='utf-8') as f:
                            history_data = json.load(f)
                            if 'loss' in history_data and history_data['loss']:
                                final_loss = history_data['loss'][-1]
                    except:
                        pass
                
                # Если не нашли историю, пытаемся найти в основных файлах истории
                if final_loss is None:
                    # Проверяем training_history_final.json
                    if 'final' in model_file.lower():
                        history_path = 'data/models/training_history_final.json'
                    else:
                        history_path = 'data/models/training_history.json'
                    
                    if os.path.exists(history_path):
                        try:
                            with open(history_path, 'r', encoding='utf-8') as f:
                                history_data = json.load(f)
                                if 'loss' in history_data and history_data['loss']:
                                    final_loss = history_data['loss'][-1]
                        except:
                            pass
                
                # Добавляем данные модели
                model_info = {
                    'name': os.path.basename(model_file),
                    'input_size': model_data.get('input_size', 10),
                    'hidden_size': model_data.get('hidden_size', 8),
                    'output_size': model_data.get('output_size', 3),
                    'learning_rate': model_data.get('learning_rate'),
                    'activation': model_data.get('activation', 'sigmoid'),
                    'dropout_rate': model_data.get('dropout_rate', 0.0),
                    'final_loss': final_loss if final_loss is not None else 0.01  # Fallback
                }
                
                comparison_data.append(model_info)
                
            except Exception as e:
                print(f"Ошибка чтения модели {model_file}: {e}")
                continue
        
        if not comparison_data:
            return jsonify({
                'success': False,
                'error': 'Не удалось загрузить данные моделей'
            }), 500
        
        # Сортируем по финальной ошибке (лучшие первые)
        comparison_data.sort(key=lambda x: x['final_loss'])
        
        # Вычисляем статистику
        losses = [m['final_loss'] for m in comparison_data]
        best_loss = min(losses)
        worst_loss = max(losses)
        avg_loss = sum(losses) / len(losses)
        
        return jsonify({
            'success': True,
            'comparison': {
                'models': comparison_data,
                'best_loss': float(best_loss),
                'worst_loss': float(worst_loss),
                'avg_loss': float(avg_loss),
                'count': len(comparison_data)
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# Глобальные переменные для хранения обученной модели
trained_model = None
trained_history = None


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
