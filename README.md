```markdown
# Crowdfunding Backend

This repository contains the backend code for the Crowdfunding Project, built with **Django** and **Django REST Framework**.  
It provides all API endpoints and business logic for managing users and crowdfunding campaigns.

---

## 📁 Project Structure
```

CROWDFUNDING_BACKEND/
├── campaigns/ # Django app for crowdfunding campaigns (models, views, serializers, etc.)
├── crowdfunding/ # Django project settings, URLs, and configuration
├── users/ # Django app for user management and authentication
├── .gitignore # Git ignore rules
├── ERD.drawio # Entity Relationship Diagram (ERD) for the database
├── manage.py # Django management script
├── README.md # Project documentation
└── requirements.txt # Python dependencies

````

### Responsibilities

- **campaigns/**: Handles all logic related to crowdfunding campaigns (CRUD operations, API endpoints, business logic).
- **users/**: Manages user registration, authentication, and profiles.
- **crowdfunding/**: Contains project-level configuration, settings, and URL routing.
- **ERD.drawio**: Visual documentation of the database schema.
- **requirements.txt**: Lists all Python packages required to run the backend.
- **.gitignore**: Specifies files and folders ignored by Git.
- **manage.py**: Used to run Django commands (server, migrations, etc.).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual environment tool (`venv` or `virtualenv`)
- Git

### Installation

1. **Clone the repository**
    ```
    git clone https://github.com/Mohamedelwali/crowdfunding_backend.git
    cd crowdfunding_backend
    ```

2. **Create and activate a virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Configure environment variables**
    - Create a `.env` file (if using [python-dotenv](https://pypi.org/project/python-dotenv/)) and add your Django secret key and database credentials.
    - Update `crowdfunding/settings.py` to read from `.env`.

5. **Apply migrations**
    ```
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access)**
    ```
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```
    python manage.py runserver
    ```

---

## 🛠️ Main Features

- User registration, login, and profile management (JWT authentication recommended)
- Create, read, update, and delete crowdfunding campaigns
- PostgreSQL database integration
- Django admin panel for data management
- RESTful API endpoints

---

## 🧪 Running Tests

````

python manage.py test

```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 📞 Contact

For questions or suggestions, contact:
**Mohamed Elwaly** – [mnoaman162@gmail.com]
**Ziad Ramzy** – [ziadramzy2@gmail.com]
**Hassan Amer** – [hassanamer46@gmail.com]
**Shimaa Nasser** – []
**Ahmed Mohamed Eid** – []

---

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
```
