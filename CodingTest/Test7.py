"""
날짜 : 2021/06/10
이름 : 김철학
내용 : 코딩 테스트 - 모험가 길드
"""

n = int(input())    # 모험가의 수 입력
data = list(map(int, input().split()))  # 각 모험가의 공포도 입력
data.sort() # 공포도가 낮은 순으로 정렬

result = 0  # 총 그룹 수
count = 0   # 현재 그룹에 포함된 모험가 수

for i in data:  # 공포도가 낮은 것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함

    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹 포함
        result += 1 # 총 그룹수 증가
        count = 0   # 현재 그룹의 포함된 모험가 수 초기화

print(result)   # 총 그룹수 출력