#import random
#import string

# User input
name = input("Enter your name: ")
age = input("Enter your age: ")
birthday = input("Enter your birthday (YYYY-MM-DD): ")

# If-Else Statements for Formatting
if name:
    name = name.title()  # Capitalizes first letter of each word
else:
    name = "Unknown"

if age.isdigit():
    age = f"{age} years old"
else:
    age = "Invalid age"

if birthday:
    try:
        year, month, day = birthday.split('-')
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        formatted_birthday = f"{months[int(month)-1]} {int(day)}, {year}"
    except:
        formatted_birthday = "Invalid date format"
else:
    formatted_birthday = "Unknown"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Birthday: {formatted_birthday}")


#charmander = " " + string.punctuation + string.digits + string.ascii_letters
#charmander = list(charmander)
#alicia_keys = charmander.copy()

#random.shuffle(alicia_keys)

# print(f'charmander: {charmander}')
# print(f'alicia_keys: {alicia_keys}')

#ENCRYPT
#plain_text = input('Enter the message to encrypt: ')
#cipher_text = ''

#for letter in plain_text:
    #index = charmander.index(letter)
    #cipher_text += alicia_keys[index]

#print(f'origial message: {plain_text}')
#print(f'encrypted message: {cipher_text}')

#DECRYPT
#cipher_text = input('Enter the message to decrypt: ')
#plain_text = ''

#for letter in cipher_text:
#    index = alicia_keys.index(letter)
#    plain_text += charmander[index]

#print(f'encryted message: {cipher_text}')
#print(f'original message: {plain_text}')