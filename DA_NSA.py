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

class RegionPeriod :
    def __init__(self, region, period):
        self.region = region
        self.period = period

# loops through the input to select the region and period of time wanted
    def Region(self):
        global region_df, time_period
        if self.region.lower() == "europe":
            region_df = df[["Date", "United Kingdom", "France", "Germany", "Italy", "Netherlands", "Greece", "Belgium & Luxembourg", "Switzerland",
                            "Austria", "Scandinavia", "CIS & Eastern Europe"]]
        elif self.region.lower() == "asia":
            region_df = df[['Date', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines','Thailand', 'Viet Nam', 'Myanmar', 'Japan', 'Hong Kong', 'China',
                            'Taiwan', 'Korea, Republic Of', 'India', 'Pakistan', 'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE']]
        elif self.region.lower() == "others":
            region_df = df[['Date', 'USA', 'Canada','Australia', 'New Zealand', 'Africa']]
        else:
            print('End')

        if self.period == "4":
            time_period = region_df[region_df['Date'].between('2008-01-01', '2017-12-31')]
            #print(time_period)
        elif self.period == "3":
            time_period = region_df[region_df['Date'].between('1998-01-01', '2007-12-31')]
        elif self.period == "2":
            time_period = region_df[region_df['Date'].between('1988-01-01', '1997-12-31')]
        elif self.period == "1":
            time_period = region_df[region_df['Date'].between('1978-01-01', '1987-12-31')]
        else:
            print("End")


#calls the function inside the class
#selects europe region and time period of 2008 to 2017
RegionPeriod("Europe", "4").Region()

#prints the final df for testing
final_df = time_period
#print(final_df)


#finds the total sum of visitors throughout the 10 years from 2008 to 2017 and sorts descending
totalvisitors_series = final_df.sum().sort_values(ascending=False)
totalvisitors_df = pd.DataFrame({'Countries':totalvisitors_series.index, 'Total Visitors':totalvisitors_series.values})
totalvisitors_top3_df = totalvisitors_df[:3]

#plots the bar chart
ax = totalvisitors_top3_df.plot(x = 'Countries',y = 'Total Visitors',kind = 'bar')

plt.title('Top 3 countries in Europe over a span of 10 years from 2008 to 2017.')
plt.xlabel('Countries')
plt.ylabel('Total Visitors')

#formats the plot to adjust the rotation of x value labels and tightens the plot into a smaller size
#to show the xlabels and ylabelss
plt.xticks(rotation = 25)
plt.ticklabel_format(axis="y", style='plain')
ax.bar_label(ax.containers[0], label_type='edge', fmt = '%d')
plt.tight_layout()

#shows the bar plot and prints the top 3 countries
print(totalvisitors_top3_df)
plt.show()

#doing testcase with the help of unittest library
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#sehy