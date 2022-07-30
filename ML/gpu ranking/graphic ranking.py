from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import math

cards=['nvidia geforce rtx 3070 ti', 'nvidia geforce rtx 3050',
       'integrated', 'iris xe',
       'intel hd',
       'amd radeon',
       'nvidia geforce gtx 1650', 'intel uhd',
       'amd radeon', 'intel iris xe',
       'amd radeon',
       'nvidia geforce rtx 3050', 'amd radeon',
       'nvidia geforce rtx 3070', 'intel uhd',
       'nvidia geforce rtx 3050 ti', 'amd radeon vega 8',
       'nvidia geforce rtx 3050', 'nvidia geforce rtx 3060',
       'intel hd',
       'nvidia geforce gtx 1650', 'intel uhd',
       'nvidia geforce rtx 3060', 'nvidia geforce mx 450',
       'amd radeon', 'nvidia geforce rtx 3050',
       'intel uhd 600', 'intel uhd',
       'amd radeon', 'nvidia geforce rtx 3050', 'amd radeon',
       'nvidia geforce rtx 3050 ti', 'amd radeon rx vega 10',
       'nvidia geforce rtx 3050',
       'intel uhd',
       'amd radeon rx vega 10', 'intel hd',
       'qualcomm adreno 618 gpu', 'amd radeon vega ',
       'amd radeon rx 6600m', 'integrated',
       'nvidia geforce gtx 1650',
       'nvidia geforce rtx 3050',
       'nvidia geforce rtx 3060',
       'nvidia geforce rtx 3050',
       'qualcomm adreno', 'integrated',
       'nvidia geforce rtx 3050ti',
       'intel uhd 600',
       'nvidia geforce rtx 3080 ti', 'intel iris plus',
       'amd radeon', 'nvidia geforce gtx',
       'intel uhd 605', 'nvidia geforce rtx',
       'intel uhd',
       'intel uhd 600', 'amd radeon',
       'intel iris xe',
       'amd radeon', 'intel iris',
       'amd radeon', 'intel uhd',
       'nvidia geforce mx 350', 'amd radeon',
       'intel iris xe', 'nvidia geforce mx 330',
       'intel hd', 'amd radeon rx 6700m', 'integrated',
       'nvidia geforce gtx 1650', 'nan',
       'nvidia geforce gtx 1650',
       'amd radeon',
       'nvidia geforce rtx 3060', 'nvidia geforce',
       'nvidia geforce gtx 1650 ti',
       'amd radeon', 'nvidia geforce rtx 3050',
       'intel iris xe', 'amd radeon vega 8',
       'intel uhd',
       'nvidia geforce gtx 1650',
       'amd radeon', 'nvidia geforce rtx 3050ti',
       'nvidia geforce mx 330',
       'intel uhd',
       'nvidia geforce gtx 1650', 'nvidia geforce mx 330',
       'nvidia geforce mx 350', 'amd radeon vega',
       'nvidia geforce gtx', 'intel iris xe',
       'intel uhd',
       'intel hd 520', 'intel uhd',
       'amd radeon rx6600m', 'intel iris xe',
       'nvidia geforce rtx', 'intel iris xe',
       'amd radeon rx 6800m', 'nvidia geforce mx 330',
       'amd radeon 5500u', 'amd radeon 5500m', 'nvidia geforce mx 130',
       'amd radeon r4', 'integrated', 'intel uhd 600',
       'intel hd 500', 'amd radeon r5',
       'amd radeon r4 (stoney ridge)', 'intel iris xe',
       'nvidia geforce gtx 1650 ti', 'nvidia geforce gtx 1650 max q',
       'nvidia geforce mx 250',
       'nvidia geforce gtx 1650 ti', 'nvidia geforce gtx 1650 ti',
       'nvidia geforce gtx 1650 ti', 'nvidia geforce gtx 1660 ti',
       'nvidia geforce rtx 2060', 'intel uhd 620',
       'intel hd 5500', 'integrated',
       'nvidia geforce rtx 2080 super max-q', 'nvidia geforce',
       'amd radeon', 'nvidia geforce mx 250',
       'amd radeon vega 6', 'intel iris xe max',
       'nvidia geforce gtx 1650 ti max-q', 'amd radeon 520',
       'nvidia geforce rtx 2070 max-q',
       'nvidia geforce gtx mx 330', 'nvidia geforce mx 230',
       'intel uhd', 'intel hd 620',
       'nvidia quadro p520', 'nvidia quadro t2000',
       'intel uhd 620', 'nvidia geforce mx 110',
       'nvidia geforce gtx']

ar=[[-1,i] for i in cards]

driver=webdriver.Firefox(executable_path=r'C:\Users\dhanu\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')
driver.get('https://gpu.userbenchmark.com/')

for i in range(len(ar)):
    searchbar=driver.find_elements_by_xpath("/html/body/div[2]/div/div[6]/form/div[2]/table/thead/tr/th[2]/div/input")
    while(len(searchbar)==0):
        searchbar=driver.find_elements_by_xpath("/html/body/div[2]/div/div[6]/form/div[2]/table/thead/tr/th[2]/div/input")
    searchbar[0].clear()
    searchbar[0].send_keys(ar[i][1])
    searchbar[0].send_keys(Keys.ENTER)
    time.sleep(3)
    try:
        text1=driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/form/div[2]/table/tbody/tr/td[5]/div[1]/div').text
        ar[i][0]=float(text1.split()[0])
    except:
        continue
    
print(ar)
ar.sort(key=lambda x:x[0])
s=pd.DataFrame(ar)
s.to_excel("gpu_ranking_new.xlsx",index=False,header=False)