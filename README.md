# 📌 Task Manager API

A small **FastAPI CRUD application** for managing tasks.
Features include creating, retrieving, updating, and deleting tasks by UUID.
The project also includes **pytest** tests and Docker setup.

---

## 🚀 Features

* Create a task (`POST /tasks/`)
* Get all tasks (`GET /tasks/`)
* Get a task by UUID (`GET /tasks/{uuid}`)
* Update a task (`PUT /tasks/{uuid}`)
* Delete a task (`DELETE /tasks/{uuid}`)

Task model:

```json
{
  "uuid": "c0a8012a-7b8a-4e5f-b9f0-123456789abc",
  "title": "Example task",
  "description": "Optional description",
  "status": "created | in_progress | done"
}
```

---

## 📦 Local Installation

1. Clone the repository and navigate to the project folder:

   ```bash
   git clone <repo_url> task_manager
   cd task_manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:

   ```bash
   uvicorn app.main:app --reload
   ```

Server available at:
👉 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
👉 ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🐳 Run with Docker

### Production

```bash
docker compose up --build
```

### Development (hot-reload)

```bash
docker compose -f docker-compose.dev.yml up --build
```

The app will be available at [http://localhost:8000](http://localhost:8000).

---

## ✅ Tests

Run unit tests:

```bash
pytest -q
```

---

## 📂 Project Structure

```
task_manager/
│── app/
│   ├── __init__.py
│   ├── main.py         # Entry point, routes
│   ├── schemas.py      # Pydantic models
│   ├── storage.py      # In-memory storage
│── tests/
│   └── test_tasks.py   # pytest CRUD tests
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── docker-compose.dev.yml
│── README.md
|── ...
```

---

## ✨ Example Requests

Create a task:

```bash
curl -X POST http://127.0.0.1:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Write tests", "description": "pytest", "status": "created"}'
```

Get all tasks:

```bash
curl http://127.0.0.1:8000/tasks/
```

Update a task:

```bash
curl -X PUT http://127.0.0.1:8000/tasks/<UUID> \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'
```

Delete a task:

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/<UUID>
```

---

## 🔧 Technologies

* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/)
* [Pytest](https://docs.pytest.org/)
* [Docker](https://www.docker.com/)

---

## 👩‍💻 Author

Karina Apaeva
Junior Python Backend Developer
