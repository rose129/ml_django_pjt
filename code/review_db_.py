import csv
from mydb__env import *
import pymysql
from emoji import core

f = open('data/total_review_list_final.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr)
n = 0
review = []
for i in rdr:
    if i[3] == '전직원':
        i[3] = 0
    elif i[3] == '현직원':
        i[3] = 1

    i[4] = i[4].rstrip('점')
    i[5] = core.replace_emoji(i[5], replace="")
    i[6] = core.replace_emoji(i[6], replace="")

    review.append(i)


conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset="utf8")
cur = conn.cursor()
# print(cur)

sql_query = "DROP TABLE IF EXISTS Company_Review"
cur.execute(sql_query)
# 0 기업명 
# 1 날짜
# 2 직무
# 3 재직여부
# 4 별점
# 5 요약
# 6 장점
# 7 단점
# 8 경영진


sql_query = """
CREATE TABLE IF NOT EXISTS Company_Review(
company_name3 varchar(20) NOT NULL,
reporting_date varchar(50),
job varchar(15) NOT NULL,
working_status BOOL NOT NULL,
rating int NOT NULL,
recap TEXT NOT NULL,
merit TEXT NOT NULL,
demerit TEXT NOT NULL,
suggestion_mgt TEXT NOT NULL

)
"""
cur.execute(sql_query)

for i in review:
    # print(i[8])
    review_list =[
        [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
    ]
    cur.executemany("INSERT INTO Company_Review(company_name3, reporting_date, job, working_status, rating, recap, merit, demerit, suggestion_mgt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", review_list)
    conn.commit()
    
# DB닫기
cur.close()
conn.close()

f.close()