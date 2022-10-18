# strings

simple_string = ('Get ready for the next battle')
my_string = ('Good jobs team')

print(len(simple_string))
print(len(my_string))

# Other string

print('hello\neveryone') #using \n
print('\thello everyone') # using \t

# format 
name, surname, age = 'sergio', 'lattke', 23 
print('my name is {} {} and im {} years old' .format(name, surname, age))
print('my name is %s %s and im %d years old' %(name, surname, age)) 
print(f'my name is {name} {surname} and im {age} years old')

#Sequences of Characters
language = 'python'
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# division
language_slice = language[ : : -1]
print(language_slice)

# function 

print(language.capitalize()) # uppercase the first letter
print(language.upper())  # uppercase all
print(language.count('t')) # count how many t have Python
print(language.isnumeric()) # Python is numeric? false
print(language.lower()) # lowercase all 
print(language.upper().isupper()) #uppercase all and PYTHON is upper? true
print(language.startswith('py')) # python starts with py?