import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=환율조회")

c = r.content

html = BeautifulSoup(c, "html.parser")

div = html.find("div", {"class": "rate_tlt"})

country = div.find("em", {"class": "t_nm"}).text

print(country)

### 전일대비 지수가 하락하자 함수 변경 "spt_con up" > "spt_con dw", 결과값으로 None 프린트 됌. 
### 따라서 if else 함수를 사용하여 전일대비 지수 상승 혹은 하락에도 옳은 결과값이 프린트 되도록 수정

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

