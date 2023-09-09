import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import os

def web_content_div(web_content, class_path, value):
    web_content_div = web_content.find_all('div', {'class': class_path})
    
    try:
        if value != 'None':
            spans = web_content_div[0].find_all()
            texts = [span.get_text() for span in spans]
        else:
            texts = []
    except IndexError:
        texts = []
    
    return texts
        
    
        
def real_time_price(stock_code):
    Error = 0
    url = 'https://finance.yahoo.com/quote/' + stock_code + '?p=' + stock_code + '&.tsrc=fin-srch'
    print(url)
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'D(ib) Mend(20px)','fin-streamer'),#"My(6px) Pos(r) smartphone_Mt(6px) W(100%)")
        print(texts)
        price, change, volume, latest_pattern, one_year_target = [], [], [],[],[]
    except ConnectionError:
        price, change, volume, latest_pattern, one_year_target = [], [], [],[],[]
        Error = 1
        print('Connection Error')
        
    return price, change, volume, latest_pattern, one_year_target, Error
    

stock = ['AAPL']

while (True):
    for stock_code in stock:
        stock_price, change, volume, latest_pattern, one_year_target, Error = real_time_price(stock_code)
        