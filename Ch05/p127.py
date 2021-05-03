# 피타고라스 정리
def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print("3변의 길이 : ",a,b,c)

pytha(2, 1) # s, t의 인수는 양의 정수를 갖는다
