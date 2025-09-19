# 📚 Flask Learning Projects  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask)  
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)  
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)  

This repository contains beginner-friendly **Flask projects** I created while learning web development with Python.  
Each project focuses on different concepts like **routing, templates, Jinja2, Bootstrap UI, and database integration (SQLite / PostgreSQL).**  

---

## 📝 Project 1: Flask To-Do App (Python + Flask + SQLite)  

A simple To-Do web app to practice Flask basics and CRUD operations.  

### 🔹 Concepts Covered  
- Flask routing & HTML rendering (`render_template`)  
- Templates & static files  
- Jinja templating: blocks, loops, conditionals  
- CRUD operations (Create, Read, Update, Delete) with **SQLite**  
- Bootstrap for responsive UI  

### 📂 Project Structure  
Todo App/  
│── app.py  
│── requirements.txt  
│── instance/todo.db  
│── templates/  
│ ├── base.html  
│ ├── index.html  
│ └── update.html  
│── static/   


---

## 📝 Project 2: Student Management System (Flask + SQLAlchemy + PostgreSQL)  

A web-based system to manage student records, courses, marks, and grades.  
Students can view their **proforma/marksheet** by entering their **Seat Number & Semester**.  

### 🔹 Features  
- Add new **Student**  
- Add new **Course**  
- View all students and courses  
- Add **academic records** (marks for a course in a semester)  
- Search student records by **Seat Number & Semester**  
- Display student **marksheet (proforma)** with  
  - Name, Father Name, Seat No, Semester  
  - Course-wise table (Course No, Credit Hours, Marks, Grade, Grade Points)  

### 📂 Project Structure 

student-management/  
│── app.py # Main Flask app  
│── models.py # SQLAlchemy models  
│── requirements.txt # Dependencies  
│── templates/  
│ ├── base.html  
│ ├── student_page.html  
│ ├── course_page.html  
│ ├── student_info_page.html  
│── static/  


## ⚙️ Installation & Setup  

1. **Clone Repository**
   ```bash
   git clone https://github.com/alishah18105/Flask-Practice
   cd Flask-Practice
    ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac  
   venv\Scripts\activate      # Windows
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**

   ```bash
   python app.py
   ```


