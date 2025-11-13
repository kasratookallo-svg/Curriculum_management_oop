

import re

# Molding Studies
class   Curriculum:
    #Donder _ Double Underlines or magic function
    # Method
    def __init__(self, lesson_name, lesson_code, teacher_name , lesson_credits):
        # Property
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        self.teacher_name = teacher_name
        self.lesson_credits = lesson_credits
        self.lesson_list = []

    def add_lesson(self, lesson):
        pass


    # Method
    def save(self):
        print(f"INFO :   {self.lesson_name:10} , {self.lesson_code:} \t\t {self.teacher_name:10} , {self.lesson_credits:}")
    # Method_function
    def validation(self ):
        return (re.match(r"^[a-zA-Z\s]{3,30}$",self.lesson_name ) and
                (type(self.lesson_code) == int and self.lesson_code >= 0) and
                re.match(r"^[a-zA-Z\s]{3,30}$", self.teacher_name) and
                (type(self.lesson_credits) == int and self.lesson_credits >= 0)
                )
    # Representation
    def __repr__(self):
        return f" \n{self.lesson_name} \t---->>(Code) {self.lesson_code:5}: (Credits)\t---->> {self.lesson_credits} \nTeacher's Name :\t\t {self.teacher_name}\n "


