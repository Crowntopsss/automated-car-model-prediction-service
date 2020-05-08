#!/usr/bin/env python
# coding: utf-8

# # Weblink Scraper for Carfax.com
# 
# 

# #### Libraries Used

# In[2]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os


# ### ChromeDriver Required for the Scraper to work. 

     
chromedriver = "chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver


# ### Step 1 Declare the Webdriver


##### It will open a chrome browser controlled by the this script.
car_url = "https://www.carfax.com/Used-Cars-Under-75000_f12"
driver2 = webdriver.Chrome(chromedriver)
driver2.get(car_url)


# ### Declare Functinos Used for Scraping
# 1. enter_zip - Enter the parameters for websearch. 
# 2. get_page_links - Get page links and store them in a CSV Format. 
# 3. next_page- Go to Next Page
# 

def get_page_links(filename):
    """get_page_links - Get page links and store them in a CSV Format."""
    with open((str(filename)+'.csv'), 'a', newline='') as csvfile:
        carwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        car_selector2 = '//div[@class="srp-list-item-description column"]'
        for car_anchor in driver2.find_elements_by_xpath(car_selector2):
            output=((car_anchor.find_element_by_css_selector('a').get_attribute('href')))
            carwriter.writerow([output])

    
def next_page():
    """next_page- Go to Next Page"""
    nextbutton=driver2.find_element_by_xpath('//li[@class="next"]/a')
    time.sleep(1)
    nextbutton.click()
    

    
def enter_zip(f2):
    """enter_zip - Enter the parameters for websearch."""
#     nextbutton=driver2.find_element_by_xpath('//input[@class="form-control search-zip ui-input"]')
#     nextbutton.send_keys('zipcode')
    zip_form=driver2.find_element_by_name("zip") # note another approach
    zip_form.send_keys(f2)
    print(f2)
    zip_form.send_keys(Keys.RETURN)
                                          
def start_scraping(num_pages, save_to_file):
    time.sleep(3)
    """Start Scraping for links"""
    for x in range(0, num_pages):
        """Declare the number of pages that will be scraped"""
        get_page_links(save_to_file)
        time.sleep(3)
        """Window_Before is very useful for scraping websites 
        that have popups at unexpected times, interm interruping the scraper"""
        window_before = driver2.window_handles[0]
        driver2.switch_to_window(window_before)
        try:
            next_page()
        except:
            print(x + "except")


# ### Enter Parameters for Scraping

#Runthis for extract all extracts wrute to file 
enter_zip('90014')
time.sleep(5) 



start_scraping(100,'data/scraped_url')



