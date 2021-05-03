"""
날짜 : 2021/04/30
"""
i = 0
while i < 10:
    i += 1  # 카운터
    if i == 3:
        continue    # 다음 문장 skip
    if i == 6:  # 탈출 조건
        break   # exit
    print(i, end=' ')
    