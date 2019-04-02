import pandas as pd

fields = ['iid', 'id', 'gender', 'idg', 'condtn', 'wave', 'round', 'order', ]
data = pd.read_csv("Speed Dating Data.csv", encoding="windows-1252", skipinitialspace=True, usecols=fields)

testing_data = data.head()

print(testing_data)
