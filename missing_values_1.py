import pandas as pd

df = pd.read_csv("D:\pythonp/train.csv")

a = df["Age"].isnull()
b = len(a)

a1 = df["Age"]
c = a == False

d = df["Age"][a == False]

d1 = a1[c]   #filtering



print(d1)
sum_d1 = sum(d1)
print(sum_d1)


print()
print()
#print(d)


#print(a)
#print(b)
#print(c)