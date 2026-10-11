# 📝 Django Blog

A custom blog website built with **Django**, featuring a personalized dashboard for managing blog posts, categories, and users. The application leverages Django's backend capabilities alongside a responsive frontend built with HTML5, CSS3, JavaScript, and Bootstrap 5.

## 🚀 Technologies Used

### 🛠️ Deployment & Server

<p>
  <img src="https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" alt="Railway" />
  <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Gunicorn" />
  <img src="https://img.shields.io/badge/WhiteNoise-Static%20Files-blue?style=for-the-badge" alt="WhiteNoise" />
</p>

* **Railway** — Application hosting and deployment.
* **Gunicorn** — WSGI HTTP server for running the Django application.
* **WhiteNoise** — Serves static files in production.

### ⚙️ Backend

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
</p>

* **Django Core** — Handles application logic, authentication, database operations, and server-side functionality.

### 🗄️ Database

<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
</p>

* **PostgreSQL** — Relational database for deployment and production use.
* **SQLite** — Alternative database for local development.

### 🎨 Frontend

<p>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap 5" />
</p>

* **HTML5 & CSS3** — Page structure and styling.
* **JavaScript** — Client-side interactions and dynamic functionality.
* **Bootstrap 5** — Responsive layouts and UI components.

## ✨ Features

* 📰 **Blog Management** — Create and manage blog posts.
* 🗂️ **Dynamic Categories** — Organize blog posts using categories.
* 👤 **User Profile Management** — Manage user profile information.
* 💬 **Blog Comments** — Allow users to comment on blog posts.
* 🔖 **Save Favorite Blogs** — Bookmark blog posts for later reading.
* 📊 **Custom Dashboard** — Manage blog posts, categories, and users through a dedicated dashboard.
* 🔐 **Authentication & Access Control** — Support user authentication and controlled access to application features.

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Josh-Guarda/django_blog.git
cd django_blog
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Open `my_blog/settings.py` and configure your preferred database.

#### Option A: SQLite

SQLite can be used for local development without setting up a separate database server.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

#### Option B: PostgreSQL

For PostgreSQL, configure your database credentials in a `.env` file rather than hardcoding sensitive information in your source code.

Create a `.env` file in your project root:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Configure the database in `my_blog/settings.py` using `python-decouple`:

```python
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}
```

**Important:** Ensure that `python-decouple` and the appropriate PostgreSQL database adapter are installed and listed in `requirements.txt`. The `.env` file should be excluded from Git using `.gitignore`.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🌐 Deployment

The application is deployed on **Railway**, using Gunicorn to run Django and WhiteNoise to serve static files in production.

Deployment configuration may require environment variables for database credentials, Django settings, and other production-specific values.

## 👨‍💻 Author

**Josh Guarda**

* GitHub: [@Josh-Guarda](https://github.com/Josh-Guarda)

---

⭐ If you find this project interesting, feel free to explore the repository and check out its implementation.
