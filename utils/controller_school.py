from .data_handler import PostgreHandler

class ControllerSchool:
    def __init__(self, pg_model: PostgreHandler):
        self.pg_model = pg_model
        
    def get_students(self):
        students = self.pg_model.get_data_all("students")
        return students
    
    def get_teachers(self):
        teachers = self.pg_model.get_data("teachers",["first_name", "second_name", "title"])
        return teachers
    
    def get_items(self):
        items = self.pg_model.get_data_all("items")
        return items
    
    def create_student(self, data:dict):
        self.pg_model.insert_data("students", data)
    
    def create_teacher(self, data:dict):
       returning_text = self.pg_model.insert_data("teachers", data)
       return returning_text
    
    def create_item(self, data:dict):
        returning_text = self.pg_model.insert_data("items", data)
        return returning_text
    
    def update_data(self, table, s_column, s_value, by_column, column_value):
        returning_text = self.pg_model.update_item(table, s_column, s_value, by_column, column_value)
        return returning_text