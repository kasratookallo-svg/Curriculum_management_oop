# Curriculum Designing Program
# Made By Kasra Tookallo

from lesson_module import Curriculum
from lesson_module import *

study_list = []

try :
    for i in range(2):
        #Getting Lesson information
        lesson_code = 0
        lesson_credits = 0
        lesson_name = input("Enter Lesson Name : ")
        lesson_code = int(input("Enter Lesson Code : "))
        teacher_name = input("Enter Teacher's Name : ")
        lesson_credits = int(input("Enter Lesson Credits : "))
        lesson = Curriculum(lesson_name, lesson_code, teacher_name, lesson_credits)
        lesson.validation()
        study_list.append(lesson)
        print("-" * 150)
        lesson.save()
        print("-" * 150)

        print("Your Stduies include : ",study_list)
        print("-" * 150)


except Exception as e:
     print(f"Error: {e}")

print("Saved.")
print("-" * 150)
