# FastAPI Basics 🚀

A beginner-friendly FastAPI project to learn how modern Python backend APIs are built — fast, async, and sane.

This repo covers:
- API creation
- Routing
- Request/response handling
- Data validation
- Automatic docs (the killer feature)

---

## What is FastAPI?

FastAPI is a **modern Python web framework** for building APIs using:
- Python type hints
- ASGI (async-first)
- Pydantic for validation

Why people simp for it:
- Blazing fast (Starlette + Uvicorn)
- Minimal boilerplate
- Auto-generated docs (Swagger & ReDoc)
- Hard to shoot your own foot (types save lives)

---
## Requirements

- Python **3.8+**
- pip
- Virtual environment (recommended, not optional if you’re sane)

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fastapi-basics.git
cd fastapi-basics
python -m venv venv
pip install fastapi uvicorn


fastapi-basics/
│
├── main.py        # Entry point
├── requirements.txt
└── README.md


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

