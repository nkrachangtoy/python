# Lists
# same as array
item_1 = 'cat'
item_2 = 'dog'
item_3 = 'rabbit'

list_name = [item_1, item_2, item_3]

# print(list_name[1])
# add an item to the list with .append()
list_name.append('cow')
# print(list_name[-1])

# add multiple items to the list with .extend()
# extend takes a list and append it
list_name.extend(['wolf', 'lizard', 'duck'])
# print(list_name)

more_items = ['bird', 'snake']
list_name.extend(more_items)
# print(list_name)

# add item anywhere in the list use insert(index, value)
# add 'bat' at index 3
list_name.insert(3, 'bat')
# print(list_name)


# Slices
# list[index1:index2]
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

some_animals = animals[1:4]
print('Some animals:    {}'.format(some_animals))

first_two = animals[0:2]
print('First two animals:   {}'.format(first_two))

# if first argument is not specify always start from first value in the list
first_two_again = animals[:2]
print('First two animals:   {}'.format(first_two_again))

# get last 2 items from the list list[-2:]
# -index = starts from the end of the list
# if index not specify after the 'colon' it assumes the length of the list
# this is a convinent way to do it, because we don't need to know the length of the list
last_two = animals[-2:]
print('Last two animals:    {}'.format(last_two))

# Exception Handling
# index
bear_index = animals.index('bear')
print(bear_index)

# if we try something that does not exist in the list
# Uncomment line 57 & 58 to see the error
# cat_index = animals.index('cat')
# print(cat_index)
"""We will get an error"""

# To prevent python from exiting out
# wrap everything is try: except:
try:
    bird_index = animals.index('bird')
except:
    bird_index = 'No birds found.'
# print(bird_index)

# Loops
# For loop
# for item_variable in list_name:
# Code block
for animal in animals:
    print(animal.upper())

# While loop
# while condition:
    # Code block

i = 0

while i > len(animals):
    print(animals[i])
    i += 1


# Sorted
sorted_animals = sorted(animals)
print(sorted_animals)

# CONCAT lists use '+'
list_one = ['one', 'two', 'three']
list_two = ['four', 'five', 'six']
all_lists = list_one + list_two
print(all_lists)

print(len(list_one))
list_one.append('somenum')
print(len(list_one))


# Ranges
# Comes in for loop

num_list = []

for number in range(5):
    num_list.append(number)

print(num_list)
