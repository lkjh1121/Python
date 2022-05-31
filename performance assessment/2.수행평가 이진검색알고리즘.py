"""
날짜 : 0000/00/00
이름 : 김재현
내용 : 파이썬 이진검색 알고리즘 수행평가
"""

dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input('검색 숫자 입력 :'))

low = 0
high = len(dataset) -1
loc = 0
state = False

while low <= high:
    mid = (low + high)

    if dataset[mid] > value:
        high = mid -1
    elif dataset[mid] < value:
        low = mid + 1
    else:
        loc = mid
        state = True
        break
if state:
    print('찾은 위치 : %d번쨰' % (loc + 1))
else:
    print('찾는 값은 없습니다.')