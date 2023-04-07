import time
from selenium import webdriver
from bs4 import BeautifulSoup
from geopy.geocoders import ArcGIS
from selenium.webdriver.chrome.service import Service
from csv import writer

from webdriver_manager.chrome import ChromeDriverManager
geolocator=ArcGIS()

options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


with open('Retail_Brand_Store_Details.csv','w', encoding='utf8', newline='') as f:
    thewriter=writer(f)
    header=['Store Name', 'Address', 'Timings', 'Coordinates', 'Phone Number']
    thewriter.writerow(header)
    for i in range(1,99):
        url="https://stores.titan.co.in/?page="+str(i)
        driver.get(url)

        time.sleep(2)

        soup=BeautifulSoup(driver.page_source,'lxml')
        outlet_lists=soup.find_all("div",class_="outlet-list")


        for outlet_list in outlet_lists:
            store_info=outlet_list.select("div.store-info-box")
            for stores in store_info:
                store1=stores.select('li.outlet-name>div.info-text')
                store=''
                for store_name in store1:
                    store+=store_name.text.strip()
                address1=stores.select('li.outlet-address>div.info-text')

                address=''
                for item in address1:
                    address+=item.text.strip()
                    address+=', '
                timing1=stores.select('li.outlet-timings>div.info-text')
                timing=''
                for t in timing1:
                    timing+=t.text.strip()
                location=geolocator.geocode(address)
                try:
                    Coordinates=(location.latitude,location.longitude)
                except:
                    Coordinates="Not Found"
                phone1=stores.select('li.outlet-phone>div.info-text')
                phone=''
                for item in phone1:
                    phone+=item.text.strip()
                phone+='\t'
                info=[store, address, timing, Coordinates, phone]
                thewriter.writerow(info)
  

time.sleep(2)

driver.close()


