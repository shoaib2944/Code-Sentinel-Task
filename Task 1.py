import pandas as pd

df = pd.read_csv("C:/Users/Shoaib/Desktop/Code Sentinel Intern/Youtube Data.csv", engine="python", on_bad_lines="skip")
print("Number of Rows and Columns: ",df.shape, df.dtypes)
print(df.describe())