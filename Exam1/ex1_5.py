"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 문자열이 "12345" 라면, '1+2+3+4+5' 결과 15를 출력하는 프로그램을 작성하시오
"""

str = '12345'
sum = 0

for i in range(len(str)):

    num = int(str[i])
    sum += num
print('합 : ', sum)