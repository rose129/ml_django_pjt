import pymysql
import os
from mydb_env import *
import csv
import charset_normalizer

# DB 연결하기
conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# company_info 테이블이 존재하면 삭제하기
sql_query = "DROP TABLE IF EXISTS startup_ranking"
cur.execute(sql_query)

# db table 생성
sql_query = """
CREATE TABLE IF NOT EXISTS startup_ranking(
    logo TEXT,
    ranking VARCHAR(15),
    company_name VARCHAR(20) PRIMARY KEY,
    recap VARCHAR(100)
)
"""

cur.execute(sql_query)


# Open the CSV file
with open('data/startup_300.csv', 'r', encoding='utf-8') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    next(reader)

    # Sort the data by 'ranking' column in ascending order
    sorted_data = sorted(reader, key=lambda row: int(row[1].rstrip('위')))

    # Iterate over each row in the CSV file
    for row in sorted_data:
        # Extract the data from the row
        logo = row[0]
        ranking = row[1].rstrip('위')
        company_name = row[2]
        recap = row[3]

        # Construct the SQL query with placeholders
        sql_query = """
        INSERT INTO startup_ranking (logo, ranking, company_name, recap)
        VALUES (%s, %s, %s, %s)
        """

        # Execute the SQL query with the data as parameters
        cur.execute(sql_query, (
            logo, ranking, company_name, recap
        ))

    # Commit the changes to the database
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()