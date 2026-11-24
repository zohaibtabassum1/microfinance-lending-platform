# Importing Flask
from flask import Flask, render_template

# Create our Flask application
app = Flask(__name__)


# Creating our Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Login Page route    |   when somebody adds /login to the URL, Login page will open, its because of @app.route("/login")
@app.route("/login")
def login():
    return render_template("login.html")

# Borrower Page route
@app.route("/profile")
def profile():
    return render_template("profile.html")

# Loan Page route
@app.route("/loan")
def loan():
    return render_template("loan.html")

# Start the application
if __name__ == "__main__":
    app.run()
