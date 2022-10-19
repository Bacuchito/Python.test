# tuples

my_tuples = tuple() 
my_other_tuple = (21, 54, 12)

my_tuples = ('sergio', 'lattke', 23, 1.70, 23)
print(my_tuples)
print(type(my_tuples))

print(my_tuples[2])
print(my_tuples[0])

print(my_tuples.count(23))
print(my_tuples.index('lattke'))

my_sum_tuple = my_tuples + my_other_tuple

print(my_sum_tuple)
print(my_sum_tuple[2:5])

my_tuples = list(my_tuples)
my_tuples.insert(1, 'Daniel')

my_tuples = tuple(my_tuples)
print(type(my_tuples))

del my_tuples   
# print(my_tuples)   #NameError: name 'my_tuples' is not defined