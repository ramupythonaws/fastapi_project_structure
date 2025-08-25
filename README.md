# FastAPI Project Folder structure
* **app/main.py:** The entry point of the FastAPI application, where the FastAPI instance is initialized and routers are included.
* **app/api/:** Contains the API endpoints, often organized by version (e.g., v1/) and then by resource (e.g., users.py, items.py within endpoints/).
* **app/core/:** Houses application-wide configurations, settings (e.g., config.py), and security-related functionalities (e.g., security.py).
*  **app/crud/:** Handle raw database operations (queries, inserts, updates, deletes).
* **app/db/:** Manages database-related components, including database connection setup (e.g., database.py) and SQLAlchemy models (e.g., models.py).
* **app/schemas/:** Defines Pydantic models for data validation, request parsing, and response serialization. 
* **app/services/:** Encapsulates business logic and interactions with the database or external services.
* **app/dependencies/:** Stores common dependencies that can be injected into route functions, such as database sessions or authentication checks.
* **tests/:** Contains unit and integration tests for the application.
* **requirements.txt:** Lists all project dependencies.
* **Dockerfile:** Defines the Docker image for containerizing the application.
* **README.md:** Provides documentation for the project.



```txt

project_name/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── items_crud.py
│   │   └── users_crud.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   └── dependencies/
│       ├── __init__.py
│       └── common.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   └── integration/
├── requirements.txt
├── Dockerfile
├── README.md
```
