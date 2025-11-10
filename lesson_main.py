import self

from lesson_module import *

for i in range(2):
    lesson_code = 0
    lesson_credits = 0
    Lesson_code = int(input("Enter Lesson Code : "))
    lesson_name = input("Enter Lesson Name : ")
    teacher_name = input("Enter Teacher's Name : ")
    lesson_credits = int(input("Enter Lesson Credits : "))





    new_lesson = Curriculum(lesson_name,lesson_code, teacher_name ,lesson_credits )
    add_lesson()

  #  print("Saved.")
   # print("-" * 15)
#print(new_lesson.__dict__)
   # print("Saved.")
    #print("-" * 15)


for lesson in self.lesson_list :
    print(lesson)
    print("Study Info = ",lesson.__dict__)

