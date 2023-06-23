import requests as req
import pymysql
import os
import csv
from mydb_env import *

f = open('data/total_review_list_final.csv','r', encoding='UTF8')

review = csv.reader(f)
next(review)
 
# 기업명,날짜,직무,재직여부,별점,요약,장점,단점,경영진에게 바라는 점
total = []
for re in review:
    data = []
    # 기업명
    r1 = re[0]
    # print(re[0])
    # 날짜
    r2 = re[1]
    # 직무
    r3 = re[2]
    # 재직여부
    r4 = re[3]
    # 별점
    r5 = re[4]
    # 요약
    r6 = re[5]
    # 장점
    r7 = re[6]
    # 단점
    r8 = re[7]
    # 경영진에게 바라는 점
    r9 = re[8]

    data.append(r1)
    data.append(r2)
    data.append(r3)
    data.append(r4)
    data.append(r5)
    data.append(r6)
    data.append(r7)
    data.append(r8)
    data.append(r9)


    total.append(data)

print(total)

f.close()

def accessDB(total):
    
    # DB연결
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset )
    # conn.set_character_set('utf8mb4')
    # 커서생성
    cur = conn.cursor()

    # daum_movies 테이블이 존재하면 삭제하기
    sql = "DROP TABLE IF EXISTS company_review"
    cur.execute(sql)

    # 테이블생성
    # 기업명,직무,회사소개,주요업무,자격요건,스택,우대사항,복리후생,회사주소
    sql = """
    CREATE TABLE IF NOT EXISTS company_review (
        company_name VARCHAR(20) NOT NULL,
        reporting_date VARCHAR(50) NULL,
        job VARCHAR(15) NOT NULL,
        working_status VARCHAR(50) NOT NULL,
        rating VARCHAR(50) NOT NULL,
        recap TEXT NOT NULL,
        merit TEXT NOT NULL,
        demerit TEXT NOT NULL,
        suggestion_mgt TEXT NOT NULL
    )

    """
    cur.execute(sql)
    cur.executemany("""
    INSERT INTO company_review(company_name, reporting_date, job, working_status, rating, recap, merit, demerit, suggestion_mgt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, total)

    # db 적용 
    conn.commit()

    result_data = cur.fetchall()

    # DB닫기
    conn.close()
    return result_data

accessDB(total)
