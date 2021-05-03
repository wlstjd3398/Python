# (1) 단어 데이터 셋
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {} # 빈 셋

# (2) get() 함수 이용 : key 이용 value 가져오기
for key in charset :
    wc[key] = wc.get(key, 0) + 1    # get() 이용
print(wc)