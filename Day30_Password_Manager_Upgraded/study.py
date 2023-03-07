# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existend_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:  # Runs when the error occurs
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:  # Runs when the error occurs
#     print(f"The key {error_message} does not exist.")
# else:  # Run when there is no error
#     content = file.read()
#     print(content)
# finally:  # Run no matter what happens
#     file.close()

# When you actually want to generate an Exception/Error use the raise handle
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
