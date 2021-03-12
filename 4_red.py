
"""
    1. re.compile("원하는 형태")
    2. m = p.match("비교할 문자열") : 처음부터 주어진 문자열의 처음부터 일치하는지 확인
    3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
    3. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환 리스트!!

    원하는 형태 : 정규식
    . : 하나의 문자를 의미한다
    ^ : 문자열의 시작 ex) (^de) > desk destination | Not > fade
    $ : 문자열의 끝 ex) (se$) > case, base, | Not > face

    w3school :
        RegEx
        python re
"""

import re
# abcd, book, desk
# ca?e,
# care, cafe, case, cave

#정규식사용법
p = re.compile("ca.e")
# . : 하나의 문자를 의미한다
# ^ : 문자열의 시작 ex) (^de) > desk destination | Not > fade
# $ : 문자열의 끝 ex) (se$) > case, base, | Not > face

def print_match(m):
    # m = p.match("cave")
    if m:
        print("------Match------")
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)  # 입력받은 문자열
        print("m.start():", m.start())  # 일치하는 문자열을 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작 / 끝 index
        print("------------------")
    else:
        print("Not match")

# m = p.match("careless")  #주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

m = p. search("good care")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall("good care cafe") # findall : 일치하는 모든것을 리스트 형태로 반환
print(lst)


