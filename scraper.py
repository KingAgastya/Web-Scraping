from turtle import width
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page  = requests.get(START_URL)
soup = bs(page.text, "html.parser")

star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')

    row = [i.text.rstrip() for i in td]
    
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df2 = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ['Star_Name', 'Distance', 'Mass', 'Radius'])

print(df2)
df2.to_csv('bright_stars.csv')
