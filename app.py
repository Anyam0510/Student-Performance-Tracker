from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    db = get_db()
    students = db.execute("SELECT * FROM students").fetchall()
    return render_template("index.html", students=students)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        db = get_db()
        db.execute("INSERT INTO students (name, roll_number) VALUES (?, ?)", (name, roll_number))
        db.commit()
        return redirect(url_for("index"))
    return render_template("add_student.html")

@app.route("/add_grades/<int:roll_number>", methods=["GET", "POST"])
def add_grades(roll_number):
    db = get_db()
    if request.method == "POST":
        subject = request.form["subject"]
        grade = int(request.form["grade"])
        db.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
        db.commit()
        return redirect(url_for("index"))
    return render_template("add_grades.html", roll_number=roll_number)

@app.route("/view/<int:roll_number>")
def view_student(roll_number):
    db = get_db()
    student = db.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,)).fetchone()
    grades = db.execute("SELECT * FROM grades WHERE roll_number = ?", (roll_number,)).fetchall()
    return render_template("view_student.html", student=student, grades=grades)

if __name__ == "__main__":
    app.run(debug=True)
