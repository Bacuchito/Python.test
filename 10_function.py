### function ###

def my_function (): 
    print('this is a function')

my_function ()

def sum_two_values (fisrt_number, second_number):
    print(fisrt_number + second_number)

sum_two_values(7, 8)
sum_two_values(123, 576)

def sum_two_new_values (first_value, second_value):
    return first_value + second_value

my_result = sum_two_new_values (23, 42)
print(my_result)

def print_name(name, surname):
    print(f'{name} {surname}')

print_name('sergio', 'lattke')

def print_name_with_default(name, surname, nickname = None):
    print(f'{name} {surname} {nickname}')

print_name_with_default('Sergio', 'Lattke',)

def print_texts(*text):
    for text in text:
        print(text.lower())

print_texts('Hello world', 'python', 'others')