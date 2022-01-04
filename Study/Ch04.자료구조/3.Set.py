"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 파이썬 자료구조 Set 실습하기 교재 p96
"""


# Set(집합) : 순서 X, 중복 X 자료구조
set1 = {1, 2, 3, 4, 5, 3, 2}
print('set1 :', type(set1))
print('set1 :', set1)

set2 = set('Hello World')
print('set2 type : ', type(set2))
print('set2 : ', set2)

# 리스트 변환해서 출력
List1 = List(set1)
print('List1 :', List1)

List2 = List(set2)
print('List2 :', List2)