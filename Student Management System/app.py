import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ali@localhost:5432/Student_Management"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
#db = SQLAlchemy(app)

@app.route('/')

def Students():
    return "<p>Student Record</p>"

    # if request.method == "POST":

    #     name = request.form["name"]
    #     father_name = request.form["father_name"]
    #     seat_number = request.form["seat_number"]
    #     program = request.form["program"]
    #     gender = request.form["gender"]


    #     student = Student(name = name, 
    #                       father_name = father_name
    #                         seat_number = seat_number
    #                         program = program
    #                         gender = gender)

    #     db.session.add(student)
    #     db.session.commit()
    # allTodo = Todo.query.all()
    # return render_template('index.html',allTodo = allTodo)

@app.route('/course')
def Course_Information():
    return "<p>Course Record</p>"

@app.route('/student_info')
def Student_Information():
    return "<p>Student Information</p>"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)