

from __future__ import print_function, division
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import pickle
import time


# url = 'https://www.carfax.com/vehicle/1N4AL3AP6FC212164'
def scrape_url(url):
    """Scrapes through a single URL and Exports Required Fields to a dictionary """
    get_url=url
    get_url
    response = requests.get(url)
    print(response.status_code)
    page = response.text
    soup = BeautifulSoup(page,"html.parser")
    big_tabledata=soup.find(class_='vdp-container-body')
    df=pd.read_html(big_tabledata)

    price=df[0][1][0]
    milage=df[0][1][1]
    location=df[0][1][2]
    ext_color=df[0][1][3]
    int_color=df[0][1][4]
    drive_type=df[0][1][5]
    transmission=df[0][1][6]
    body_style=df[0][1][7]
    engine=df[0][1][8]
    fuel=df[0][1][9]
    mpg_city_highway=df[0][1][10]
    vin=df[0][1][11]
    stock=df[0][1][12]
    big_text = soup.find(class_='___iso-state___').prettify()
    print(vin)
    make_str = big_text.find('\\&quot;make\\&quot;')
    make_tag=(big_text[make_str:make_str+100].split("\\&quot;")[1])

    #declare make cell
    make=(big_text[make_str:make_str+100].split("\\&quot;")[3])
 
    #declare model
    model_str = big_text.find('\\&quot;model\\&quot;')
    (big_text[model_str:model_str+100].split("\\&quot;")[1])
    model=(big_text[model_str:model_str+100].split("\\&quot;")[3])

    #declare year:
    year_str = big_text.find(',\\&quot;year\\&quot;')
    (big_text[year_str:year_str+100].split("\\&quot;")[1])
    year=(big_text[year_str:year_str+100].split("\\&quot;")[2])

    dict_car=({'vin':vin,'year':year,'model':model,'make':make,'stock':stock,'price':price,
       'milage':milage,'location':location,'ext_color':ext_color,'int_color':int_color,'drive_type':drive_type,
       'transmission':transmission,'body_style':body_style,'engine':engine,'fuel':fuel,
       'mpg_city_highway':mpg_city_highway,'stock':stock})
    
    dict_car2=str(dict_car)
    line_clean=dict_car2.replace(' ','')
    line_clean2=line_clean.replace('|','')    
    line_clean3=[line_clean2.replace('nan','99')]
    line_clean3
    df_car = pd.DataFrame((line_clean3))
    car_dict= eval(df_car[0][0])

    return car_dict

def start_scraping(url_list):
    """Loops through scrape_url(which outputs a dictionary 
    which is then readily converted to a DataFrame) """
    df_out = None
    for url in url_list: 
        try:
            test=scrape_url(url)
            df_abc = pd.DataFrame(test, index=range(1))
            if df_out is None:
                df_out = df_abc
            else:
                df_out = df_out.append(df_abc)
            time.sleep(3)
            df_out.to_csv('test_output.csv')

        except:
            print('except')
    return df_out


#All URLS in a CSV file are converted into a list. 
all_urls = []
with open('data/step1_output_scraped_url_.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        all_urls.append(row[0])
all_urls_v2=all_urls
all_urls_v3=(set(all_urls_v2))

Scrape_Output=(start_scraping(all_urls_v3))

df_remove_dups=Scrape_Output.drop_duplicates(['vin'], keep='last')



df_remove_dups.to_csv('data/html_extract.csv')

