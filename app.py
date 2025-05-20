from flask import Flask, render_template, request, redirect, url_for, session

from Enroll_student import student_enrollment
from grades_assign import assign_grades_for_student
from register_and_login import user_registration, user_login

app = Flask(__name__)
app.secret_key = "secretkey123"
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/register',methods=['GET','POST'])
def register_users():
    if request.method == "POST":
        user_type = request.form['user_type']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = user_registration(user_type,name,email,password)
        if user:
            return redirect(url_for('login'))
        return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = user_login(email,password)
        if user:
            session['user_type'] = user.__class__.__name__
            session['email'] = user.email
            session['password'] = user.password
            return redirect(url_for('dashboard'))
        return render_template("login.html")
@app.route('/dashboard')
def dashboard():
    if "user_type" not in session:
        return redirect(url_for('login'))
    if session["user_type"] == "student":
        return render_template("student_deshboard", name=session["name"])
    elif session["user_type"] == "Facilitator":
        return render_template("facilitator_dashboard", name=session["name"])

@app.route('/enroll', methods=['POST'])
def enroll():
    if 'user_type' in session and session['user_type'] == 'Student':
        course_code = request.form['course_code']
        from Student_Course_Management import Student
        student = Student(session['name'], session['email'], "hidden")  # Fake password for now
        student_enrollment(student, course_code)
    return redirect(url_for('dashboard'))
@app.route('/assign_grades')
def assign_grades():
    if "email" not in session and session['user_type'] == 'Facilitator':
        student_email = request.form['student_email']
        course_code = request.form['course_code']
        grades = request.form['grades']
        from Student_Course_Management import Facilitator
        facilitator = Facilitator(session['email'], session['password'],"hidden")
        assign_grades_for_student(facilitator, student_email, course_code, grades)
    return redirect(url_for('dashboard'))
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)



