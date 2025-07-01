````markdown
🎯 Crowdfunding Backend

A backend system for a crowdfunding platform, built with Django and Django REST Framework.  
It provides secure APIs for managing users, campaigns, and administrative tasks.


📁 Project Structure

CROWDFUNDING_BACKEND/
├── campaigns/           # Campaign app (models, serializers, views)
├── users/               # User management & authentication
├── crowdfunding/        # Project settings and URLs
├── ERD.drawio           # Entity Relationship Diagram
├── manage.py            # Django CLI entry point
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignored files
└── README.md            # Project documentation
````

---

## 📦 Responsibilities by Folder

| Folder/File        | Responsibility                                         |
| ------------------ | ------------------------------------------------------ |
| `campaigns/`       | Crowdfunding campaign logic (CRUD, serializers, views) |
| `users/`           | User registration, JWT login, profile                  |
| `crowdfunding/`    | Django settings, app configs, URL routing              |
| `ERD.drawio`       | Database schema diagram                                |
| `manage.py`        | Django management commands                             |
| `requirements.txt` | Python packages list                                   |
| `.gitignore`       | Files/folders excluded from version control            |

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.8+
* PostgreSQL
* Git
* Virtual environment tool (`venv` or `virtualenv`)

---

### ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mohamedelwali/crowdfunding_backend.git
   cd crowdfunding_backend
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   * Create a `.env` file in the root directory.
   * Add your secret key and database settings.
   * Make sure `crowdfunding/settings.py` reads the `.env` file.

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

---

## 🛠️ Features

* 🔐 JWT-based authentication (register, login, profile)
* 📦 Campaign creation, listing, editing, and deletion
* 🗄️ PostgreSQL database integration
* 🧑‍💻 Django admin panel
* 📡 RESTful API architecture

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** your feature branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit** your changes

   ```bash
   git commit -m "Add new feature"
   ```
4. **Push** to GitHub

   ```bash
   git push origin feature/your-feature
   ```
5. **Open a Pull Request** 🚀

---

## 🛡️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📞 Contact

* **Mohamed Elwaly** – [mnoaman162@gmail.com](mailto:mnoaman162@gmail.com)
* **Ziad Ramzy** – [ziadramzy2@gmail.com](mailto:ziadramzy2@gmail.com)
* **Hassan Amer** – [hassanamer46@gmail.com](mailto:hassanamer46@gmail.com)
* **Shimaa Nasser** – *(Email not provided)*
* **Ahmed Mohamed Eid** – *(Email not provided)*

---

## 📚 References

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [PostgreSQL Docs](https://www.postgresql.org/docs/)

```
