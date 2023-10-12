# with open("weather_data.csv") as weather_data:
#   weathers = weather_data.readlines()
#   for weather in weathers:
#     weather.replace("\n", "")
#     print(weather)


# import csv

# with open("weather_data.csv", "r") as weather_data:
#   data = csv.reader(weather_data)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       temperatures.append(row[1])
#   print(temperatures)


import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


# Convert to dict.
# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


## Create a dataframe from scratch
# data_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("student_scores.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color = data["Primary Fur Color"]
grey_squirrels_count = len(data[primary_fur_color == "Gray"])
red_squirrels_count = len(data[primary_fur_color == "Cinnamon"])
black_squirrels_count = len(data[primary_fur_color == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
# fur_colors = primary_fur_color.dropna().unique().tolist()
# print(fur_colors)

# .nunique()
# black_fur = fur_color["black"].count()
# print(black_fur)
# # split_fur_color = fur_color.count()
# # print(split_fur_color)
# #Primary Fur Color