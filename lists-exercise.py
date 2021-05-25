# Create a list to hold the to-do tasks.
to_do_list = []
is_finished = False
while not is_finished:
    task = input('Enter a task for your to-do list. Press <enter> when done: ')
    if len(task) == 0:
        is_finished = True
    else:
        to_do_list.append(task)
        print('Task added.')

# Display the to-do list
print()
print('Your to-do list.')
print('_' * 16)
for task in to_do_list:
    print(task)
