"""
날짜 : 2021/05/24
이름 : 김철학
내용 : 코딩 테스트 - 1이 될때 까지
"""
n, k = map(int, input().split())
result = 0

while True:

    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1

print(result)