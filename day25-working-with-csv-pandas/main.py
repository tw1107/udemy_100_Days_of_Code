
# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
#
# avg_temp = data["temp"].mean()
# print(f"Average temperature: {avg_temp}")
#
# max_temp = data["temp"].max()
# print(f"Max temperature: {max_temp}")
#
# data_dict = data.to_dict()
# print(data_dict)
#

# #Get data in columns
# print(data["condition"])
# print(data.condition)

#Get data in Row
# print(data[data.day == "Monday"])

# Get the row of max temp
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Alice"],
#     "scores": [76, 80, 90]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = ["Gray", "Cinnamon", "Black"]

squirrel_color = df[df["Primary Fur Color"].isin(color)]

result = squirrel_color.groupby("Primary Fur Color").size().to_frame("Count").reset_index()
result.rename(columns={"Primary Fur Color":"Fur Color"}, inplace=True)

result.to_csv("squirrel_count.csv")
