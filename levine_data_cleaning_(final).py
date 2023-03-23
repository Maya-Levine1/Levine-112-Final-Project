# -*- coding: utf-8 -*-
"""Levine Data Cleaning (Final)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10uwShgePU2OlXrHvG2uPMTEfuqKgT3CD

# business (If I say "we" it's becas

Goals 

*   Get specific mileage types in 2009
*   Get death types in 2009 by state
*   Get land death types in 2009 by state 
*   Combine mileage/states/land in 2009
*   Get deaths over time 
*   Get mileage over time 
* combine death/milesage over time

CSVs to upload


*   road miles
*   deaths by time
*   miles_years
*  land

CSVs created
* years

# Mileage over time
"""

import pandas as pd
miles_years=pd.read_csv("miles_years.csv")
miles_years

"""# Deaths over time"""

over_time1=pd.read_csv("deaths by time.csv") 
over_time2=over_time1.drop(columns=['Unnamed: 4', 'Unnamed: 5'])
over_time=over_time2.drop(46)
over_time

for i in range(0,46):
  over_time.loc[i]=over_time.loc[i].str.replace(",","")

"""# Join by time, death and mileage """

over_time=over_time.astype(int) 
miles_years=miles_years.astype(int)
years=over_time.merge(miles_years, on="Year",how="inner")
years.to_csv('years',index=False)
years

"""# Specific mileage types in 2009 (df_relevant)"""

import pandas as pd
road_type=pd.read_csv("Road miles.csv") 
df_relevant1 = road_type.drop(columns=["R-INTERSTATE",	"R-PRINCIPAL ARTERIAL",	"R-MINOR ARTERIAL",	"R-MAJOR COLLECTOR",	"R-MINOR COLLECTOR",	"R-LOCAL 2/",	"U-INTERSTATE",	"U-OTHER EXPRESSWAY","U-PRINCIPAL ARTERIAL",	"U-MINOR ARTERIAL",	"U-COLLECTOR",	"U-LOCAL"])
df_relevant= df_relevant1.drop([8,52,53])

"""# Specific death stats in 2009 (deaths)"""

import requests
response = requests.get(
    "https://www.iihs.org/topics/fatality-statistics/detail/state-by-state")

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

len(soup.find_all("table"))

crashes = soup.find_all("table")[0]

states=[]
for row in crashes.find_all("tr"):
  state = (row.find("th").text)
  states.append(state)

df_states=pd.DataFrame(states[2:])
df_states

data =[]

for row in crashes.find_all("tr"):
  new_data = []
  for cell in row.find_all("td"):
    new_data.append(cell.text)
    data.append(new_data)

df=pd.DataFrame(data).iloc[::6,:]
df1=df.reset_index()
df_data=df1.drop(["index"], axis=1)
df_data

joined1 = pd.merge(df_states, df_data, left_index=True, right_index=True)
deaths = joined1.rename(columns={"0_x":"STATE", "0_y":"Population",1:"VMT (Millions)",2: "Fatal_Crashes",
                       3:"Deaths",4:"Deaths per 100K",5:"Deaths per 100M VMT"
                       },inplace=False)

for i in range(0,51):
  deaths.loc[i]=deaths.loc[i].str.replace(",","")

deaths

"""# Death by land type (land)"""

land1=pd.read_csv("land type.csv")
land=land1.drop([8])
land

"""# Merging deaths/road mileage/land in 2009"""

#Things are: 
#df_relevant
#deaths 
#land
crash_data1=deaths.merge(df_relevant, on="STATE",how="outer")
crash_data2=crash_data1.merge(land, on="STATE",how="outer")
crash_data=crash_data2.drop([8,51,53,54])

crash_data.to_csv('crash_data',index=False)