# Python Task System - Deployment Guide

## Деплой на Render.com (Бесплатно)

### Шаг 1: Подготовка (СДЕЛАНО ✅)
- ✅ Создан `Procfile`
- ✅ Создан `render.yaml`
- ✅ Добавлен `gunicorn` в `requirements.txt`
- ✅ Обновлён `main.py` для production

### Шаг 2: Регистрация на Render.com

1. Перейдите: https://render.com
2. Нажмите **"Get Started"**
3. Зарегистрируйтесь через **GitHub** (рекомендуется)

### Шаг 3: Создание Web Service

1. В дашборде нажмите **"New +"** → **"Web Service"**
2. Подключите ваш GitHub репозиторий: `70187595/python_task_system`
3. Настройте параметры:
   - **Name**: `python-task-system`
   - **Region**: `Frankfurt (EU Central)` или ближайший
   - **Branch**: `master`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
4. Выберите **"Free"** план
5. Нажмите **"Create Web Service"**

### Шаг 4: Переменные окружения (Environment Variables)

Добавьте в Render:
```
FLASK_ENV=production
FLASK_DEBUG=False
PORT=10000
```

### Шаг 5: Деплой

- Render автоматически развернёт приложение
- Процесс займёт 5-10 минут
- После завершения получите URL: `https://python-task-system.onrender.com`

---

## Альтернатива: PythonAnywhere

### Шаг 1: Регистрация
1. Перейдите: https://www.pythonanywhere.com
2. Создайте **Beginner** аккаунт (бесплатно)

### Шаг 2: Загрузка проекта
```bash
git clone https://github.com/70187595/python_task_system.git
cd python_task_system
pip install --user -r requirements.txt
```

### Шаг 3: Настройка WSGI
В разделе **Web** создайте приложение и укажите:
```python
import sys
sys.path.append('/home/yourusername/python_task_system')

from main import app as application
```

---

## Альтернатива: Railway.app

1. Перейдите: https://railway.app
2. Войдите через GitHub
3. Нажмите **"New Project"** → **"Deploy from GitHub repo"**
4. Выберите `python_task_system`
5. Railway автоматически определит Python и развернёт проект

---

## Проблемы и решения

### matplotlib не работает на сервере
Добавьте в начало `app/models/neural_network.py`:
```python
import matplotlib
matplotlib.use('Agg')  # Для серверов без GUI
```

### База данных SQLite
- На Render используйте persistent disk (платно)
- Или перейдите на PostgreSQL (бесплатно на Render)

---

## Ваш проект готов к деплою! 🚀

Рекомендую **Render.com** - самый простой вариант.
