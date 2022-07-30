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
errors=[]
k=1
while(prev!=driver.current_url):
    prev=driver.current_url
    # print(prev)
    time.sleep(1)
    laptops=driver.find_elements_by_class_name("_1fQZEK")
    laptops=[x.get_attribute('href') for x in laptops]
    if(len(laptops)==0):
        break

    try:
        for l in laptops:
            ar1={}

            #link
            ar1["link"]=l
            driver.get(l)
            time.sleep(1.5)
            #name
            z=driver.find_elements_by_class_name("B_NuCI")
            
            while(len(z)==0):
                driver.get(l)
                time.sleep(1.5)
                z=driver.find_elements_by_class_name("B_NuCI")
            #name
            ar1["name"]=z[0].text
            
            #user rating
            z=driver.find_elements_by_class_name("_2dMYsv")
            if (len(z)==0):
                ar1["user rating"]=str(driver.find_element_by_class_name("_3LWZlK").text)

            # try:
            #     ar1["user rating"]=str(driver.find_element_by_class_name("_3LWZlK").text)
            # except:
            #     ar1["user rating"]="NA"
            
            ar1["Price"]=str(driver.find_element_by_css_selector("._30jeq3._16Jk6d").text)


            #read more
            # time.sleep(3)
            readmore=driver.find_element_by_css_selector("._2KpZ6l._1FH0tX")
            readmore.click()

            #tables
            tableclass=driver.find_elements_by_class_name("_14cfVK")
            # print(tableclass)
            for t in tableclass:
                column1=t.find_elements_by_css_selector("._1hKmbr.col.col-3-12")
                column1=[x.text for x in column1]
                column2=t.find_elements_by_class_name("_21lJbe")
                column2=[x.text for x in column2]

                # print("columns")
                # print(column1)
                # print(column2)
                for j in range(len(column1)):
                    ar1[column1[j]]=column2[j]
                    # print("ar1")
            # print(ar1)
            ar.append(ar1)
            # break
            # print(ar)
    except:
        # print()
        # print("i",i)
        errors.append(i)
        d=pd.DataFrame(ar)
        ar=[]
        d.to_excel("complete laptop data"+str(k)+".xlsx")
        k+=1
    i+=1
    driver.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_5beaa1f7-c029-4d2e-b966-d9ee6e2d6ee6_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&sort=recency_desc&page="+str(i))
    
print("errors",errors)
d=pd.DataFrame(ar)
d.to_excel("complete laptop data"+str(k)+".xlsx")
