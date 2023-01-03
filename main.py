from utils.data_handler import PostgreHandler
from utils.school_system import SchoolSystem
import os

postgre_model = PostgreHandler(
    database="postgres", 
    host="localhost", 
    user="postgres", 
    password="Lomivan88!"
    )
school_sys = SchoolSystem(postgre_model)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_menu():
    print("******Welcome in school information system******")
    print("Choose from the menu:")
    print("\t[0] to insert a teacher")
    print("\t[1] to insert a item")
    print("\t[2] to insert a student")
    print("\t[3] to list teachers")
    print("\t[4] to list students")
    print("\t[5] to list items")
    print("\t[6] to update student")
    print("\t[7] to delete student")
    
def teachers_list():
    teachers = school_sys.get_teachers()
    print("\nTeacher list: ")
    for teacher in teachers:
       print(str(teacher["teacher_id"]) + " " + teacher["title"] + teacher["first_name"] + " " + teacher["second_name"])

def student_list():
    students = school_sys.get_students()
    print("\nStudent list: ")
    for student in students:
        print(f"{student['student_id']} {student['first_name']} {student['second_name']}, {student['gender']}")

def insert_teacher():
    print("\nCreate teacher:")
    f_name = input("First name: ")
    s_name = input("Second name: ")
    title = input("Title: ")
    school_sys.create_teacher({"first_name":f_name, "second_name":s_name, "title":title})

def insert_student():
    print("\nCreate student:")
    f_name = input("First name: ")
    s_name = input("Second name: ")
    date_of_birth = input("Date of birth: ")
    gender = input("Gender: ")
    school_sys.create_student({"first_name":f_name, "second_name":s_name, "date_of_birth":date_of_birth ,"gender":gender})

def delete_stundent():
    print("\nDelete student:")
    try: 
        student_id = int(input("Type student ID: "))
        deleted_student = school_sys.delete_student(student_id=student_id)
        print(f"Student was deleted: {deleted_student}")
    except TypeError as e:
        print("Student id must be integer!")
    
if __name__ == "__main__":
    
    while True:
        print_menu()
        try:
            menu_choice = int(input("Your choice: "))
            if menu_choice < 0 or menu_choice > 7 :
                print("Choice out of range!")
        except TypeError as e:
            print("Please type the number from menu!")

        if menu_choice == 0:
            insert_teacher()
        if menu_choice == 1:
            pass
        if menu_choice == 2:
            insert_student()
        if menu_choice == 3:
            teachers_list()
        if menu_choice == 4:
            student_list()
        if menu_choice == 7:
            delete_stundent()
            
        next_choice = input("Type 'exit' if you want to finish or push 'Enter' for next choice. \n")
        if next_choice == "exit":
            break
        else:
            cls()
    