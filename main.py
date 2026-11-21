import random
import string

print("=== Strong Password Generator ===")
print("Made by Md Faruque Hosain")

# How long password?
length = int(input("How many characters? (ex: 12): "))

# All characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_chars = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_chars)

print("\nYour Strong Password is:")
print(password)
print("\nCopy it and keep it safe! 🔐")
