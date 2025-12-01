"""
Модуль инициализации приложения для системы генерации и проверки заданий Python
"""

from flask import Flask
import os

def create_app():
    """Создание и настройка Flask приложения"""
    app = Flask(__name__)
    
    # Конфигурация
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['DATABASE'] = os.path.join(app.instance_path, 'tasks.db')
    
    # Создание папки для базы данных
    os.makedirs(app.instance_path, exist_ok=True)
    
    # Регистрация маршрутов
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
