"""
날짜 : 2021/06/03
이름 : 김철학
내용 : 코딩 테스트 - 시각
"""
# h값 입력받기
h = int(input())

count = 0

# '3'들어가면 00:00:00 ~ 04:59:59

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)