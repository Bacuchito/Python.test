# List

grocey_list = ['egg', 'avocados', 'cookies', 'hot pepper jam', 'blueberries', 'brocoli']

print(grocey_list)

todo_list = ['🏦 Get quarters', '🧺 Do laundry.', '🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.', 
'💻 Complete Lists chapter.', '💖 Call mom.', '📺 Watch My Hero Academia.' ]

print(todo_list[0])
print(todo_list[1])

print(todo_list[2:5])

# print(todo_list[9]) IndexError: list index out of range

#-------Inventory-------#

airplane_toys = [ 898, 732, 543, 878 ]

print(min(airplane_toys))
print(max(airplane_toys))

#--------reading books--------#

books_list = ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Made to Stick', 'Life in Code']

books_list.append('Zero to Sold')
books_list.remove('Zero to One')
books_list.pop(0)

print(books_list)

#-------- 💿 Theme: Indie Travel Songs-------#

playlist = [
   'Porches - rangerover',
   'Mount Eerie - You Swan, Go On',
   'Carolyn Polachek - Look at Me Now',
   'Pinegrove - Darkness'
   'LVP UP - Spirit Was',
   'Mitski - First Love / Late Spring',
]

print(playlist)

for i in playlist:
    print(i)

for i in range(len(playlist)):
    print(playlist[i])


things_to_do = [
   '💻 create my own project.',
   '🗺  Learn new lenguages',
   '🏡 buy a house in germany',
   '🌏 Live somewhere in Japon for a year.',
   '🎹 learn to play piano.',
   '📝 work for a big company',
   '📱 Be devOps',
   '👾 create a video game',
   '👴 Grow old with no regrets.'
]
for i in things_to_do:
    print(i)
