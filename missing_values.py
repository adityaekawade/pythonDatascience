import pandas as pd

df = pd.read_csv("D:\pythonp/train.csv")

number_of_values = len(df["Age"])
age_null_count = sum(df["Age"].isnull())


#print(df["Age"].isnull())
print(age_null_count)
print(number_of_values)
print(number_of_values - age_null_count)


sum_of_age = sum(df["Age"])  #results in nan
print(sum_of_age)
print("avg age = " , sum_of_age / number_of_values )
