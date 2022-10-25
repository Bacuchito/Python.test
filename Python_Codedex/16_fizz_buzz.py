#Create a fizz_buzz.py program that outputs numbers from 1 to 100. Here's the catch:
'''For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".'''
# Fizz Buzz 🐝

for i in range(1, 101):
    if i % 4 == 0 and i % 9 == 0:
        print('fizzbuzz')
    elif i % 4 == 0:
        print('fizz')
    elif i % 9 == 0:
        print('buzz')
    else:
        print(i)

