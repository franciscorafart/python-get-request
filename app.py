#import library to make http requests
import requests
#import BeautifulSoup class from bs4 file. Will allow us to parse through html
from bs4 import BeautifulSoup

#get request
request = requests.get("https://www.amazon.com/MXL-770-Cardioid-Condenser-Microphone/dp/B0007NQH98?pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3443758062&pf_rd_r=0e28883a-d1bd-4bcb-bf98-9b22aeae13f2&pd_rd_wg=ItHrL&pf_rd_s=desktop-gateway&pf_rd_t=40701&pd_rd_w=scuL4&pf_rd_i=desktop-gateway&pd_rd_r=0e28883a-d1bd-4bcb-bf98-9b22aeae13f2&ref_=pd_gw_dl_rcs")
content = request.content

#Using html parser of beautiful soup class
soup = BeautifulSoup(content, "html.parser")

#parse through the html and look for a span with the established id in JSON format
#<span id="priceblock_dealprice" class="a-size-medium a-color-price">US$59.95</span>
element = soup.find("span",{"id":"priceblock_dealprice"})

#strip method to remove leading and trailing white space
string_price = element.text.strip()

#Convert number

#This is copying the string from different indexes. Instead of [start:end] we start from index = 1
price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if (price<60):
    print("Buy! Price is {}".format(price))
else:
    if (price > 60):
        print("Don't buy! Price is {}".format(price))
