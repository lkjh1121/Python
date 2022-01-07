"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 파이썬 break, continue 실습하기 p69
"""
i = 0
while i < 10:
    i += 1 # 카운터
    if i == 3:
        continue  # 다음문장 skip
    if i == 6:  # 탈출 조건
        break  # exit
    print(i, end=' ')