import random
import string

# define password length
length = 12

# define characters to be used in password generation
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

# combine all characters
all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

# generate random password
password = ''.join(random.sample(all_characters, length))

# print the generated password
print("Your password is:", password)
