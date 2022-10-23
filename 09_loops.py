# Loops

# while
my_conditional = 0

while my_conditional < 10:
    print(my_conditional)
    my_conditional += 1
else: 
    print('the loop continue')

while my_conditional < 20:
    print(my_conditional)
    my_conditional += 1
    if my_conditional == 15:
        print('the loop has stoped')
        break
    print(my_conditional)

# For

my_list = ['sergio', 'lattke', 23, 1.70, ]
for element in my_list:
    print(element)

my_tuples = ('sergio', 'lattke', 23, 1.70, 23)
for element in my_tuples:
    print(element)

my_set = {'python', 'javascript', 'markdown'}
for element in my_set:
    print(element)

my_dict= {'Firsname':'Sergio', 'Lastname':'Lattke', 'Age':23}
for element in my_dict:
    print(element)
else:
    print('the loop has done')

my_dict= {'Firsname':'Sergio', 'Lastname':'Lattke', 'Age':23}
for element in my_dict:
    print(element)
    if element == 'age':
        break

my_dict= {'Firsname':'Sergio', 'Lastname':'Lattke', 'Age':23}
for element in my_dict:
    print(element)
    if element == 'age':
        continue
else:
    print('the loop has done')
    
