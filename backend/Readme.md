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

## Author

Aniket Underiya
