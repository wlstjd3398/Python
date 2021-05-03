"""
날짜 : 2021/05/03
이름 : 김철학
내용 : 파이썬 외부 패키지 설치 실습 교재 p239
"""

from openpyxl import Workbook

# Excel 파일 쓰기

# 엑셀파일 객체생성
workbook = Workbook()   # 엑셀파일객체 = 클래스

# 활성화된 sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '홍길동'
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고'])
sheet.cell(6, 2, '사과')
# 6행 2열

# 엑셀파일 저장
workbook.save('C:/Users/bigdata/Desktop/sample.xlsx')
workbook.close()


