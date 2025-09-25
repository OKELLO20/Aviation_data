
import requests
import csv
import pandas as pd
import openpyxl
import time

#some parts of this code have been ommitted and will be made available once the developement of the application is complited

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})
myjson = response.json()
csvheader = ['Departure_time', 'airline_name']


for x in myjson['data']:
    listing = [x['arrival']['actualTime'], x['airline']['name']]
    ourdata.append(listing)
print('Done')

with open('Users/[]/Desktop/AviationData/quil.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print('done')

csv= pd.read_csv('Users/[]/Desktop/AviationData/quil.csv')

excelWriter = pd.ExcelWriter('Users/[]/Desktop/AviationData/aviation.xlsx')
csv.to_excel(excelWriter)

excelWriter.close()
print('Done')

from openpyxl import load_workbook


ws = wb.active

ws.insert_cols(2)
ws['B1'].value='City'

ws.insert_cols(3)
ws['C1'].value='Operation'


excel_file = 'Users/[]/Desktop/AviationData/aviation.xlsx'


leg = df.max()

x = int(leg) + 3

for i in range(2,x):
    ws.cell(row=i, column=2).value = 'Nairobi'



for i in range(2,x):
    ws.cell(row=i, column=3).value = 'Arrival'



print('sleeping')

time.sleep(62)

print('working')



url = "[]"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})
ourjson = response.json()
csvheader = ['Departure_time', 'airline_name']

for x in ourjson['data']:
    listing = [x['departure']['actualTime'], x['airline']['name']]
    ourdata.append(listing)
print('Done')

with open('Users/[]/Desktop/AviationData/third.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print('done')


excelWriter = pd.ExcelWriter('Users/[]/Desktop/AviationData/flying.xlsx')
csv.to_excel(excelWriter)

excelWriter.close()
print('Done')


ws = wb.active

ws.insert_cols(2)
ws['B1'].value='City'

ws.insert_cols(3)
ws['C1'].value='Operation'


excel_file = 'Users/[]/Desktop/AviationData/flying.xlsx'
df = pd.read_excel(excel_file, usecols=[0])

leg = df.max()

x = int(leg) + 3

for i in range(2,x):
    ws.cell(row=i, column=2).value = 'Nairobi'




wb.save('Users/[]/Desktop/AviationData/flying.xlsx')

data_folder= '/Users/[]/Desktop/AviationData'

df = []

for file in os.listdir(data_folder):
    if file.endswith('xlsx'):
        print('loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_folder,file)))

df_master.to_excel('master file.xlsx', index=False)

