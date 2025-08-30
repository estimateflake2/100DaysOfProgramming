#======================= Working with CSV files using Pandas
#====== End Game, to guess and name all the states in the United States.
from numpy.ma.extras import average

RESOURCE_PATH = 'resource/weather_data.csv'
#=========================================================================================
# import os
#
# if os.path.exists(RESOURCE_PATH):
#     with open(RESOURCE_PATH) as f:
#         content = f.readlines()
#
#         print (content)
# else:
#     print("not a file")
#=========================================================================================
# import csv
# import os
#
# if os.path.exists(RESOURCE_PATH):
#     with open(RESOURCE_PATH) as f:
#         content = csv.reader(f)
#         temperature = []
#         for row in content:
#             print (row)
#             try:
#                 temperature.append(int (row[1]))
#             except:
#                 pass
#         print (temperature)
#=========================================================================================
##============ WORKING WITH PANDAS
import pandas
import math

content = pandas.read_csv(RESOURCE_PATH)
# print (content )
# print (content ['temp'][0])
# #>>>>>>>>>>>> using [type] to determine data type
#
# #===> Pandas Data Structure (Series vs Data Frame)
# #Data Frame: A single sheet in a cvs file (content)
# #Series: equivalent to a list or a column in a table. (content['temp'])
#
# data_dict = content.to_dict()
# print (data_dict)
# print (data_dict['temp'][1])
#
# data_list = content['temp'].to_list()
# print ("average==>", average(data_list))
# print ("average==>", content['temp'].mean())

monday = content[content.day == "Monday"]
print(monday)

#Creating DataFrame from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scroe": [76,56,65]
}

data = pandas.DataFrame(data_dict)
print (data)

data.to_csv("resource/new_data.csv")



















