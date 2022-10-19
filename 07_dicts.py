# Dictionaries

my_dict =  dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Firsname':'Sergio', 'Lastname':'Lattke', 'Age':23}

print(my_other_dict)
print(type(my_other_dict))

my_dict = {
    'Firsname':'Sergio', 
    'Lastname':'Lattke', 
    'Age':23,
    'Lenguaje': {'Python', 'Nodejs', 'Javascript', 'Markdown'},
    1:1.70
}
print(my_dict)

my_dict['Firsname'] = 'Daniel'
print(my_dict['Firsname'])

my_dict['Street'] = 'Nelso ct'
print(my_dict)

del my_dict['Street']
print(my_dict)

print('Daniel' in my_dict)
print('Firsname' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(my_dict)
my_new_value = my_new_dict.values()

print(type(my_new_value))


print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))






