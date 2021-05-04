# (1) 재귀함수 정의 : 1~n 카운트
def Counter(n):
    if n == 0 :
        return 0    # 종료 조건
    else :
        Counter(n-1)    # 재귀호출
    print(n, end = ' ')

# (2) 함수 호출1
print('n=0 : ', Counter(0))

# (3) 함수 호출2
Counter(5)

