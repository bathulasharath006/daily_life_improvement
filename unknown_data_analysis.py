import pandas as pd

pd.set_option('display.max_columns', None) # display all columns of a DataFrame, no matter how many there are.
pd.set_option('display.max_colwidth', None) # display the full content of each column's cell, regardless of length.

df = pd.read_excel("file.xlsx")

df.shape # Get (rows, cols)

df.head()

df.info()

df.describe() # Add .transpose() , if you want different orientation.

# Print each column's value_counts.

for col in df.columns:
    print(f"Value counts for column: {col}")
    print(df[col].value_counts())
    print("\n" + "-"*50 + "\n")


