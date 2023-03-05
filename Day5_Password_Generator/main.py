import random
import string


print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your generator?\n"))
num_symbols = int(input("How many symbols would you like in your generator?\n"))
num_numbers = int(input("How many numbers would you like in your generator?\n"))

special_characters = "!@#$%¨&*()"

password = []
password.extend([random.choice(string.ascii_letters) for n in range(num_letters)])
password.extend([random.choice(special_characters) for n in range(num_symbols)])
password.extend([random.choice(string.digits) for n in range(num_numbers)])

random.shuffle(password)
output = "".join(password)

print(f"Here is your password: {output}")
