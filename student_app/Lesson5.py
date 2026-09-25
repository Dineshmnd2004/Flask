from flask import Flask, render_template, request

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("form.html")


# Exercise 1: Basic Form
@app.route("/basic-form", methods=["POST"])
def basic_form():

    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    city = request.form.get("city", "").strip()

    return f"""
        <h2>Basic Form Details</h2>
        Name: {name}<br>
        Age: {age}<br>
        City: {city}
    """


# Exercise 2: Required Fields
@app.route("/required", methods=["POST"])
def required():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name:
        return "Name is required"

    if not email:
        return "Email is required"

    return f"Name: {name}<br>Email: {email}"


# Exercise 3: Age Validation
@app.route("/age-validation", methods=["POST"])
def age_validation():

    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()

    if not name:
        return "Name is required"

    if not age:
        return "Age is required"

    if not age.isdigit():
        return "Age must be a number"

    age = int(age)

    if age < 18 or age > 60:
        return "Invalid age. Age must be between 18 and 60"

    return f"Hello {name}, your age is {age}"


# Exercise 4: Search Form
@app.route("/search")
def search():

    keyword = request.args.get("keyword", "").strip()

    if not keyword:
        return "Please enter something to search"

    return f"You searched for: {keyword}"


# Exercise 5: Registration Form
@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    age = request.form.get("age", "").strip()

    # Name validation
    if not name:
        return "Name is required"

    # Email validation
    if not email:
        return "Email is required"

    if "@" not in email:
        return "Invalid email"

    # Password validation
    if not password:
        return "Password is required"

    if len(password) < 6:
        return "Password must contain at least 6 characters"

    # Age validation
    if not age:
        return "Age is required"

    if not age.isdigit():
        return "Age must be a number"

    age = int(age)

    if age < 18 or age > 60:
        return "Age must be between 18 and 60"

    return f"""
        <h2>Registration Successful</h2>
        Name: {name}<br>
        Email: {email}<br>
        Age: {age}
    """


if __name__ == "__main__":
    app.run(debug=True)