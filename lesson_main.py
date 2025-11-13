
from lesson_module import Curriculum
from lesson_module import *

study_list = []

try :
    for i in range(2):
        lesson_code = 0
        lesson_credits = 0
        lesson_name = input("Enter Lesson Name : ")
        lesson_code = int(input("Enter Lesson Code : "))
        teacher_name = input("Enter Teacher's Name : ")
        lesson_credits = int(input("Enter Lesson Credits : "))
        lesson = Curriculum(lesson_name, lesson_code, teacher_name, lesson_credits)
        lesson.validation()
        study_list.append(lesson)
        lesson.save()
        print(study_list)

        #study_list.append(new_lesson)
except Exception as e:
     print(f"Error: {e}")



#print("Study Info = " , new_lesson)
print("Saved.")
print("-" * 15)


#for lesson in lesson_list :
 #   print(lesson)


