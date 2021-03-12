import requests


res = requests.get("http://google.com")
res.raise_for_status()
# res1 = requests.get("http://cubelink.ga")
print("응답코드 :", res.status_code)

# print("응답코드 :", res1.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼다. [에러코드", res.status_code,"]")

print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)
#정보 받은것까찌 해봄
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)