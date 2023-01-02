from .data_model import PostgreHandler

class ControllerSchool:
    def __init__(self, pg_model: PostgreHandler):
        self.pg_model = pg_model
        
    def get_students(self):
        students = self.pg_model.get_data("students", ["first_name", "second_name", "date_of_birth", "gender"])
        return students
    
    def get_teachers(self):
        teachers = self.pg_model.get_data("teachers",["first_name", "second_name", "title"])
        return teachers
    
    def get_items(self):
        items = self.pg_model.get_data_all("items")
        return items