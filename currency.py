import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=환율조회")

c = r.content

html = BeautifulSoup(c, "html.parser")

div = html.find("div", {"class": "rate_tlt"})

country = div.find("em", {"class": "t_nm"}).text

print(country)

rate_dw = div.find("span", {"class": "spt_con dw"})

rate_up = div.find("span", {"class": "spt_con up"})

if rate_up == None :
    currency_dw = rate_dw.find("strong").text
    print(currency_dw)
else :
    currency_up = rate_up.find("strong").text
    print(currency_up)

### 미국USD
### 1,183.00

