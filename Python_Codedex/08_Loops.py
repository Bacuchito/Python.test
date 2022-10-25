# Pin

from sys import intern


print('Bank of Bacu')

pin = int(input('What is your ping code?: '))

while pin != 1234:
    pin = int(input('incorrect ping code, try again: '))

    if pin == 1234:
        print('PIN accepted!')

# guess

guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input('Gues the number:   '))
    tries = tries + 1

if guess != 6:
    print('You ran out of tries')
else:
    print('You got it!')


