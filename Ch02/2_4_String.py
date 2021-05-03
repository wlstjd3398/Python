"""
날짜 : 2021/04/26
이름 : 김철학
내용 : 파이썬 String 예제 교재  p48
"""

#문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 + str2

print('str3 : ', str3)

#문자열 곱하기
name ='홍길동'
print('name * 3 :', name * 3)

#문자열 길이
msg = 'Hello World'
print('msg 길이 :', len (msg))

#문자열 인덱스
print('msg 1번째 문자 :', msg[0])
print('msg 7번째 문자 :', msg[6])
print('msg -1번째 문자 :', msg[-1])
print('msg -5번째 문자 :', msg[-5])

#문자열 자르기(substring)[start:end]
print('msg 0~5까지 문자열 :', msg[0:5])
print('msg 0~5까지 문자열 :', msg[:5]) #start 없는 경우 생략해서 나옴
print('msg 6~11까지 문자열 :', msg[6:11])
print('msg 6~11까지 문자열 :', msg[6:]) #end 없는 경우 생략해서 나옴

#문자열 분리(분리되는것을 token이라고함)
people = '김유신|김춘추|장보고|강감찬|이순신' #token 5개
p1, p2, p3, p4, p5 = people.split('|') #구분자가 |

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

#문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주') #개행 한줄 띄워라
print('서울\t대전\t대구\t부산\t광주') #t = tab
print('저는 \'홍길동\' 입니다.') #홍길동 이름 강조 \를 문자로 표현한다
print("저는 '홍길동' 입니다.") #파이썬은 이 방법으로 가능하다

#
