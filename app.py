from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Dinesh"
    course = "CSE"
    age = 22
    sub = "Python"
    marks = 75


    return render_template("index.html", name = name, course = course, age = age, sub = sub, marks = marks)

if __name__ == "__main__":
    app.run(debug=True)