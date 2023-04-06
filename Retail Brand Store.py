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
url="https://stores.titan.co.in/titan-world-watch-shop-lajpat-nagar-new-delhi-187114/Home?utm_source=locator&utm_medium=googleplaces"

driver.get(url)

time.sleep(2)

soup=BeautifulSoup(driver.page_source,'lxml')

with open('Retail_Brand_Store_Details.csv','w', encoding='utf8', newline='') as f:
    thewriter=writer(f)
    header=['Store Name', 'Address', 'Timings', 'Coordinates', 'Phone Number']
    thewriter.writerow(header)
    store_name=soup.find("h1",id="speakableIntro").text.strip()
    # print("Store Name -",store_name.text.strip())
    address1=soup.select('div.info-text>span')
    # print(address1)
    address=""
    for item in address1:
        address+=item.text+", "
    timings=soup.find('span',class_='info-text').text
    # print("Timings -",timings.text)
    location=geolocator.geocode(address)
    Coordinates=(location.latitude,location.longitude)
    # print("Address -",address)
    # print((location.latitude,location.longitude))
    
    mobile=soup.select('div.info-text>a')
    phone=''
    for item in mobile:
        phone=item.text.strip()
    phone+='\t'    
    # print(phone)
    info=[store_name, address, timings, Coordinates, phone]
    thewriter.writerow(info)
  

time.sleep(2)

driver.close()


