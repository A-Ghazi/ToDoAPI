
# Todo List API

This is a simple **Todo List API** built using **FastAPI** and **MySQL** as the database. The API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on todo items.

## Features

- Create, read, update, and delete todo items.
- Input validation with **Pydantic** models.
- **MySQL** as the database for persistent storage.
- **Dependency Injection** for database sessions.
- **FastAPI** for high-performance, modern web APIs.

## Project Structure

```bash
app/
│
├── main.py          # Entry point for the FastAPI application
├── database.py      # Database configuration and session creation
├── models.py        # SQLAlchemy models (database tables)
├── schemas.py       # Pydantic models (request/response validation)
├── crud.py          # CRUD operations (Create, Read, Update, Delete)
└── routes/
    └── todos.py     # API routes/endpoints for Todo items
```

## Requirements

- **Python 3.8+**
- **MySQL** database
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **uvicorn** for serving the app

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/todo-list-api.git
cd todo-list-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database

- Ensure that **MySQL** is installed and running on your machine.
- Create a database:

```sql
CREATE DATABASE todo_db;
```

- Update the MySQL connection string in the `app/database.py` file with your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/todo_db"
```

### 5. Run Migrations (Create Tables)

Run the following script to create the required tables in the MySQL database:

```python
from app.database import Base, engine
Base.metadata.create_all(bind=engine)
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

- The API will be available at: `http://127.0.0.1:8000`

## Endpoints

| Method | Endpoint          | Description                      |
|--------|-------------------|----------------------------------|
| `GET`  | `/todos/`          | Get all todos                    |
| `GET`  | `/todos/{id}`      | Get a specific todo by ID        |
| `POST` | `/todos/`          | Create a new todo                |
| `PUT`  | `/todos/{id}`      | Update a todo by ID              |
| `DELETE` | `/todos/{id}`    | Delete a todo by ID              |

### Sample POST Request

```bash
POST /todos/
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Cheese",
  "completed": false
}
```

### Response

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Cheese",
  "completed": false
}
```

## Testing the API

You can use **Postman** or **curl** to interact with the API. Here's a sample request to create a new todo:

```bash
curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{
    "title": "Go for a walk",
    "description": "Evening walk in the park",
    "completed": false
}'
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- **FastAPI**: Fast, modern web framework for building APIs.
- **Pydantic**: Data validation and parsing using Python type annotations.
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM).
  
