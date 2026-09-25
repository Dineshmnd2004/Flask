
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Exercise 1: Query parameters
@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Guest")
    return f"Welcome, {name}!"


# Exercise 2: Form data
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    phn_num = request.form.get("phone_number", "")
    if not username:
        return "Username is required", 400

    return f"Welcome, {username}!"


# Exercise 3: JSON request and response
@app.route("/api/student", methods=["POST"])
def student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    name = data.get("name", "Guest")
    age = data.get("age")

    return jsonify({
        "name": name,
        "age": age
    }), 200


# Exercise 4: Registration with status codes
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    return jsonify({
        "message": "Registration successful",
        "name": data["name"]
    }), 201


# Exercise 5: Frontend-backend exchange
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Fetch Practice</title>
    </head>
    <body>
        <h2>Flask Frontend</h2>
        <button onclick="greetUser()">Send Request</button>
        <p id="result"></p>

        <script>
        async function greetUser() {
            const response = await fetch("/api/greet", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: "Dinesh"
                })
            });

            const data = await response.json();

            document.getElementById("result").textContent =
                data.message;
        }
        </script>
    </body>
    </html>
    """)


@app.route("/api/greet", methods=["POST"])
def greet():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    name = data["name"]

    return jsonify({
        "message": f"Hello, {name}!, How are you doing today?"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)