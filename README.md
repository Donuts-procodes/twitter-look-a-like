# 🐦 **Twitter Look-a-Like**

> A sleek Twitter-inspired web app built using **Flask (Python)** for the backend and **React + Vite** for the frontend.

---

## 🚀 **Features**

- 🔐 **User Authentication** (Register/Login)
- 🏠 **Protected Home Page** (only accessible after login)
- 🔒 **Secure Password Hashing** with Flask-Bcrypt
- 🔄 **Frontend Routing** using React Router
- 🧠 **SQLite + SQLAlchemy** database integration

---

## ⚙️ **Tech Stack**

**Frontend:**
- ⚛️ React + Vite
- 🌐 React Router DOM
- 🔗 Axios

**Backend:**
- 🐍 Flask
- 🔐 Flask-Bcrypt
- 🔄 Flask-CORS
- 📍 SQLAlchemy + SQLite

---

## 📦 **Project Structure**

```
twitter-look-a-like/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── ...
└── frontend/
    ├── src/
    │   └── pages/
    │       ├── Intro.jsx
    │       ├── Register.jsx
    │       ├── Login.jsx
    │       └── Home.jsx
    └── ...
```

---

## 💪 **Getting Started**

### 🔧 Backend Setup

```bash
cd backend
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🌍 **Available Routes**

### 🔒 Frontend Pages

- `/intro` — Welcome screen with **Register/Login** buttons
- `/register` — **New user registration** page
- `/login` — **User login** page
- `/` — **Home** (after login) with **Logout** button

### ⚙️ Backend API

- `POST /api/register` — Register a new user
- `POST /api/login` — Login an existing user

---

## 👤 **Author**

**Donuts-procodes**  
🔗 GitHub: [https://github.com/Donuts-procodes](https://github.com/Donuts-procodes)

---
