dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력 : "))

low = 0 # start 위치
high = len(dataset) - 1 # end 위치
loc = 0
state = False   # 상태 변수

while (low <= high):
    mid = (low + high) // 2

    if dataset[mid] > value:    # 중앙값이 큰 경우
        high = mid - 1
    elif dataset[mid] < value:  # 중앙값이 작은 경우
        low = mid + 1
    else:   # 찾은 경우
        loc = mid
        state = True
        break   # 반복 exit
if state :
     print('찾은 위치 : %d 번째' % (loc+1))
else :
    print('찾는 값은 없습니다')