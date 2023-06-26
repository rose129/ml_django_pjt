import csv
from mydb__env import *
import pymysql
from emoji import core

# DB 연결하기
conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


sql_query = "DROP TABLE IF EXISTS word_cloud"
cur.execute(sql_query)

# Open the CSV file
with open('data/word_cloud_review_final.csv', 'r', encoding='utf-8') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the data from the row
        company_name = row[0]
        ttl_merit = core.replace_emoji(row[1], replace="")
        ttl_demerit = core.replace_emoji(row[2], replace="")
        ttl_review = core.replace_emoji(row[3], replace="")

        # Construct the SQL query with placeholders
        sql_query = """
        INSERT INTO word_cloud(company_name, ttl_merit, ttl_demerit, ttl_review)
        VALUES (%s, %s, %s, %s)
        """

        # Execute the SQL query with the data as parameters
        cur.execute(sql_query, (company_name, ttl_merit, ttl_demerit, ttl_review))

    # Commit the changes to the database
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()