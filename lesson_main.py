import self

import lesson_module
from lesson_module import *

lesson_list = []
lesson_code = 0
lesson_credits = 0
for i in range(2):
    Lesson_code = int(input("Enter Lesson Code : "))
    lesson_name = input("Enter Lesson Name : ")
    teacher_name = input("Enter Teacher's Name : ")
    lesson_credits = int(input("Enter Lesson Credits : "))





    new_lesson = Curriculum(lesson_name,lesson_code, teacher_name ,lesson_credits )
    lesson_list.append(new_lesson)

    print("Saved.")
    print("-" * 15)
print("Study Info = " , new_lesson.__dict__)
print("Saved.")
print("-" * 15)


#for lesson in lesson_list :
 #   print(lesson)


