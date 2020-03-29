import pandas as pd

file = open('nepnews.csv', encoding='utf8', errors='ignore')

df = pd.read_csv('nepnews.csv', encoding='utf8', header=None)
df1 = df[1:3]
print(df.head(6))
