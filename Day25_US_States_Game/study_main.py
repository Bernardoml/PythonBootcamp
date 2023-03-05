# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")

# print(type(data))  # will tell that it's a 'DataFrame' ojb
# print(type(data))  # will tell that it's a 'Series' obj

# data_dict = data.to_dict()  # can change DF obj it to a dict easily
# temp_list = data['temp'].to_list()  # can change the series obj to a list easily

# TODO: calculate the average temperature
# temp_list = data["temp"].to_list()
# total = 0
# count = 0
# for elem in temp_list:
#     total += elem
#     count += 1
# average_temp = round((total / count), 2)
# print(average_temp)

# Done with pandas
# print(data["temp"].mean())

# TODO: get the max value from temperature column
# print(data["temp"].max())

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# TODO: get the temp for monday and convert from C to F
# def convert_to_f(temp_in_c):
#     return round((temp_in_c * 1.8) + 32, 1)
#
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(convert_to_f(monday_temp))


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# df = pd.DataFrame(data_dict)
# print(df)
# df.to_csv("new_data.csv")

# TODO: get the number of squirrels for each primary color
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # Short version, using value_counts
# fur_color = data["Primary Fur Color"]
# print(fur_color.value_counts())

# Long Version, counting each color and doing a new df
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
