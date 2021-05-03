# (1) list에 자료 저장하기
import random


lst = []    # 빈 list 만들기
for i in range(10) : # 0~9
    r = random.randint(1, 10)    # 난수 발생
    lst.append(r)   # 난수 저장

print('lst=', lst)  # 난수 출력

# (2) list에 자료 참조하기
for i in range(10) :    # 0~9
    print(lst[i] * 0.25)    # 난수 * 0.25
