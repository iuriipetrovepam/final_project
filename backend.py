from datetime import datetime
import calendar
import requests
#from xml.etree import ElementTree
import xmltodict

today = datetime.now()

year_number = datetime.now().timetuple().tm_year
month_number = datetime.now().strftime('%m')

current_month_start = f"01/{month_number}/{year_number}"
current_month_end = f"{calendar.monthrange(year_number, int(month_number))[1]}/{month_number}/{year_number}"

print(f"today {today}")
print(f"year_number {year_number}")
print(f"month_number {month_number}")
print(f"current_month_start {current_month_start}")
print(f"current_month_end {current_month_end}")
print(f"")
link = f'http://www.cbr.ru/scripts/xml_metall.asp?date_req1={current_month_start}&date_req2={current_month_end}'
req = requests.get(link)
print(req, type(req))

data = xmltodict.parse(req.content)
for key, value in data.items(): 
    #print(key, "--", value) 
    for item in value:
        if item == 'Record':
            for item2 in item.value():
                print(item2)

        
