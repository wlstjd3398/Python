"""
날짜 : 2021/05/20
이름 : 김철학
내용 : 파이썬 데이터베이스 SQL 실습하기
import pymysql(terminal로 설치)
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114', user='wlstjd3398', password='1234', db='wlstjd3398', charset='utf8')

# 실행 객체 생성
cur = conn.cursor()

# SQL실행
sql = "INSERT INTO `USER1` VALUES ('p101', '김유신', '010-1234-1001', 25);"
cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()

print('INSERT 완료...')
