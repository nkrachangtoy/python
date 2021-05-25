# Tuples
# A tuple is an immutable list
# Once it's defined, it can't be changed

# tuple_name = (item_1, item_2, item_n)
# tuple_name = (item_1,)
# Access item in tuple list tuple_name[index]

# Use tuple when the data should not be change

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days_of_the_week[0]
print(monday)
# We can treat tuple as a list
# for looping it
for day in days_of_the_week:
    print(day)

# But cannot alter the value in the list
# days_of_the_week[0] = 'New Monday'


# Turn tuple into list
weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
# type() to display type of object
print('Weekend_turple is {}'.format(type(weekend_tuple)))
print('Weekend_list is {}'.format(type(weekend_list)))

# use tuple to assign multiple values at once
weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)


# use tuple to assign with list
contact_info = ['555-0123', 'jason@example.com']
# tuple
(phone, email) = contact_info
print(phone)
print(email)


# Use tuple in function
def high_and_low(numbers):
    # Determine the highest and lowest number
    highest = max(numbers)
    lowest = min(numbers)
    return(highest, lowest)


lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is : {}'.format(highest))
print('The lowest number is : {}'.format(lowest))


# Use tuple in assignment list
contacts = [('Jason', '555-0123'), ('Carl', '555-1234')]

for (name, phone) in contacts:
    print('{}: {}'.format(name, phone))


# Delete tuple
del contact_info
# print(contact_info)
