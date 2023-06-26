from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json
from bs4 import BeautifulSoup as bs
import os
import datetime
from mydb_env import *
import pymysql
import requests as req
import csv
import re


# demo 사이트 누적 300위까지 크롤링 
qq = []


for ii in range(1,4):
    url = f'http://www.demoday.co.kr/companies/rank/total/all/{ii}'

    res = req.get(url)
    soup = bs(res.text, 'html.parser')

    li = soup.select('.contents-list .new')

    

    # list = []
    # print(li)
    for i in li:
        list = []
        image = i.select_one('.company-summary img')['src']
        # print(image)
        list.append(image)

        r = i.select_one('h3.title .ranking').get_text(strip=True)
        # r = int(r.rstrip('위'))
        list.append(r)
        # print(type(r))
        
        n = i.select_one('h3.title a').get_text(strip=True)
        # print(n)
        list.append(n)

        
        
        # print(list)
        qq.append(list)
# print(qq)
# -----------------------------------------------------------

# # Chrome WebDriver 경로 설정
# webdriver_path = '/path/to/chromedriver'

# # Chrome WebDriver 옵션 설정
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # GUI 없는 모드로 실행

# # WebDriver 인스턴스 생성
# driver = webdriver.Chrome(service=Service(webdriver_path), options=chrome_options)

# # ----------------------------------------------
# # selenium 기업정보 300개

# qwer = []

# for i in qq:
#     url = f'http://www.demoday.co.kr/company/{i[1]}'
#     print(i[1])
#     driver.get(url)

#     info = []

#     name = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(1) > span.value").text
#     s_year = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(2) > span.value").text
#     employees = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(3) > span.value").text
#     category = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(4) > span.value").text
#     business_areas = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(5) > span.value").text
#     homepage = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(6) > span.value").text
#     facebook = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(7) > span.value").text
#     twitter = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(8) > span.value").text
#     blog = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(9) > span.value").text

    
#     info.append(i[1])
#     info.append(name)
#     info.append(s_year)
#     info.append(employees)
#     info.append(category)
#     info.append(business_areas)
#     info.append(homepage)
#     info.append(facebook)
#     info.append(twitter)
#     info.append(blog)
#     # print(len(info))
#     qwer.append(info)
# # print(len(qwer))

# # -----------------------------------------



# WebDriver 종료
driver.quit()

# # time.sleep(3)
# # driver.close()


data_dir = 'project2/'
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

file_path = f"{data_dir}기업.csv"

with open(file_path, 'w', newline="", encoding='utf-8-sig') as f:
    write = csv.writer(f)

    write.writerow(['순위','기업','이미지'])
    write.writerows(qq)


# file_path2 = f"{data_dir}데모데이_기업별정보.csv"

# with open(file_path2, 'w', newline="", encoding='utf-8-sig') as f:
#     write = csv.writer(f)

#     write.writerow(['기업','대표자','설립년도','임직원수','카테고리','사업분야','홈페이지','페이스북','트위터','블로그'])
#     write.writerows(qwer)













# 몽고반점 (수정해야함)

# import pymongo
# from nosql_info import *

# conn = pymongo.MongoClient(db_info)
# scraper_db = conn.teampro
# item_col = scraper_db.ject2
# item_col.insert_many(qq)






# selenium 반복돌리기전

# url = "http://www.demoday.co.kr/company/리디"

# # 웹 페이지 가져오기
# driver.get(url)

# info = []

# # 요소 찾기
# name = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(1) > span.value").text
# s_year = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(2) > span.value").text
# employees = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(3) > span.value").text
# category = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(4) > span.value").text
# business_areas = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(5) > span.value").text
# homepage = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(6) > span.value").text
# facebook = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(7) > span.value").text
# twitter = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(8) > span.value").text
# blog = driver.find_element(By.CSS_SELECTOR, "#company_details > li:nth-child(9) > span.value").text

# info.append(name)
# info.append(s_year)
# info.append(employees)
# info.append(category)
# info.append(business_areas)
# info.append(homepage)
# info.append(facebook)
# info.append(twitter)
# info.append(blog)

# print(info)
