import random
import string

print("===================================")
print("      PASSWORD GENERATOR 🔐")
print("===================================")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    random_char = random.choice(all_characters)
    password += random_char

print("\n===================================")
print(" Generated Password:", password)
print("===================================")
print(" Strong Password Created Successfully ✅")