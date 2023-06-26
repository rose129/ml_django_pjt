import pymysql
import os
from mydb__env import *
import csv
import charset_normalizer

# DB 연결하기
conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# company_info 테이블이 존재하면 삭제하기
sql_query = "DROP TABLE IF EXISTS company_info"
cur.execute(sql_query)

# db table 생성
sql_query = """
CREATE TABLE IF NOT EXISTS company_info(
    company_name VARCHAR(20) PRIMARY KEY,
    industry_field VARCHAR(100),
    workforce VARCHAR(20),
    company_type VARCHAR(30),
    est_date VARCHAR(30),
    capital VARCHAR(30),
    sales VARCHAR(30),
    ceo VARCHAR(50),
    initial_salary VARCHAR(30),
    main_business VARCHAR(200),
    insurance VARCHAR(30),
    website VARCHAR(50),
    address VARCHAR(200),
    subsidiary VARCHAR(200)
   
)
"""

cur.execute(sql_query)

# Open the CSV file
with open('data/company_info_list.csv', 'r', encoding='utf-8') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the data from the row
        company_name = row[0]
        industry_field = row[1]
        workforce = row[2]
        company_type = row[3]
        est_date = row[4]
        capital = row[5]
        sales = row[6]
        ceo = row[7]
        initial_salary = row[8]
        main_business = row[9]
        insurance = row[10]
        website = row[11]
        address = row[12]
        subsidiary = row[13]

        # Construct the SQL query with placeholders
        sql_query = """
        INSERT INTO company_info (company_name, industry_field, workforce, company_type, est_date, capital, sales, ceo, initial_salary, main_business, insurance, website, address, subsidiary)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the SQL query with the data as parameters
        cur.execute(sql_query, (
            company_name, industry_field, workforce, company_type, est_date, capital, sales, ceo, initial_salary,
            main_business, insurance, website, address, subsidiary
        ))

    # Commit the changes to the database
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()