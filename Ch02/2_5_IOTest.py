#Input Output = IO
"""
날짜 : 2021/04/27
이름 : 김철학
내용 : 파이썬 표준입출력 실습 교재 p42
"""

#파이썬 표준 출력
print('Hello', end='!')
print('python') #문자를 한줄로하는데 구분을 !로

print('010', '1234', '1111', sep='-') #seperate

#파이썬 표준 입력
num = input('숫자 입력 : ')

print('입력한 숫자 : ', num)
print('num type :', type(num)) #run에 11입력 하면 출력방식대로 출력됨(str로 출력되어 문자열임='5')

#입력받은 문자열을 숫자로 변환
result = int(num) # '5'-> 5로 변환
print('result :', result)
print('result type :', type(result))

#서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 4, 27, '화')) #순서대로 대입해서 출력

#포맷문자 출력
print('이름 : {}, 나이 : {}, 주소 : {}'.format('김유신', 23, '김해시'))
