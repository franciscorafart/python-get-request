#import requests library to make http request
import requests
#import BeautifulSoup class from bs4 file. Will allow to parse through html
from bs4 import BeautifulSoup

#get request: requesting the price of an amazon article
request = requests.get("https://www.amazon.com/MXL-770-Cardioid-Condenser-Microphone/dp/B0007NQH98?pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3443758062&pf_rd_r=0e28883a-d1bd-4bcb-bf98-9b22aeae13f2&pd_rd_wg=ItHrL&pf_rd_s=desktop-gateway&pf_rd_t=40701&pd_rd_w=scuL4&pf_rd_i=desktop-gateway&pd_rd_r=0e28883a-d1bd-4bcb-bf98-9b22aeae13f2&ref_=pd_gw_dl_rcs")
content = request.content

#Using html parser of beautiful soup class
soup = BeautifulSoup(content, "html.parser")

#Look for a span with the established id in JSON format
element = soup.find("span",{"id":"priceblock_dealprice"})

#strip method to remove leading and trailing white space
string_price = element.text.strip()

#Convert number

#remove $ sign from the price
#This is copying the string from different indexes. Instead of [start:end] we start from index = 1
price_without_symbol = string_price[1:]

#convert to float
price = float(price_without_symbol)

#print out to user
if (price<60):
    print("Buy! Price is {}".format(price))
else:
    if (price > 60):
        print("Don't buy! Price is {}".format(price))
