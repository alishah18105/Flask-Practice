import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Student, Course, db, Student_Info

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:ali@localhost:5432/Student_Management"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.urandom(24)


db.init_app(app)

@app.route('/',methods=['GET', 'POST'] )

def Students():
    allStudents = Student.query.all()
    return render_template('student_page.html',allStudents = allStudents)

@app.route('/course',methods=['GET', 'POST'] )
def Course_Info():
    allCourses = Course.query.all()
    return render_template('course_page.html',allCourses = allCourses)

@app.route('/student_info')
def Student_Info():
    return "<p>Student Information</p>"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)