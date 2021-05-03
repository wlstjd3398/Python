# (1) 리스트 정렬
lst = [1, 2, 3, 4]  # list 생성
result = lst * 2    # 각 원소 연산 안됨
print(result)   # [1, 2, 3, 4, 1, 2, 3, 4]


result.sort()   # 오름차순 정렬
print(result)   # [1, 1, 2, 2, 3, 3, 4, 4]

result.sort(reverse = True) # 내림차순 정렬
print(result)   # [4, 4, 3, 3, 2, 2, 1, 1]

# (2) 리스트 요소 검사
import random
r = []  # 빈 list
for i in range(5) :
    r.append(random.randint(1,5))
print(r)
if 4 in r :
    print('있음')
else :
    print('없음')