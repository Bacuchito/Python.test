# List

from ipaddress import collapse_addresses


my_list = [24, 54, 23, 12, 27, 24, 49]

print(my_list)
print(type(my_list))
print(len(my_list))

my_other_list = ['sergio', 'lattke', 23, 1.70, ]

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])

print(my_list.count(24)) #return number of occurences of value

name, surname, age, height = my_other_list
print(name)
print(age)

my_other_list.append('cat') # append object to the end of the list
print(my_other_list)

my_other_list.insert(3, 'milk') # insert a object in the number 3
print(my_other_list)

my_list.remove(23) # remove the value
print(my_list)

del my_list[2]  # delete the value
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

my_other_list[3] = 'coke' #change the value
print(my_other_list)

my_new_list = my_list.copy()

my_list.clear() # delete all or clear all
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

print(my_new_list[1 : 4])

my_new_list.sort()
print(my_new_list)
