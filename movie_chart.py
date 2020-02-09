import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.cgv.co.kr/movies/?ft=0")
c = r.content

### html.parser : 홈페이지 소스 파싱
html = BeautifulSoup(c, "html.parser")

### Find 함수 : 찾고자 하는 때
ol = html.find("ol")

### find_all : 여러개의 태그를 찾을 때
li = ol.find_all("li")

###변수.find("태그명",{"class":"찾고자하는클래스명"}
for l in li:
    div = l.find("div", {"class": "box-contents"})
    ### strong 태그를 찾고 거기서 text만 가져올 때
    strong = div.find("strong").text
    print(strong)

### strong 태그에서 find_all 불가능 왜냐면 strong 태그를 모두 찾아 리스트 형태로 반환할 때 에러 발생

### text 메소드는 하나의 태그에만 해당 되는 것, 리스트 형태로 사용 불가
