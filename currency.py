import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=환율조회")

c = r.content

html = BeautifulSoup(c, "html.parser")

div = html.find("div", {"class": "rate_tlt"})

country = div.find("em", {"class": "t_nm"}).text

print(country)

rate = div.find("span", {"class": "spt_con up"}).text

print(str(rate[3:]))


### 미국USD
### 1,193.50  전일대비상승9.50 (+0.8%) 
