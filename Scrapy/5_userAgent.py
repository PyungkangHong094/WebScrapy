"""
    웹 스크래핑의 기본
    user agent string 을 가져와서 그 value 에 넣어줘야한다
    그렇게 해야지 가져오고싶은 사이트에 다 긁어 와서 써줄수있다.

"""
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()
with open("test-info_1.html", "w", encoding="utf-8") as f:
    f.write(res.text)