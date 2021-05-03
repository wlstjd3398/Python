"""
날짜 : 2021/04/27
이름 : 김철학
내용 : 파이썬 자료구조 Dictionary 실습 교재 p98
"""

# Dictionary 생성 {}사용
dic1 = {1: '서울', 2: '대전', 3: '대구', 4: '부산', 5: '광주'}
dic2 = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cherry'
}
dic3 = {
    101: [1, 2, 3, 4, 5],
    102: (6, 7, 8, 9, 10),
    103: {'한국', '미국', '중국', '일본'},
    104: {'p1': '김유신', 'p2': '김춘추', 'p3': '장보고'}
}

# Dictionary 출력
print('dic1 type :', type(dic1))
print('dic1[1] :', dic1[1])
print('dic1[4] :', dic1[4])
print('dic1[5] :', dic1[5])

print('dic2 type :', type(dic2))
print("dic2['A'] :", dic2['A'])
print("dic2['B'] :", dic2['B'])
print("dic2['C'] :", dic2['C'])

print('dic3 type :', type(dic3))
print('dic3[101][1] :', dic3[101][1])
print('dic3[101][4] :', dic3[101][4])
print('dic3[102][3] :', dic3[102][3])
print('dic3[103] :', dic3[103])
print("dic3[104]['p1'] :", dic3[104]['p1'])

# 응용
dics = [dic1, dic2, dic3]

print(dics[0][3])
print(dics[1]['A'])
print(dics[2][104]['p2'])

