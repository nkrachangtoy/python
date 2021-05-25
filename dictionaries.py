# Dictionaries
# Hold key-value pairs called items
# AKA associative arrays, hash tables and hashes

# dictionary_name = {key_1: value_1, key_N: value_N}
# dictionary_name = {}
# dictionary_name[key]

contacts = {'Jason': '555-0123', 'Carl': '555-4321'}
# Get value from key
jasons_phone = contacts['Jason']
carls_phone = contacts['Carl']

# print('Dial {} to call Jason.'.format(jasons_phone))
# print('Dial {} to call Carl.'.format(carls_phone))

# Set value to key
contacts['Jason'] = '555-0000'
new_jasons_phone = contacts['Jason']
print('Dial {} to call Jason.'.format(new_jasons_phone))

# Add new key and value to dictionary
contacts['Tony'] = '555-5678'
print(contacts)
print(len(contacts))

# Delete key from dictionary
del contacts['Tony']
print(contacts)

new_contacts = {
    'Aiden': ['555-1234', '555-0987'],
    'Dream': '555-4335'
}

# .values() to check if the value exist
# print('Does the value exist in the dictionary: {}'.format(
#     '555-0976' in new_contacts.values()))

# print('Does the value exist in the dictionary: {}'.format(
#     '555-4335' in new_contacts.values()))

# Looping through dictionary with for loop
for number in new_contacts['Aiden']:
    print('Phone:   {}'.format(number))


# We can check whether the key exist in the dictionary
if 'Aiden' in new_contacts.keys():
    # this is True and cuz 'Aiden' exist in the dictionary
    print("Aiden's phone number is: ")
    print(new_contacts['Aiden'][0])


# This will not be executed since 'Tony' does not exist
if 'Tony' in new_contacts.keys():
    print("Tony's phone number is: ")
    print(new_contacts['Tony'][0])
