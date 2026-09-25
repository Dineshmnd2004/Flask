from flask import Flask, request

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello Flask"

@app.route("/greet/<name>")
def greet(name):
    return f"Welcome,{name}!"

@app.route("/cube/<int:number>")
def cube(number):
    return str(number ** 3)

@app.route("/search")
def search():
    k = request.args.get('q', 'Python')
    return f"Searching for: {k}"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return "Registration page"

    return "Registration Submitted"

if __name__ == "__main__":
    app.run(debug=True)