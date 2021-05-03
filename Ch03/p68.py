# (1) random 모듈 관련 함수 도움말
import random
help(random.randint)
help(random.choices)    # 모집단에서 k 크기 목록 반환

# (2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동', '이순신', '유관순']
print(names)    # 전체이름
print(names[2]) # , 특정이름 출력

# (3) list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else :
    print('유관순 없음')

# (4) 난수 정수로 이름 선택하기
idx = random.randint(0, 2)
print(names[idx])