# Тестовое задание для PelidTeam

## Описание

Тестовое задание для стажировки backend-разработчика (Python, Junior+) от PelidTeam.
Это Django-проект с API для интерактивной карты.

**API эндпоинты:**
| Метод | URL                 | Описание                 |
| ----- | -----------------   | ------------------------ |
| GET   | /api/places/<id>/   | Детали конкретного места |
| GET   | /api/places.geojson | GeoJSON для карты        |

## Стек: 
- Python 3.12
- asgiref==3.10.0
- Django==5.2.7
- django-admin-sortable2==2.2.8
- django-tinymce==5.0.0
- pillow==12.0.0
- python-decouple==3.8
- sqlparse==0.5.3
- tzdata==2025.2

### 1. Клонирование репозитория

```bash
git clone https://github.com/RiozakiHideki/PelidTeam_test.git
cd Backend_Test_Assignment_PelidTeam
```

### 2. Создание виртуального окружения

```bash
python3 -m venv .venv
```

### 3. Активация виртуального окружения

* **macOS/Linux:**

```bash
source .venv/bin/activate
```

* **Windows (CMD):**

```cmd
.venv\Scripts\activate
```

* **Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Настройка базы данных

### 1. Применение миграций

```bash
python manage.py migrate
```

### 2. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Следуйте инструкциям для ввода имени пользователя, email и пароля.
Суперпользователь нужен для доступа к админ-панели: `http://127.0.0.1:8000/admin/`.


## Запуск
```bash
python manage.py runserver
```