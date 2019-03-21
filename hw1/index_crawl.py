import csv
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver

# Web crawler for Capacity untilization 
url = 'https://www.federalreserve.gov/datadownload/Download.aspx?rel=G17&series=f213ee970e317c0f3cc80e775d35b8e5&filetype=csv&label=include&layout=seriescolumn&lastObs='
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(20)
driver.get(url)

# Find the download button's element
download_element = driver.find_element_by_xpath('//*[@id="DataURL"]')

# Save the historical data csv file into dataframe
csv = download_element.get_attribute('href')
df = pd.read_csv(csv)

# Remove the first 234 rows 
df = df.drop(df.index[0:233], axis = 0)

# Save the first 2 columns and remove the other
df = df.drop(df.columns[2:], axis = 1)
df = df.reset_index(drop = True)

# Rename the name of cols and rows
df = df.rename(columns = {'Series Description':'Date'})
df = df.rename(columns = {'Total index; s.a. CAPUTL':'Value'})

# Change the date values (from yyyy-mm to yyyy-mm-dd )
Dates = []
for date in df['Date']:
	Dates.append(date + '-01')

df['Date'] = Dates

# pirnt the first 20 elements
print(df.head(20).to_string(index=False))
