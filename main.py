"""
Главный файл для запуска системы генерации и проверки заданий Python
"""

import os
import sys
from app import create_app

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Главная функция для запуска приложения"""
    # Создание приложения
    app = create_app()
    
    # Настройки для разработки
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    
    print("=" * 60)
    print("🐍 Система генерации и проверки заданий Python")
    print("=" * 60)
    print(f"🌐 Веб-интерфейс: http://{host}:{port}")
    print(f"🔧 Режим отладки: {'Включен' if debug_mode else 'Отключен'}")
    print(f"📁 Рабочая директория: {os.getcwd()}")
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
        print("\n\n👋 Приложение остановлено пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка запуска приложения: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
