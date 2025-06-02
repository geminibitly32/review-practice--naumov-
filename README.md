# 📁 Учебная практика: Ревьюирование программных модулей

## Тема: Создание и изучение возможностей репозитория проекта

Добро пожаловать в мой учебный репозиторий, созданный в рамках практики по ревьюированию программных модулей. Здесь я осваиваю базовые навыки работы с системой контроля версий **Git** и платформой **GitHub**, а также учуся анализировать историю изменений кода и структуру проектов.

---

## 🧩 Содержание проекта

| Папка / Файл       | Описание |
|--------------------|----------|
| `src/`             | Папка с исходным кодом |
| `src/calculator.py` | Пример простого скрипта на Python — калькулятор |
| `.gitignore`       | Файлы, игнорируемые Git (для Python) |
| `README.md`        | Основное описание проекта |
| `report.md`        | Отчет по анализу стороннего репозитория |

---

## 🛠 Используемые технологии

- Язык программирования: **Python**
- Система контроля версий: **Git**
- Хостинг репозиториев: **GitHub**

---

## ✅ Задачи выполнения практики

1. Создать личный репозиторий на GitHub.
2. Добавить необходимые файлы (`README.md`, `.gitignore`, `src/`, `report.md`).
3. Сделать минимум 5 коммитов с понятными сообщениями.
4. Проанализировать чужой репозиторий и написать отчёт в формате Markdown.
5. Изучить основные функции Git: коммиты, ветки, Pull Requests, Issues.

---

## 📚 Полезные ссылки

- [GitHub Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 
- [Python .gitignore шаблон](https://github.com/github/gitignore/blob/main/Python.gitignore) 
- [Awesome for Beginners — пример проекта для анализа](https://github.com/mungell/awesome-for-beginners) 

---

Вы можете клонировать этот репозиторий и изучить структуру:

```bash
git clone https://github.com/ваше_имя/review-practice-ai_student.git review-practice-naumov

---

#### 2. **.gitignore**
Скопируйте следующий текст в файл `.gitignore`:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.ini
*.dll

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so 0A may be unexpected
# e.g. spec file is needed in git
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# Environments
env/
venv/
ENV/
env.bak/
venv.bak/

# VS Code
.vscode/
