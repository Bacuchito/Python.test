#Create a grades.py program that checks whether a grade is above or below 55.
#Start by creating a variable called grade and give it a value that's between 0 and 100.
# # Grades 💯
import random

grade = random.randint(1, 100)

print(grade)

if grade >= 55:
    print('You passed.')
else:
    print('You failed.') 