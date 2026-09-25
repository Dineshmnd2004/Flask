from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Ai Engineer Journey."

@app.route("/about")
def about():
    return "This is my first Flask Project."
if __name__ == "__main__":
    app.run(debug=True)


