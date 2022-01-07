"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 파이썬 list 자료구조 실습하기 p73
"""
# (1) list에 자료 저장하기
import random

let = []  # 빈 list 만들기
for i in range(10) :  # 0~9
    r = random.randint(1, 10)  # 난수 발생
    let.append(r)  # 난수 저장

print('lst=', let)  #난수 출력

# (2) list에 자료 참조하기
for i in range(10) :  # 0~9
    print(let[i] * 0.25)  # 난수 * 0.25