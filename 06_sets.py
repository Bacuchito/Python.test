# Sets 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {'Sergio', 'lattke', 23, 1.70}

print(type(my_other_set))
print(len(my_other_set))

my_other_set.add('Bacuchito') # a set is not an ordered structure and does not support repeated
print(my_other_set)

print('sergio' in my_other_set )
print('Sergio' in my_other_set )

my_other_set.remove(1.70)
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {'python', 'javascript', 'markdown'}
print(type(my_set))

my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {'Sergio', 'lattke', 23, 1.70}
my_new_set = (my_set.union(my_other_set).union(my_set).union({'java', 'nodejs'})) # sets cant duplicate

print(my_new_set)

print(my_new_set.difference(my_other_set))









