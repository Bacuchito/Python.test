# 99 Bottles of Beer 🍻
# Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer"
# String concatenation

for i in range(5):
    print(f"The square of  + {i} +  is  + {i*i}")


for a in range(99, 0, -1):
    print(f'{a} bottles of beer on the wall')
    print(f'{a} bottles of beer')
    print(f'Take one down, pass it around')
    print(f'{a - 1} bottles of beer on the wall')


