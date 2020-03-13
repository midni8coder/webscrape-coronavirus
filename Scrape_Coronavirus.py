#
# Author: Devid Lingampally https://in.linkedin.com/in/devidlingampally
# Date: March 14 2020 
# Description: To fetch updated data about Coronavirus and storing it in csv file
# Purpose: This Web Scraping is for analysis purpose only. Not used for any business/commercial purpose

import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
overview_filename = 'Coronavirus_Overview_'+dt_string+'.csv'
detailed_filename = 'Coronavirus_CountryWise_'+dt_string+'.csv'

print('### Fetching Data from https://www.worldometers.info/coronavirus/ Please wait..!!!')

response = requests.get('https://www.worldometers.info/coronavirus/')

soup  = BeautifulSoup(response.text,'html.parser')

print('*** Preparing file.. Please wait..  ****')

main_counters  = soup.find_all(class_='maincounter-number')
number_table_main =soup.find_all(class_='number-table-main')
country_wise =soup.find(id='main_table_countries')

with open(overview_filename,'w') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['Total Cases','Deaths','Recovered', 'Active Cases', 'Closed Cases']
	csv_writer.writerow(['***** NOTE: This data is  for analytical purpose only.No one is authorized to use this data for business/commercial benefits *******'])
	csv_writer.writerow(headers)

	total = main_counters[0].get_text()
	deaths = main_counters[1].get_text()
	recovered = main_counters[2].get_text()
	active_cases = number_table_main[0].get_text()
	closed = number_table_main[1].get_text()
	csv_writer.writerow([total,deaths,recovered,active_cases,closed])
	print('Done with overview.. *** Please find details in filename: "'+overview_filename+'"')

print('*** Preparing country wise details Please wait.. Almost done ****')

with open(detailed_filename,'w') as csv_file:
	csv_writer = writer(csv_file)
	headers_list = []
	for header in country_wise.find_all('th'):
		headers_list.append(header.get_text().replace('\n',''))
	csv_writer.writerow(['***** NOTE: This data is  for analytical purpose only.No one is authorized to use this data for business/commercial benefits *******'])
	csv_writer.writerow(headers_list)
	for row in country_wise.find('tbody').find_all('tr'):
		row_data = []
		for data in row.find_all('td'):
			row_data.append(data.get_text().replace('\n',''))
		csv_writer.writerow(row_data)
	print('**** Saved country wise details.. in file :"'+detailed_filename+'"')
	
