#  Smartnotes Plus

Smartnotes Plus is a Django-based web application for creating, editing, organizing, and managing personal notes. It features rich-text editing using CKEditor and supports user authentication, tags, and public/private visibility.

##  Features

- User Registration & Login/Logout
- Create, Update, Delete, and View Notes
- CKEditor Integration for Rich Text Editing
- Tag Support (Optional/Customizable)
- Public or Private Notes
- PostgreSQL Database Support
- Bootstrap for Frontend Styling

##  Project Structure

```

smartnotes\_plus/
├── manage.py
├── smartnotes\_plus/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── notes/
│           ├── base.html
│           ├── login.html
│           ├── register.html
│           ├── note\_list.html
│           ├── note\_form.html
│           └── note\_confirm\_delete.html
└── db.sqlite3 or PostgreSQL

````

##  Tech Stack

- **Backend**: Django 5.2+
- **Database**: PostgreSQL / SQLite
- **Frontend**: Bootstrap 5
- **Rich Text Editor**: CKEditor 4
- **ORM**: Django ORM
- **Authentication**: Django Auth System

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smartnotes_plus.git
cd smartnotes_plus
````

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure `django`, `psycopg`, and `django-ckeditor` are in `requirements.txt`.

### 4. Configure PostgreSQL (optional)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smartnotes_db',
        'USER': 'alok_notes',
        'PASSWORD': 'Alok3007',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Ensure privileges in PostgreSQL:

```sql
GRANT ALL PRIVILEGES ON DATABASE smartnotes_db TO alok_notes;
GRANT ALL ON SCHEMA public TO alok_notes;
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Open your browser at: `http://127.0.0.1:8000`

---

##  License

This project is for learning/demo purposes. You are free to modify and use it.

---

##  Author

**Aloknath Tiwari**
Backend Developer | Django & FastAPI | Data Engineering Enthusiast
📧 [aloknathtiwari2000@gmail.com](mailto:aloknathtiwari2000gmail.com)


