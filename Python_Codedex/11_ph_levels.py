# Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.
#First, create a variable called ph and ask the user for a value between 0 and 14.
# pH Levels 🧪

pH = int(input('Enter a pH level (0-14): ', 'hello: '))

if pH > 7:
    print('Basic')
elif pH <7:
    print('Acidic')
else:
    print('Neutral')
