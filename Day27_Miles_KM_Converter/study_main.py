# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# # Made with list comprehension, since *args is a tuple
# def add(*args):
#     return sum([num for num in args])
#
#
# print(add(1, 2, 3, 4, 5))


# # *args = tuple of infinite number of arguments
# # **kwargs = dict of infinite number of keyword arguments
# def calculate(n, **kwargs):
    # You can loop through the **kwargs dict with for loop and dict.items()
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # Since it's a dict, you can access like this kwargs["add"]
    # it will return 3
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


# # Creating a class with **kwargs
# class Car:
#     def __init__(self, **kw):
#         self.maker = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(maker="Nissan", model="GT-R")  # this will do fine, since both arguments are passed
# my_car2 = Car(maker="Nissan")  # this will generate an error, since the model argument wasn't passed

# # Creating a class with **kwargs and using the get method to fetch the key
# # the get method will return None if they kwarg wasn't passed
# # so that it won't create an error
# class Car:
#     def __init__(self, **kw):
#         self.maker = kw.get("maker")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(maker="Nissan", model="Skyline", color="Black")
# print(my_car.maker)
# print(my_car.model)
# print(my_car.color)
# print(my_car.seats)

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Put padding around the window

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# after creating the object, you can alter the elements in two ways
my_label["text"] = "New Text"  # accessing the attribute
my_label.config(text="Newest Text")  # using the config command, may pass more attributes


# Button
def button_clicked():
    print("I got clicked.")
    new_text = tk_input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
tk_input = tkinter.Entry(width=10)
tk_input.grid(column=4, row=4)

window.mainloop()
