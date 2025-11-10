import re


class   Curriculum:
    #Donder _ Double Underlines or magic function
    # Method
    def __init__(self,lesson_name,lesson_code, teacher_name , lesson_credits):
        # Property
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        self.teacher_name = teacher_name
        self.lesson_credits = lesson_credits
        self.lesson_credits = []

    def add_lesson(self, lesson):
        self.lesson_list.append(lesson)

    # Method
    def save(self):
        print("INFO : " , self.lesson_name , self.lesson_code ,  self.teacher_name , self.lesson_credits)
    # Method
    def validation(self):
        return (re.match(r"^[a-zA-Z\s]{3,30}$",self.lesson_name ) and
                re.match(r"^[a-zA-Z\s]{3,30}$", self.teacher_name) and
                self.lesson_code >= 0 and
                20 >= self.lesson_credits >= 0)

    def __repr__(self):
        return f" {self.lesson_name:10} (Code) {self.lesson_code}: (Credits) {self.lesson_credits:10} - Teacher's Name : {self.teacher_name:10} "
        #return "Person(name={},age={})".format(self.name, self.age)

