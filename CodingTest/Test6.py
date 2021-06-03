"""
날짜 : 2021/06/03
이름 : 김철학
내용 : 코딩 테스트 - 왕실의 나이트(체스)
"""

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0


# 오른쪽 2칸, 위쪽 1칸
next_row = row + 2
next_col = column - 1

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 오른쪽 2칸, 아래쪽 1칸
next_row = row + 2
next_col = column + 1

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 왼쪽 2칸, 위쪽 1칸
next_row = row - 2
next_col = column - 1

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 왼쪽 2칸, 아래쪽 1칸
next_row = row - 2
next_col = column + 1

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 위쪽 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column - 2

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 위쪽 2칸, 왼쪽 1칸
next_row = row - 1
next_col = column - 2

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 아래쪽 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column + 2

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


# 아래쪽 2칸, 왼쪽 1칸
next_row = row - 1
next_col = column + 2

if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1


print(result)