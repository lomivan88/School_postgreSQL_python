from utils.data_model import PostgreHandler
from utils.controler_school import ControllerSchool

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
    print(items)
    