from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import math

cards=['intel core i9 12th gen',
 'amd ryzen 7 octa core',
 'amd ryzen 7 octa core 5th gen',
 'intel core i5 11th gen',
 'intel core i7 11th gen',
 'intel celeron dual core',
 'intel core i5 10th gen',
 'intel pentium silver',
 'amd athlon dual core',
 'amd ryzen 7 dual core 7th gen',
 'amd ryzen 3 quad core 3rd gen',
 'amd ryzen 9 octa core 5th gen',
 'intel core i3 11th gen',
 'amd ryzen 5 hexa core',
 'intel core i5 12th gen',
 'intel core i7 12th gen',
 'amd ryzen 5 quad core',
 'amd ryzen 7 hexa core 10th gen',
 'amd ryzen 9 octa core 10th gen',
 'amd ryzen 7 quad core 10th gen',
 'intel core i3 10th gen',
 'amd ryzen 5 quad core 3rd gen',
 'intel pentium quad core',
 'intel celeron quad core',
 'amd ryzen 7 quad core',
 'intel core i9 11th gen',
 'qualcomm snapdragon 7c gen 2',
 'amd ryzen 5 dual core',
 'amd ryzen 3 dual core',
 'intel pentium quad core 10th gen',
 'intel core i7 10th gen',
 'amd ryzen 9 octa core',
 'amd dual core',
 'amd ryzen 5 hexa core 5th gen',
 'intel pentium quad core 11th gen',
 'amd ryzen 3 quad core',
 'amd ryzen 9 octa core 9th gen',
 'intel ryzen 7 hexa core',
 'amd ryzen 9 octa core 11th gen',
 'amd ryzen 5 octa core',
 'amd ryzen 7 quad core 3rd gen',
 'amd ryzen 5 octa core 11th gen',
 'amd ryzen 7 octa core 4th gen',
 'apple m1 pro',
 'intel celeron dual core 4th gen',
 'amd ryzen 3 hexa core 4th gen',
 'amd ryzen 3 dual core 3rd gen',
 'intel core i5 9th gen',
 'amd apu dual core a6',
 'mediatek mediatek kompanio 500',
 'apple m1',
 'amd apu dual core a9',
 'intel hexa core i5 10th gen',
 'intel octa core i7 10th gen',
 'amd ryzen 5 hexa core 4th gen',
 'intel core i7 8th gen',
 'intel core i9 10th gen',
 'intel core i5 7th gen',
 'intel core i5 8th gen',
 'intel core i3 7th gen',
 'intel core i7 9th gen']

ar=[[-1,i] for i in cards]

driver=webdriver.Firefox(executable_path=r'C:\Users\dhanu\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')
driver.get('https://cpu.userbenchmark.com/')

for i in range(len(ar)):
    
    time.sleep(3)
    searchbar=driver.find_element_by_xpath("/html/body/div[2]/div/div[6]/form/div[2]/table/thead/tr/th[2]/div/input")
    searchbar.clear()
    searchbar.send_keys(ar[i][1])
    searchbar.send_keys(Keys.ENTER)
    time.sleep(2)
    try:
        text1=driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/form/div[2]/table/tbody/tr/td[5]/div[1]/div').text
        ar[i][0]=float(text1.split()[0])
    except:
        continue
    
print(ar)
s=pd.DataFrame(ar)
s.to_excel("cpu_ranking.xlsx",index=False,header=False)