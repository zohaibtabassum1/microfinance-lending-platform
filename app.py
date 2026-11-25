# Importing JSON
import json

# For HashPassword
import os
from dotenv import load_dotenv

# Importing Flask
from flask import Flask, render_template, request, redirect, url_for

# Importing from werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

# Create our Flask application
app = Flask(__name__)

# Get demo password from .env file
demo_password = os.environ.get("DEMO_PASSWORD")

if not demo_password:
    raise RuntimeError("DEMO_PASSWORD is missing. Check your .env file.")
    
# Sample user with a hashed password
sample_user = {
    "email": "test@example.com",
    "password": generate_password_hash(demo_password)
}


# Creating our Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Login Page route    |   when somebody adds /login to the URL, Login page will open, its because of @app.route("/login")
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if (
        sample_user["password"] is not None
        and email == sample_user["email"]
        and check_password_hash(sample_user["password"], password)
        ):
            return redirect(url_for("profile"))
        else:
            return "Invalid email or password!"

    return render_template("login.html")

# Loan Page route
@app.route("/loan", methods=["GET", "POST"])
def loan():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        loan_amount = request.form.get("loan_amount")
        loan_purpose = request.form.get("loan_purpose")

        # Even if someone bypasses the browser, Flask checks the submitted information using this validation
        if not full_name or not email:
            return "Please fill in all required fields."
        if not loan_amount or not loan_amount.isdigit() or int(loan_amount) <= 0:
            return "Please enter a valid loan amount."
        return render_template(
            "loan_success.html",
            name=full_name,
            email=email,
            loan_amount=loan_amount,
            loan_purpose=loan_purpose
        )

    return render_template("loan.html")

# Borrowers Page route
@app.route("/profile")
def profile():

    with open("borrowers.json", "r", encoding="utf-8") as file:
        borrowers = json.load(file)

    return render_template("profile.html", borrowers=borrowers)


# Start the application
if __name__ == "__main__":
    app.run()
