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
    return render_template('student_page.html')

@app.route('/course')
def Course():
    return render_template('course_page.html')

@app.route('/student_info')
def Student_Info():
    return "<p>Student Information</p>"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)