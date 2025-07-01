```markdown
# 🎯 Crowdfunding Backend

This repository contains the backend code for the **Crowdfunding Project**, built using **Django** and **Django REST Framework**.  
It provides API endpoints and core business logic for managing users and crowdfunding campaigns.

---

## 📁 Project Structure
```

CROWDFUNDING_BACKEND/
├── campaigns/ # App for crowdfunding campaign logic (models, views, serializers, etc.)
├── users/ # App for user management and authentication
├── crowdfunding/ # Project configuration, settings, URLs
├── ERD.drawio # Entity Relationship Diagram for the database
├── manage.py # Django management script
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # Project documentation

````

### 📦 Responsibilities

- `campaigns/` – Handles all logic related to crowdfunding campaigns (CRUD, APIs, business logic).
- `users/` – Manages user registration, authentication, and profile data.
- `crowdfunding/` – Root project folder with settings, environment config, and URLs.
- `ERD.drawio` – Database schema in visual format.
- `requirements.txt` – Lists all required Python packages.
- `.gitignore` – Files and folders excluded from Git versioning.
- `manage.py` – CLI tool for running Django commands.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual environment tool (`venv` or `virtualenv`)
- Git

### ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mohamedelwali/crowdfunding_backend.git
   cd crowdfunding_backend
````

````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   - Create a `.env` file if using [python-dotenv](https://pypi.org/project/python-dotenv/).
   - Add your secret key and DB credentials.
   - Ensure `crowdfunding/settings.py` reads from `.env`.

5. **Apply migrations**

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

- ✅ JWT-based user authentication (login, register, profile)
- ✅ Full CRUD for crowdfunding campaigns
- ✅ PostgreSQL database integration
- ✅ Admin panel via Django admin
- ✅ RESTful API endpoints

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create your feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

4. Push to your branch:

   ```bash
   git push origin feature/your-feature
   ```

5. Open a Pull Request.

---

## 🛡️ License

This project is licensed under the **MIT License**.

---

## 📞 Contact

For questions or suggestions, contact the team:

- **Mohamed Elwaly** – [mnoaman162@gmail.com](mailto:mnoaman162@gmail.com)
- **Ziad Ramzy** – [ziadramzy2@gmail.com](mailto:ziadramzy2@gmail.com)
- **Hassan Amer** – [hassanamer46@gmail.com](mailto:hassanamer46@gmail.com)
- **Shimaa Nasser** – _(email not provided)_
- **Ahmed Mohamed Eid** – _(email not provided)_

---

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

```

```
````
