# FastAPI Auth Service

A backend authentication service built using FastAPI. This project demonstrates user authentication, token-based authorization, and scalable backend design.

---

Features

* User authentication (Login)
* JWT-based authorization
* Secure API endpoints
* Modular project structure
* FastAPI-powered high-performance APIs

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd fastapi-auth-service
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
python3 -m pip install fastapi uvicorn python-jose passlib[bcrypt]
```

---

## Run the Server

```bash
python3 -m uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## Author

Anshu Saxena
