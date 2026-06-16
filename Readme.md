# ChatBot with FastAPI & LangChain

An AI-powered chatbot application built using FastAPI, LangChain, and Groq LLM.

## Features

* FastAPI Backend
* LangChain Integration
* Groq LLM Support
* REST API Endpoints
* Interactive Frontend
* Environment Variable Management
* Modular Project Structure

## Project Structure

```text
ANI_bot/
│
├── backend/
│   ├── bot/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── routers.py
│   │
│   ├── utils/
│   │   ├── db.py
│   │   └── settings.py
│   │
│   ├── .env
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── requirement.txt
└── README.md
```

## Technologies Used

* Python
* FastAPI
* LangChain
* Groq API
* SQLAlchemy
* PostgreSQL
* HTML
* CSS
* JavaScript

## Installation

### Clone Repository

```bash
git clone https://github.com/underiya-ai/ChatBot-with-Fastapi.git
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirement.txt
```

### Configure Environment Variables

Create a `.env` file inside the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=your_database_url
```

### Run Application

```bash
uvicorn backend.main:app --reload
```

### Backend Challenges & Solutions

#### 1. SQLAlchemy Database Configuration

Problem: Managing database connections manually across the application.

Solution: Created a centralized database configuration using SQLAlchemy Engine and Session.

#### 2. Database Session Management


Problem: Database sessions needed to be opened and closed safely.

Solution: Implemented FastAPI Dependency Injection using a dedicated get_db() function.

#### 3. Database Table Creation 


Problem: Database tables were not being created automatically.

Solution: Used Base.metadata.create_all() during application startup.

#### 4. FastAPI Dependency Injection

Problem: Passing database sessions throughout the application.

Solution: Used FastAPI's built-in Dependency Injection system with Depends().

#### 5. Prompt Engineering
Problem

The chatbot generated excessively long responses.

Solution

Added a system prompt to control response style and length.

#### 6. Debugging Internal Server Errors

Problem

500 Internal Server Error

Solution

Used Uvicorn terminal logs and traceback messages to identify the root cause instead of relying only on Swagger UI.


#### 7. CORS Middleware Configuration

Problem

The frontend was sending requests to the backend, but the browser blocked the communication.

The FastAPI server logs showed:

OPTIONS /chat HTTP/1.1" 405 Method Not Allowed

Cause

The browser automatically sends a preflight OPTIONS request before the actual POST request.

Since CORS was not configured in the FastAPI application, the backend rejected the request.

Solution

Configured FastAPI CORS Middleware to allow requests from the frontend.


## Author

Aniket Underiya
