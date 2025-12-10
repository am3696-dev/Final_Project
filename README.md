
## Final Project: Advanced User Profile System
# Overview
This is a full-stack web application built with **FastAPI** (Backend) and **HTML/JavaScript** (Frontend). It demonstrates a complete user lifecycle including Registration, Authentication (JWT), Profile Management (Bio/Location), Password Changes, and Account Deletion.

The project features a robust **CI/CD pipeline** using GitHub Actions to automatically run tests and deploy the Docker image to Docker Hub.

## Features
* **User Authentication:** Secure Signup and Login using hashed passwords (Bcrypt).
* **Profile Management:** Users can update their Biography and Location.
* **Security:** Users can securely change their passwords.
* **Account Management:** Full lifecycle support, including "Delete Account."
* **Automated Testing:** 89%+ Code Coverage with Pytest and full End-to-End (E2E) testing with Playwright.

## Docker Hub Repository
You can pull the production-ready image from Docker Hub here:
**[https://hub.docker.com/r/am3696/final_project](https://hub.docker.com/r/am3696/final_project)**

---

## How to Run Locally
### 1. Prerequisites
* Python 3.10+
* Docker (for running Postgres) or a local PostgreSQL server
### 2. Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/am3696-dev/Final_Project.git
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install pytest-playwright
    playwright install
    ```
4.  **Run the Application**
    ```bash
    uvicorn app.main:app --reload
    ```
    Once running, visit http://127.0.0.1:8000/profile-ui to create an account and use the app.

### Run All Tests:
```bash
pytest
```
### Run E2E Browser Tests Only:
```bash
pytest tests/e2e/test_auth.py
```

