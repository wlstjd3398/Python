"""
날짜 : 2021/05/20
이름 : 김철학
내용 : 파이썬 CRUD 프로그램
"""

#C Create -> insert
#R Read -> select
#U Update -> update
#D Delete -> delete

"""
날짜 : 2021/05/20
이름 : 김철학
내용 : 파이썬 CRUD 프로그램
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='wlstjd3398',
                       password='1234',
                       db='wlstjd3398',
                       charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    result = int(input('입력 : '))

    if result == 0:
        break
    elif result == 1:
        # 사용자 데이터 입력
        uid  = input('아이디 입력 : ')
        name = input('이름 입력 : ')
        hp   = input('휴대폰 입력 : ')
        age  = input('나이 입력 : ')

        # print(uid, name, hp, age)

        # SQL 실행객체 생성
        cur = conn.cursor()

        # SQL 실행
        sql = "INSERT INTO `USER1` VALUES ('%s', '%s', '%s', %s);"
        cur.execute(sql % (uid, name, hp, age))
        conn.commit()

        print('INSERT 완료...')
    elif result == 2:
        # 사용자 조회
        # SQL 실행객체 생성
        cur = conn.cursor()
        # SQL 실행
        sql = "SELECT * FROM `USER1`;"
        cur.execute(sql)

        # 결과 출력
        for row in cur.fetchall():
            print('--------------------')
            print('아이디 :', row[0])
            print('이름 :', row[1])
            print('휴대폰 :', row[2])
            print('나이 :', row[3])
            print('--------------------')

    elif result == 3:
        # 사용자 검색
        uid = input('검색할 아이디 : ')

        cur = conn.cursor()

        sql = "SELECT * FROM `USER1` WHERE `uid`='%s';"
        cur.execute(sql % uid)
        rows = cur.fetchall()

        if len(rows) == 0:
            # SELECT 결과가 없을 경우
            print('해당하는 사용자가 없습니다.')
        else:
            # SELECT 결과가 있을 경우
            for row in rows:
                print('-------------------')
                print('아이디 :', row[0])
                print('이름 :', row[1])
                print('휴대폰 :', row[2])
                print('나이 :', row[3])
                print('-------------------')

    elif result == 4:
        # 사용자 삭제
        uid = input('삭제할 아이디 : ')

        cur = conn.cursor()

        sql = "DELETE FROM `USER1` WHERE `uid`='%s';"
        rs = cur.execute(sql % uid)
        conn.commit()

        if rs > 0:
            print('DELETE 완료...')
        else:
            print('삭제할 아이디가 존재하지 않습니다.')


# 데이터베이스 종료
conn.close()

print('데이터베이스 프로그램 종료...')