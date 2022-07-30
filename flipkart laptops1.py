from numpy import arange
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import math

driver=webdriver.Firefox(executable_path=r'C:\Users\dhanu\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')
driver.get('https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5beaa1f7-c029-4d2e-b966-d9ee6e2d6ee6_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&sort=recency_desc')

ar=[]
prev="https://www.flipkart.com"
i=1
while(prev!=driver.current_url):
    prev=driver.current_url
    print(prev)
    time.sleep(3)
    
    
    laptops=driver.find_elements_by_class_name("_1fQZEK")
    if(len(laptops)==0):
        break
    
    for l in laptops:
        ar1=list()
        ar1.append(l.find_element_by_class_name("_4rR01T").text)
        ar1.append(l.get_attribute('href'))

        specslist=l.find_elements_by_class_name("rgWa7D")
        # print("spl")
        # print(specslist)
        attri = [x.text for x in specslist]
        # print()
        # print(attri)
        del attri[5:]
        ar1.extend(attri)
        try:
            ar1.append(l.find_element_by_class_name("_3LWZlK").text)
        except:
            ar1.append("NA")
        # print("ar1")
        # print(ar1)
        ar1.append(l.find_element_by_class_name("_25b18c").text.split()[0])
        ar.append(ar1)
        # print(ar)
    i+=1
    driver.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5beaa1f7-c029-4d2e-b966-d9ee6e2d6ee6_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&sort=recency_desc&page="+str(i))
    
d=pd.DataFrame(ar)
d.to_excel("laptop data.xlsx",index=False,header=False)
