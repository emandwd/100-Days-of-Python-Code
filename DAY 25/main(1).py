# readlines() → Reads the file line by line into a list of strings
# with open(r"C:\Users\emand\PyCharmMiscProject\.venv.p3.10\PYTHON COURSE DAY 25\weather_data.csv") as weather_data :
    #  WeatherData = weather_data.readlines()
    #   print(WeatherData)


# import csv
# with open("weather_data.csv") as data_file:
    # data = csv.reader(data_file)
    # tempreture = []
    # for row in data:
        # if row[1]!= "temp":
            # tempreture.append(int(row[1]))
    # print(tempreture)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"]) # pandas takes first row as a name of each column
print(type(data)) # the whole table called dataframe
print(type(data["temp"])) # part of the table called series

# convert into dictionary
data_dict = data.to_dict()
print(data_dict)

# convert into a list
temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list)) # check the length of the list


# calculate the average of the tempreture
sum = 0
data = pandas.read_csv("weather_data.csv")
data_temp = data["temp"]
for temp in data_temp:
    sum += temp
average = sum/len(data_temp)
print(float(average))


# or

print(data["temp"].mean())


print(data["temp"].max())
print(data["condition"])
print(data.condition)


# get the data in the row
print(data[data.day == "Monday"])


max_number = data["temp"].max()
print(data[data.temp == max_number])
# or
print(data[data.temp == data.temp.max()])


# get data in row
print(data[data.day == "Monday"])

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
