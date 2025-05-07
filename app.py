import os

folders = [
    "app",
    "app/models",
    "app/schemas",
    "app/crud",
    "app/api",
    "app/services",
    "app/dependencies",
    "app/utils",
    "app/static/documents",
    "alembic"
]

init_files = [
    "app/__init__.py",
    "app/models/__init__.py",
    "app/schemas/__init__.py",
    "app/crud/__init__.py",
    "app/api/__init__.py",
    "app/services/__init__.py",
    "app/dependencies/__init__.py",
    "app/utils/__init__.py"
]

files = [
    "app/main.py",
    "app/config.py",
    "app/database.py",
    ".env",
    "requirements.txt",
    "README.md"
]

def create_project_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for init_file in init_files:
        with open(init_file, "w") as f:
            f.write("# init\n")
        print(f"Created: {init_file}")

    for file in files:
        with open(file, "w") as f:
            f.write("# Placeholder\n")
        print(f"Created file: {file}")

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully.")