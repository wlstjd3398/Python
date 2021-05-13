"""
날짜 : 2021/05/13
이름 : 홍길동
내용 : 파이썬 리스트에 점수를 입력하고 리스트 총합을 구하기
"""

scores = []

while True:
    print('0:종료, 1:입력')
    result = input('입력 : ')

    if (score==0):
        break
    score = int(input('점수입력 : '))



print('입력한 점수 확인')
print(scores)

sum = 0

for score in scores:
    sum += score

print('리스트 총합 :', sum)
