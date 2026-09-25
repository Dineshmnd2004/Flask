
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    student = {
        "name": "Dinesh",
        "course": "Computer Science",
        "marks": 85
    }

    skills = ["Python", "Flask", "SQL"]

    return render_template(
        "home.html",
        student=student,
        skills=skills
    )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)