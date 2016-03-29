import pandas as pd
import numpy as np

df = pd.read_csv("D:\pythonp/train.csv")

passenger_age = df.pivot_table(index="Pclass", values="Age", aggfunc=np.mean)
print(passenger_age)

port_stats = df.pivot_table(index="Embarked", values=["Age", "Survived", "SibSp", "Fare"], aggfunc=np.mean)
print(port_stats)
