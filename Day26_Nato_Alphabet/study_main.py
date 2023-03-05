# List Comprehension will work with sequences in python
# Sequences are ordered - List, String, Range, Tuple

# List Comprehension will create another list from existing list
# new_list = [new_item for item in list]
# primes = [1, 2, 3, 5, 7, 11]
# primes_squared = [item ** 2 for item in primes]
# print(primes)
# print(primes_squared)

# List Comprehension can be used with strings
# new_list = [new_item for item in string]
# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# List Comprehension can also be used with range
# new_list = [new_item for item in range(x, y)]
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# List Comprehension can also be used with tuples
# primes_tuple = (1, 2, 3, 5, 7, 11)
# tuple_list = [item ** 2 for item in primes_tuple]
# print(primes_tuple)
# print(tuple_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 4]
# print(names)
# print(short_names)
# print(long_names)

# Dictionary Comprehension - Creating from a list
# new_dict= {new_key:new_value for item in list}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {name: random.randint(1, 100) for name in names}
# print(students_scores)

# Dictionary Comprehension - Creating from a dict
# new_dict= {new_key:new_value for (key, value) in dict.items()}
# Conditional Dictionary Comprehension
# new_dict= {new_key:new_value for (key, value) in dict.items() if test}
# passed_students = {key: value for (key, value) in students_scores.items() if value >= 60}
# print(passed_students)


# How to iterate over a Pandas DataFrame
# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lilly"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(f"{key}: {value}")
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Looping through a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

# Looping through rows of a data frame and printing each row
# for (index, row) in student_data_frame.iterrows():
#     print(row)

# Looping through rows of data and printing an exact score
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)
