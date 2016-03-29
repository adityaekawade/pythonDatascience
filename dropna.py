import pandas as pd
import numpy as np

df = pd.read_csv("D:\pythonp/train.csv")

a = df.dropna(subset=["Age"])

print(a)
