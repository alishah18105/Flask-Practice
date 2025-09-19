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
    
    if request.method == "POST":
        name = request.form['name']
        father_name = request.form['father_name']
        seat_number = request.form['seat_number']
        program = request.form['program']
        gender = request.form['gender']

        student = Student(name = name, father_name = father_name, seat_number = seat_number, program = program, gender =gender)
        db.session.add(student)
        db.session.commit()
        return redirect('/')  

    allStudents = Student.query.all()
    return render_template('student_page.html',allStudents = allStudents)


@app.route('/course', methods=['GET', 'POST'])
def Course_Info():
    if request.method == "POST":
        course_no = request.form['course_no']
        course_name = request.form['course_name']
        credit_hours = request.form['credit_hours']

        course = Course(
            course_no=course_no,
            course_name=course_name,
            credit_hours=credit_hours
        )
        db.session.add(course)
        db.session.commit()
        return redirect('/course')

    allCourses = Course.query.all()
    return render_template('course_page.html', allCourses=allCourses)



@app.route('/student_info', methods=['GET', 'POST'])
def Student_Information():
    

    if request.method == "POST":
        if "add_record" in request.form:
            
            seat_number = request.form['seat_number']
            semester = int(request.form['semester'])
            course_no = request.form['course_no']
            marks = int(request.form['marks'])

            record = Student_Info(
                seat_number=seat_number,
                semester=semester,
                course_no=course_no,
                marks=marks
            )
            db.session.add(record)
            db.session.commit()
            return redirect('/student_info')

        elif "search_record" in request.form:
            # Form 2: Search student records
            seat_number = request.form['search_seat_number']
            semester = int(request.form['search_semester'])
            student_info = db.session.query(
                Student_Info,
                Student.name,
                Student.father_name,
                Student_Info.course_no,
                Student_Info.marks,
                Course.credit_hours,
                Student_Info.semester,
                Student_Info.seat_number,

                
            ).join(Student, Student_Info.seat_number == Student.seat_number
            ).join(Course, Student_Info.course_no == Course.course_no
            ).filter(
                Student_Info.seat_number == seat_number,
                Student_Info.semester == semester
            ).order_by(Student_Info.course_no).all()
            return render_template('student_info_page.html', student_info=student_info)
    return render_template('student_info_page.html')



@app.route('/delete/student/<int:student_id>')
def delete_Student(student_id):
    student = Student.query.filter_by(student_id= student_id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

@app.route('/delete/course/<int:course_id>')
def delete_Course(course_id):
    course = Course.query.filter_by(course_id= course_id).first()
    db.session.delete(course)
    db.session.commit()
    return redirect("/course")
if __name__ == "__main__":
    app.run(debug=True, port = 8000)