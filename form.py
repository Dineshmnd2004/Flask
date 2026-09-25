
from flask import Flask, request

app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")

        return f"Registered: {name}, {email}"

    return """
    <form method="POST">
        <input name="name" placeholder="Enter name">
        <input name="email" placeholder="Enter email">
        <button type="submit">Register</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)