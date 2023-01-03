from utils.data_handler import PostgreHandler
from utils.controller_school import ControllerSchool

postgre_model = PostgreHandler(
    database="postgres", 
    host="localhost", 
    user="postgres", 
    password="Lomivan88!"
    )
school_controller = ControllerSchool(postgre_model)

if __name__ == "__main__":
    pass
    # students = school_controller.get_students()
    # teachers = school_controller.get_teachers()
    # items = school_controller.get_items()
    # print(students)
    # print(teachers)
    # school_controller.create_item({"item_name":"Czech Language", "teacher_id": 3, "description": "Firt level"})
    # print(items)
    # student = school_controller.create_student({"first_name": "Franta", "second_name": "Maly", "date_of_birth": '1999-12-05', "gender": "M"})
    # students = school_controller.get_students()
    # for student in students:
    #     print(student)
    updated_student = school_controller.update_student("second_name", "Vancura", "student_id", 1)
    students = school_controller.get_students()
    print(students)
    deleted_student = school_controller.delete_student(4)
    students = school_controller.get_students()
    print(students)
    