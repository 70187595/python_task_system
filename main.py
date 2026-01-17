"""
Главный файл для запуска системы генерации и проверки заданий Python
"""

import os
import sys
from app import create_app

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Создаём приложение для production (gunicorn)
app = create_app()

def main():
    """
    Главная функция для запуска Flask веб-приложения
    
    Инициализирует и запускает веб-сервер с системой генерации
    и проверки заданий Python. Использует переменные окружения
    для конфигурации:
    - FLASK_DEBUG: включить/отключить режим отладки (по умолчанию True)
    - PORT: порт для запуска (по умолчанию 5000)
    - HOST: хост для прослушивания (по умолчанию 127.0.0.1)
    
    Обрабатывает прерывания (Ctrl+C) и ошибки запуска.
    """
    # Создание приложения
    app = create_app()
    
    # Настройки для разработки
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    
    print("=" * 60)
    print("Система генерации и проверки заданий Python")
    print("=" * 60)
    print(f"Веб-интерфейс: http://{host}:{port}")
    print(f"Режим отладки: {'Включен' if debug_mode else 'Отключен'}")
    print(f"Рабочая директория: {os.getcwd()}")
    print("=" * 60)
    print("Для остановки нажмите Ctrl+C")
    print("=" * 60)
    
    # Запуск приложения
    try:
        app.run(
            host=host,
            port=port,
            debug=debug_mode,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n\nПриложение остановлено пользователем")
    except Exception as e:
        print(f"\nОшибка запуска приложения: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
