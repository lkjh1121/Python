"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 파이썬 구구단 실습하기 p74
"""
# 구구단 출력 : range() 함수 이용

#   (1) 바깥쪽 반복문
for i in range(2, 10) :
    print('~~~ {}단 ~~~', format(i))

    # (2) 안쪽 반복문
    for j in range(1,10) :
        print('%d * %d =%d'%(i, j, i*j))