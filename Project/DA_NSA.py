#import necessary libraries needed
import numpy as np, pandas as pd, matplotlib.pyplot as plt, openpyxl

#import excel file into a dataframe
df_raw = pd.read_excel('./Project_File.xlsx')

# copy the raw data into a separate variable that will be cleaned
df = df_raw

# Cleaning the columns by removing whitespaces and renaming the first column to "Date" to access the dates easier
df.columns = df.columns.str.strip()
df = df.rename(columns={'' : 'Date'})
#Convert Year-Month dates to an actual datetime
df['Date'] = pd.to_datetime(df['Date'])

Europe = ["United Kingdom", "Germany", "France", "Italy", "Netherlands", "Greece", "Belgium & Luxemburg", "Switzerland", "Austria"]

print(df)
print(Europe)