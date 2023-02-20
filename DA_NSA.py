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

print(df.columns)
class RegionPeriod :
    def __init__(self, region, period):
        self.region = region
        self.period = period

# loops through the input to select the region and period of time wanted
    def Region(self):
        global region_df, time_period
        if self.region == "europe":
            region_df = df[["Date", "United Kingdom", "France", "Germany", "Italy", "Netherlands", "Greece", "Belgium & Luxembourg", "Switzerland",
                            "Austria", "Scandinavia", "CIS & Eastern Europe"]]
        elif self.region == "asia":
            region_df = df[['Date', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines','Thailand', 'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China',
                            'Taiwan', 'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE']]
        elif self.region == "others":
            region_df = df[['Date', 'USA', 'Canada','Australia', 'New Zealand', 'Africa']]
        else:
            print('End')

        if self.period == "4":
            time_period = region_df[region_df['Date'].between('2008-01-01', '2018-12-31')]
            #print(time_period)
        elif self.period == "3":
            time_period = region_df[region_df['Date'].between('1998-01-01', '2007-12-31')]
        elif self.period == "2":
            time_period = region_df[region_df['Date'].between('1988-01-01', '1997-12-31')]
        elif self.period == "1":
            time_period = region_df[region_df['Date'].between('1978-01-01', '1987-12-31')]
        else:
            print("End")

#asks for input of region and period of time wanted
region = input("Regions available: Asia, Europe, Others\n"
               "Insert region needed : ").lower()
period = input("\nPeriods available:\n"
               "1 = 1978-1987\n"
               "2 = 1988-1997\n"
               "3 = 1998-2007\n"
               "4 = 2008-2017\n"
                "Insert period needed : \n")

#calls the function insided the class
RegionPeriod(region, period).Region()

#prints the final df
final_df = time_period
print(final_df)

#stuck here
#group = final_df.groupby(final_df['Date'].dt.year)
#print(group.describe())