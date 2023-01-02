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
    # students = school_controller.get_students()
    # teachers = school_controller.get_teachers()
    items = school_controller.get_items()
    # print(students)
    # print(teachers)
    # school_controller.create_item({"item_name":"Czech Language", "teacher_id": 3, "description": "Firt level"})
    print(items)