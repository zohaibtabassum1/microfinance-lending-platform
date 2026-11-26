# Microfinance Lending Platform

A beginner-friendly, fictional microfinance lending platform built with Python and Flask. This project demonstrates basic borrower management, login functionality, loan applications, and application security testing.

**Note:** This is an educational demonstration project. It is not intended for real financial transactions or production use.

## Features

- Login page with password hashing.
- Borrower profile displaying sample borrower records.
- Loan application form with server-side validation.
- CSRF protection using Flask-WTF.
- Sample borrower data generated and stored in JSON.
- Security scanning using Semgrep and pip-audit.

## Technologies Used

- Python
- Flask
- HTML
- JSON
- Werkzeug
- Flask-WTF
- python-dotenv
- Semgrep
- pip-audit

## Project Setup

### 1. Clone the repository

```powershell
git clone https://github.com/zohaibtabassum1/microfinance-lending-platform.git
cd microfinance-lending-platform
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

**Important: This step is mandatory.** The application requires a `.env` file before it can run. It contains the demo login password and Flask secret key.

Create a file named `.env` in the project root directory.

Add the following:

```env
DEMO_PASSWORD=your_own_demo_password
SECRET_KEY=your_generated_secret_key
```

Generate a secure secret key by running this command in your activated `.venv` PowerShell terminal:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the generated key into the `SECRET_KEY` variable in your `.env` file.

Choose your own demo password and set it as `DEMO_PASSWORD`.

**What happens if you skip this step?**

The application will not start. It will display an error if `DEMO_PASSWORD` or `SECRET_KEY` is missing. The secret key is required for Flask-WTF CSRF protection to validate form submissions correctly.

**Security note:** The `.env` file contains private configuration values. Never upload it to GitHub or share its contents. It is excluded through `.gitignore`.

### 6. Generate sample borrower data

```powershell
python generate_data.py
```

This creates the sample borrower data file used by the application.

### 7. Run the application

```powershell
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000/

## Demo Login

Use the following email address:

`test@example.com`

The demo password is the value you configured as `DEMO_PASSWORD` in your local `.env` file.

### Demo Authentication Limitations

This project uses a single demo account stored in application memory. Its password hash is generated at application startup using Werkzeug's password hashing functions and the `DEMO_PASSWORD` environment variable.

No user records or password hashes are stored permanently in a database or file. This is a simplified authentication implementation for educational demonstration purposes, not a production-ready user management system.

## Security Testing

The project uses two security scanning tools.

**Semgrep - Static Application Security Testing**

```powershell
semgrep scan --config auto .
```

**pip-audit - Dependency Vulnerability Scanning**

```powershell
pip-audit -r requirements.txt
```

Refer to `baseline_scan.md` for the recorded security scan results and manual security verification.

## Security Notes

- Passwords are hashed using Werkzeug.
- CSRF protection is implemented using Flask-WTF.
- Environment variables are loaded using python-dotenv.
- `.env` and virtual environment folders are excluded through `.gitignore`.
- Sample borrower records are fictional.
- This application is intended for educational purposes and is not production-ready.

## Project Purpose

This project was developed as part of a cybersecurity internship task to practise Flask development, basic application security, dependency auditing, and security documentation.