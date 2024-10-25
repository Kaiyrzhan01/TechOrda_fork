
# FastAPI Project

## Установка окружения

1. Создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запустите приложение:

```bash
python main.py
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

## Создание `.gitignore`

Создайте файл `.gitignore` и добавьте в него стандартные рекомендации для Python:

```plaintext
__pycache__/
*.pyc
*.pyo
.env
venv/
```

### Примечания

- Виртуальное окружение необходимо для изоляции зависимостей проекта.
- `requirements.txt` должен содержать все необходимые библиотеки для вашего приложения.
test
