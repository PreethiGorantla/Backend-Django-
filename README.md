# Backend-Django

A Django-based backend project implementing CRUD operations, user authentication, and REST API functionality.

---

## 🚀 Features

- User Registration
- User Login & Logout
- Patient Management (CRUD Operations)
- Django Forms
- Django Templates
- REST API using Django REST Framework
- Model Serializers
- Basic Authentication Handling

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite3
- HTML Templates

---

## 📂 Project Structure

Backend-Django/
│
├── main/                 # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   ├── api_urls.py
│   └── templates/
│
├── myapp/                # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── .gitignore

---

## ⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/PreethiGorantla/Backend-Django-.git
cd Backend-Django-

2️⃣ Create Virtual Environment

python -m venv venv
Activate:
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install django
for REST Framework
pip install django djangorestframework

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Run Server
python manage.py runserver

📌 API Endpoints

/api/ – API root
/add/ – Add patient
/update/<id>/ – Update patient
/login/ – User login
/register/ – User registration

📖 What I Learned

Django Project Structure
Models & Migrations
Forms Handling
Template Rendering
Authentication System
REST API Development
Git & GitHub Version Control
