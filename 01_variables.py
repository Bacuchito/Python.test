# Variables
from sre_constants import SRE_FLAG_IGNORECASE


my_variable = 'My variable is too good'
print(my_variable)

first_name = 'Sergio' 
last_name = 'Lattke' 
country = 'venezuela'
age = 23
skills = ['javascript, python, git, github, Markdown']


bool = (3 > 5)
print(bool)

person_info = {
   'firstname':'Sergio',
   'lastname':'Lattke',
   'country':'Venezuela',
   'age':'23',
   'skills':'javascript, python, git, github, Markdown'
   }
print(person_info)

# concatenation
new_variable = str(age)
print(new_variable)
print(type(new_variable))
print('this is my name:', first_name)

# system functions
print(len(first_name))

# variables in one line
name, surname, gender, pets = 'Sergio', 'Lattke', 'Male', 5
print('my name is:', name, surname, 'i have:', pets, 'pest and im:', gender)


# inputs
print(input('What is your name?: '))
print(input('how old are you?: '))



