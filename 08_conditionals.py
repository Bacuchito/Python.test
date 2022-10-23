# conditionals

my_conditions = 5 * 5

if my_conditions == 11:
    print('hello')
else:
    print('the conditional is false')


if my_conditions >= 10 and my_conditions <= 20:
    print('the conditional is true')
else:
    print('the conditional is false')


if my_conditions > 10 and my_conditions < 20:
    print('the conditional is true')
elif my_conditions > 20:
    print('The conditional is more than 20')
else:
    print('the conditional is false')


my_string = 'hello'
my_other_string = ''

if my_string:
    print('the string is not clear')

if not my_other_string:
    print('the other string is clear')


