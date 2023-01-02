from .data_handler import PostgreHandler

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
    
    def create_student(self, data = {"first_name":str, "second_name":str, "date_of_birth":str, "gender":str }):
        self.pg_model.insert_data("students", data)
    
    def create_teacher(self, data= {"first_name":str, "second_name":str,  "title":str }):
       returning_text = self.pg_model.insert_data("teachers", data)
       return returning_text
    
    def create_item(self, data:dict):
        returning_text = self.pg_model.insert_data("items", data)
        return returning_text