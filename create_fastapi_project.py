import os

PROJECT_STRUCTURE = {
    "app": {
        "main.py": "",
        "api": {
            "__init__.py": "",
            "v1": {
                "__init__.py": "",
                "endpoints": {
                    "__init__.py": "",
                    "users.py": "# User endpoints\n",
                    "items.py": "# Item endpoints\n"
                }
            }
        },
        "core": {
            "__init__.py": "",
            "config.py": "# Configuration settings\n",
            "security.py": "# Security utilities\n"
        },
        "crud": {
            "__init__.py": "",
            "items_crud.py": "# Configuration settings\n",
            "users_crud.py": "# Security utilities\n"
        },
        "db": {
            "__init__.py": "",
            "database.py": "# Database connection\n",
            "models.py": "# DB models\n"
        },
        "schemas": {
            "__init__.py": "",
            "user.py": "# User schemas\n",
            "item.py": "# Item schemas\n"
        },
        "services": {
            "__init__.py": "",
            "user_service.py": "# Business logic for users\n",
            "item_service.py": "# Business logic for items\n"
        },
        "dependencies": {
            "__init__.py": "",
            "common.py": "# Common dependencies\n"
        }
    },
    "tests": {
        "__init__.py": "",
        "unit": {},
        "integration": {}
    },
    "requirements.txt": "# Add your requirements here\nfastapi\nuvicorn\n",
    "Dockerfile": "FROM python:3.10\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n",
    "README.md": "# FastAPI Project\n"
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)


def main():
    project_name = input("Enter your project name: ").strip()
    if not project_name:
        print("Project name cannot be empty.")
        return

    if os.path.exists(project_name):
        print(f"Directory '{project_name}' already exists.")
        return

    os.makedirs(project_name)
    create_structure(project_name, PROJECT_STRUCTURE)
    print(f"✅ FastAPI project '{project_name}' created successfully!")


if __name__ == "__main__":
    main()


# Below command is used to create 
'''
python create_fastapi_project.py
'''
