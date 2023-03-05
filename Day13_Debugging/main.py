############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# * This one is bugged because the range function will include 'a' and exclude 'b'
# * it will produce a, a+1, a+2, ..., b-1. But not 'b'

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# * The dice list is [0] through [5], but the randint function will generate
# * a number from 1 through 6, so the first item will never be printed
# * and on the other side, '6' will produce an index out or range error.

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# * The year 1994 is excluded from the logical tests
# * year < 1994 and year > 1994, both excluding the 1994 year

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# * input should be casted as int function that way it won't show
# * the 'cannot evaluate srt > int' Type error
# * The other error is print statement not being indented in the if block
# * The third error is the not formated f string {age}.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# * word_per_page == int >> This will evaluate to True or False
# * Then it will generate the wrong number multiplying by 0

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# * This one will only append the last new_item to b_list
# * since the append is not in the indented if block