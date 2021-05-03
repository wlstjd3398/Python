# (1) 튜플 자료형 변환
lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

# (2) 튜플 관련 함수
print(len(t3), type(t3))    # 5 <class 'tuple'>
print(t3.count(3))
print(t3.index(4))
