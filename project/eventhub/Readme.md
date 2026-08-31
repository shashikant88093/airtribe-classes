<!-- username and password -->
<!-- username = eventhub -->
<!-- password = eventhub -->



# EventHub API

EventHub is a backend REST API for a simplified event ticketing and seat reservation platform built with Django and Django REST Framework.

---

## 📋 Table of Contents
- [Docker Setup Commands](#-docker-setup-commands-recommended)
- [Local Setup Commands](#-local-setup-commands-without-docker)
- [Database & Management Commands](#-database--management-commands)
- [API Testing Commands (cURL)](#-api-testing-commands-curl)
- [API Endpoints Summary](#-api-endpoints-summary)
- [Interactive API Documentation](#-interactive-api-documentation)
- [Design Decision](#-design-decision)

---

## 🐳 Docker Setup Commands (Recommended)

```bash
# 1. Clone the project repository
git clone <your-repository-url>

# 2. Navigate into the project root directory
cd eventhub

# 3. Build docker images and start all containers in foreground (logs attached)
docker compose up --build

# 4. Start all containers in the background (detached mode)
docker compose up -d

# 5. Check real-time logs from the running web container
docker compose logs -f web

# 6. Check the running container status and port mappings
docker compose ps

# 7. Stop and remove running containers, networks, and volumes
docker compose down



# 1. Navigate to the project root directory
cd eventhub

# 2. Create an isolated Python virtual environment named 'venv'
# macOS/Linux:
python3 -m venv venv
# Windows:
python -m venv venv

# 3. Activate the virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows (Command Prompt):
venv\Scripts\activate.bat
# Windows (PowerShell):
venv\Scripts\Activate.ps1

# 4. Upgrade pip package installer to the latest version
pip install --upgrade pip

# 5. Install all required dependencies (Django, DRF, drf-spectacular)
pip install -r requirements.txt

# 6. Apply database migrations to create SQLite tables
python manage.py makemigrations
python manage.py migrate

# 7. Start the local development server at 127.0.0.1:8000
python manage.py runserver




# Generate migration files for newly modified models
docker compose run --rm web python manage.py makemigrations

# Apply migrations to the database
docker compose run --rm web python manage.py migrate

# Create an administrator account for Django Admin panel access
docker compose run --rm web python manage.py createsuperuser

# Open an interactive Python shell with the Django environment loaded
docker compose run --rm web python manage.py shell

# Access the container's interactive Linux bash shell
docker compose run --rm web /bin/sh