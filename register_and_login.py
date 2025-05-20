from Student_Course_Management import Student, Facilitator
import re
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
def validate_name(name):
    return name.isaphla()
def validate_password(password):
    return  len(password) >= 8
def user_registration(user_type, name=None, email=None, password=None):
    if name is None:
        name = input("Enter your full name: ")
        if not validate_name(name):
            print("Invalid name, name must contain only letters")
        return

    if email is None:
        email = input("Enter your email: ").strip()
        if not validate_email(email):
            print("Invalid email")
            return
    if password is None:
        password = input("Enter your password: ")
        if not validate_password(password):
            print("Invalid password, password must be more the Eight digit (8)")


    if user_type.lower() == "student":
        try:
            with open("student.txt", "r") as file:
                for line in file:
                    if email in line:
                        print("This email is already registered.")
                        return None
        except FileNotFoundError:
            pass

        with open("student.txt", "a") as file:
            file.write(f"{name},{email},{password}\n")
        return Student(name, email, password)

    elif user_type.lower() == "facilitator":
        with open("facilitator.txt", "a") as file:
            file.write(f"{name},{email},{password}\n")
        return Facilitator(name, email, password)

    else:
        print("Invalid user type")
        return None

def user_login(email=None, password=None):
    if email is None:
        email = input("Enter your email: ").strip()
    if password is None:
        password = input("Enter your password: ").strip()

    try:
        with open("student.txt", "r") as file:
            for line in file:
                name, user_email, user_password = line.strip().split(",")
                if user_email == email and user_password == password:
                    return Student(name, email, password)
    except FileNotFoundError:
        pass

    try:
        with open("facilitator.txt", "r") as file:
            for line in file:
                name, user_email, user_password = line.strip().split(",")
                if user_email == email and user_password == password:
                    return Facilitator(name, email, password)
    except FileNotFoundError:
        pass

    print("Login failed: Invalid email or password")
    return None
