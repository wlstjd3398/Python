from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

# (1) 산술평균
def Avg(data):
    avg = mean(data)
    return avg

print('산술평균 =', Avg(dataset))

# (2) 분산/표준편차
def var_sd(data):
    avg = Avg(data) # 함수 호출
    # list 내포
    diff = [(d - avg)**2 for d in data]

    var = sum(diff) / (len (data) - 1)
    sd = sqrt(var)
    return var, sd

# (3) 함수 호출
v, s = var_sd(dataset)
print('분산=', v)
print('표준편차=', s)