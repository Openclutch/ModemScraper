from bs4 import BeautifulSoup
import csv
import requests
import time

page = requests.get("http://192.168.100.1/Diagnostics.asp")

# get datetime for filename
datetime = time.strftime("%Y-%m-%d %H-%M")

# debugging while at work, comment out above and change how it's called below
# html = open("index.html").read()

soup = BeautifulSoup(page.content, 'html.parser')
allTables = soup.find_all('table', class_='light1')

# Manually select the table since there aren't any identifiers
table = allTables[1]

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.encode('utf-8'))
    output_rows.append(output_row)

# Manually pop since I don't have time to figure out glitch above
output_rows.pop(2)
output_rows.pop(12)

filename = datetime + '.csv'

with open('data/' + filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
