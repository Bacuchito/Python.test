print('Bank of the world')

c = int(input('Put your pin code: '))

while c != 1234:
    c = (int(input('inccorect pin code, try again: ')))
    if c == 1234:
        print('PIN accepted')

