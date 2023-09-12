import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_col = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_col = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_col = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_col)
print(cinnamon_col)
print(black_col)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_col, cinnamon_col, black_col]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_color_count.csv")

print(data_dict)
print(df)
