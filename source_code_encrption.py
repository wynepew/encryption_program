import random
import string

charmander = " " + string.punctuation + string.digits + string.ascii_letters
charmander = list(charmander)
alicia_keys = charmander.copy()

random.shuffle(alicia_keys)

# print(f'charmander: {charmander}')
# print(f'alicia_keys: {alicia_keys}')

#ENCRYPT
plain_text = input('Enter the message to encrypt: ')
cipher_text = ''

for letter in plain_text:
    index = charmander.index(letter)
    cipher_text += alicia_keys[index]

print(f'origial message: {plain_text}')
print(f'encrypted message: {cipher_text}')