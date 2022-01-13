"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 최대공약수 연습문제
"""

a = int(input('첫번쨰 수 입력 :'))
b = int(input('두번쨰 수 입력 :'))

result = min = 0

if a < b:
    min = a
else:
    min = b

while True:

    if a % min == 0 and b % min == 0:
        result = min
        break

    min -= 1

    print('%d와 %d의 최대 공약수는 %d입니다.' % (a, b, result))
