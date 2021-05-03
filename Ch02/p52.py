# (1) 특정 글자 수 반환
oneLine = "this is one Line string"
print('t 글자 수 : ', oneLine.count('t'))

# (2) 접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

# (3) 문자열 교체
print(oneLine.replace('this', 'that'))

# (4) 문자열 분리(split) : 문단 -> 문장
multiLine = """this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 : ', sent)

# (5) 문자열 분리(split)2 : 문장 -> 단어
words = oneLine.split(' ')   # split(sep =' ') : default
print('단어 : ', words)

# (6) 문자열 결합(join) : 단어 -> 문장
sent2 = ','.join(words) # '구분자'.join(string)
print(sent2)    # this,is,one,line,string
