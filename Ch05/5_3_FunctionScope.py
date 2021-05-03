"""
날짜 : 2022/04/29
이름 : 김철학
내용 : 파이썬 함수 스코프 교재 p132
"""
def sum(x, y):
    tot = 0

    for k in range(x, y+1):
        tot += k

    return tot

tot = 0
start = 1
end = 10

tot = sum(start, end)

print('tot:', tot)
