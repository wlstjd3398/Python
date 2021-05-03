var = 10    # if 블럭에서 사용될 변수
if var >= 5 :   # 조건식
    print('var=', var)
    print('var는 5보다 크다')
    print('조건이 참인 경우 실행')

print('항상 실행')


# 100 ~ 85 : '우수', 84 ~ 70: '보통', 69이하 : '저조'
score = int(input('점수 입력 :'))
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
        