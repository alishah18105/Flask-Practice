from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "Student"   
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    father_name = db.Column(db.String(50), nullable=False)
    seat_number = db.Column(db.String(50), unique = True, nullable = False)
    program = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable = False )

    student_info = db.relationship("Student_Info", back_populates="student")

class Course(db.Model):
    __tablename__ = "Course"  # match your actual table name
    course_id = db.Column(db.Integer, primary_key=True)
    course_no = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    credit_hours = db.Column(db.Integer, nullable=False)

    student_info = db.relationship("Student_Info", back_populates="course")


class Student_Info(db.Model):
    __tablename__ = "Student_Info"  # match your actual table name
    info_id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(50), db.ForeignKey("Student.seat_number"), nullable = False)
    semester = db.Column(db.Integer, nullable=False)
    course_no = db.Column(db.String(20), db.ForeignKey("Course.course_no"), nullable=False)
    marks = db.Column(db.Integer, nullable=False)

    student = db.relationship("Student", back_populates="student_info")
    course = db.relationship("Course", back_populates="student_info")
