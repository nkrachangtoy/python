# Exercise 1
# Variables
animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'
# Print statements
print('Here is an animal, a vegetable, and a mineral.')
print(animal)
print(vegetable)
print(mineral)

# Exercise 2
# Get the input from the user.
user_input = input('Please write something and press enter: ')
print('You entered: {}'.format(user_input))

# Exercise 3
# Get the input from the user.
text = input('What would you like the cat the say ')
# Determine the length of the input
text_length = len(text)

# Make the border the same size as the input
print('  {}'.format('_' * text_length))
print('< {} >'.format(text))
print('  {}'.format('_' * text_length))
