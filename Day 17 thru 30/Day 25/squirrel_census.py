
SQUIRREL_PATH = 'resource/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250830.csv'
import pandas

content = pandas.read_csv(SQUIRREL_PATH)

color_counts = content["Primary Fur Color"].value_counts()

color_counts_df = color_counts.reset_index()
color_counts_df.columns = ["Fur Color", "Count"]

color_counts_df.to_csv("resource/squirrel_count.csv")

print(color_counts_df)
#===================================================================================
