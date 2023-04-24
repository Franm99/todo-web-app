# TODO Web App with Django

**Under development**

Simple ToDo web app with Django.

* Create your ToDo list.
* Add items to each ToDo element, with a description and due date.

## Installation

1. Clone the repository to your desired location.

```bash
C:\> git clone https://github.com/Franm99/todo-web-app.git
```

2. In the repository location, create a new environment (if not installed yet, install virtualenv with `pip install pirtualenv`).

```bash
C:\> python -m venv venv
```

3. Activate the virtual environment. 

**Windows**
```bash
C:\> venv\Scripts\activate.bat
(venv) C:\>
```
**Linux**
```bash
~$ source venv/bin/activate
(venv) ~$
```

4. Install all dependencies.

```bash
pip install -r requirements.txt
```

## How to run (developer mode)

1. Activate the virtual environment.

2. Migrate Django models to database.

```bash
(venv) C:\> python manage.py migrate
```
3. Run the Django server.

```bash
(venv) C:\> python manage.py runserver
# ...
# Starting development server at http://127.0.0.1:8000/
```
