"""
날짜 : 2022/01/04
이름 : 김재현
내용 : 파이썬 자료구조 List 실습하기 교재 p84
"""

# 리스트
List1 = [1, 2, 3, 4, 5]

print('List1 type :', type(List1))
print('List1[0] :', List1[0])
print('List1[2] :', List1[2])
print('List1[3] :', List1[3])

List2 = [5, 3.14, True, 'Apple']
print('List2 type :', type(List2))
print('List1[1] :', List1[1])
print('List1[2] :', List1[2])
print('List1[3] :', List1[3])

List3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('List3 type :', type(List3))
print('List3 [0][2] :', List3[0][2])
print('List3 [1][1] :', List3[1][1])
print('List3 [2][0] :', List3[2][0])

# 리스트 수정, 추가, 삭제
dataset = [1, 7, 3, 4, 5]
print('dataset :', dataset)

dataset[1] = 7
print('dataset :', dataset)

dataset[2:4] = [8,9, 10]
print('dataset :', dataset)


dataset[3:5] = []
print('dataset :', dataset)

# 리스트 반복문
for num in (1, 2, 3, 4, 5):
    print('num :', num)

people = ['김유신', '김춘추', '장보고']

for person in people:
    print('person :', person)

for index, value in enumerate(people):
    print('%d-, %s' % (index, value))

# 리스트 Comprehension
array = [1, 2, 3, 4, 5]

result1 = [num * 3 for num in array]
result2 = [num * 3 for num in array if num % 2 == 1]

print('result :', result1)
print('result :', result2)