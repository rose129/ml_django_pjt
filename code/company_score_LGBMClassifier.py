import numpy as np
import pandas as pd
import os
from konlpy.tag import Okt
from collections import Counter
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from lightgbm import LGBMClassifier

import warnings
warnings.filterwarnings('ignore')
okt = Okt()


stopwords = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/FastCampusDataset/master/korean_stopwords.txt").values.tolist()


def apply_regular_expression(text):
    hangul = re.compile("[^ ㄱ-ㅣ 가-힣\s]")  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
    result = hangul.sub("", text)  # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
    return result

def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 정규 표현식 처리
    result = hangul.sub('', text)
    okt = Okt()  # 형태소 추출
    nouns = okt.nouns(result)
    nouns = [x for x in nouns if len(x) > 1]  # 한글자 키워드 제거
    nouns = [x for x in nouns if x not in stopwords]  # 불용어 제거
    return nouns


df = pd.read_csv("data/T4.csv")

summary = []
for t in df["text"]:
    tt = apply_regular_expression(t)
    summary.append(tt)
df["text"] = summary
df["text"] = df["text"].str.replace(pat=r"[^\w]", repl=r" ", regex=True)

vect = CountVectorizer(tokenizer = lambda x: text_cleaning(x))
vect_two = vect.fit_transform(df["text"].tolist())

tfidf_vectorizer = TfidfTransformer()
tf_idf_vect = tfidf_vectorizer.fit_transform(vect_two)

invert_index_vectorizer = {v: k for k, v in vect.vocabulary_.items()}

x = tf_idf_vect
y = df["y"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=1)

lr = LGBMClassifier(n_estimators=400, learning_rate=0.1)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print('accuracy: %.2f' % accuracy_score(y_test, y_pred))
print('precision: %.2f' % precision_score(y_test, y_pred))
print('recall: %.2f' % recall_score(y_test, y_pred))
print('F1: %.2f' % f1_score(y_test, y_pred))

importances = lr.feature_importances_

coef_pos_index = np.argsort(importances)[1:]
coef_neg_index = np.argsort(importances)[::-1]

coef_pos_index = sorted(((value, index) for index, value in enumerate(coef_pos_index)), reverse = True)
coef_neg_index = sorted(((value, index) for index, value in enumerate(coef_neg_index)), reverse = False)




df_pos = pd.DataFrame()
pos_key_list = []
pos_level_list = []

for coef in coef_pos_index[:2000]:
    
    keyword,level = invert_index_vectorizer[coef[1]], coef[0]
    pos_key_list.append(keyword)
    pos_level_list.append(level)
    

df_pos["keyword"] = pos_key_list
df_pos["level"] = pos_level_list

df_neg = pd.DataFrame()
neg_key_list = []
neg_level_list = []

for coef in coef_neg_index[:2000]:
    
    keyword,level = invert_index_vectorizer[coef[1]], coef[0]
    neg_key_list.append(keyword)
    neg_level_list.append(level)
    

df_neg["keyword"] = neg_key_list
df_neg["level"] = neg_level_list

df_total_review = pd.read_csv("data/company_review.csv")
df_name = df_total_review["com_name"]
df_name2 = df_name.drop_duplicates()

len_count = []
for name in df_name2:
    a = name == df_name
    b = len(df_total_review.loc[a,"com_name"])
    len_count.append(b)

df_total_review = pd.read_csv("data/company_review.csv")
error = df_total_review[df_total_review["com_name"]=="스마트웰니스"].index
df_total_review = df_total_review.drop(error)

total_company_score = []
pos_count_list = []
neg_count_list = []

for l in len_count:
        name = df_total_review["com_name"][:l]
        rating = df_total_review["rating"][:l]
        text = df_total_review["recap"][:l]
        df_total_review = df_total_review.drop(df_total_review.index[:l],axis = 0)
        df_company = pd.DataFrame()
        df_company["name"] = name
        df_company["rating"] = rating
        df_company["rating"] = df_company["rating"].str.replace("점","")
        df_company["rating"] = df_company["rating"].astype("int64")
        df_company["text"] = text
       
        summary = []
        for t in df_company["text"]:
            tt = apply_regular_expression(t)
            summary.append(tt)
            
        df_company["text"] = summary
        try:
            df_company["text"] = df_company["text"].str.replace(pat=r"[^\w]", repl=r" ", regex=True)
        except:
            print(name * 20)
            
        df_company = df_company.reset_index()
    
        corpus = "".join(df_company["text"].tolist())
        corpus_mor = text_cleaning(corpus)
      
        corpus_mor_temp_pos = corpus_mor.copy()
        corpus_mor_result_pos = corpus_mor.copy()

        for i in pos_key_list:
            if i not in corpus_mor_temp_pos:
                corpus_mor_result_pos.append(i)
            else:
                corpus_mor_temp_pos.remove(i)
        
    
        corpus_mor_temp_neg = corpus_mor.copy()
        corpus_mor_result_neg = corpus_mor.copy()
        
        for i in neg_key_list:
            if i not in corpus_mor_temp_neg:
                corpus_mor_result_neg.append(i)
            else:
                corpus_mor_temp_neg.remove(i)
        
        
        
        pos_count = len(corpus_mor_temp_pos)
        neg_count = len(corpus_mor_temp_neg)

      

        company_score_pos = 0
        company_score_neg = 0

        if pos_count >= 149:
            company_score_pos = 5
        elif 149 > pos_count >= 112:
            company_score_pos = 4
        elif 112 > pos_count >= 75:
            company_score_pos = 3
        elif 75 > pos_count >= 38:
            company_score_pos = 2
        else:
            company_score_pos = 1

        if neg_count >= 149:
            company_score_neg = 1
        elif 149 > neg_count >= 112:
            company_score_neg = 2
        elif 112 > neg_count >= 75:
            company_score_neg = 3
        elif 75 > neg_count >= 38:
            company_score_neg = 4
        else:
            company_score_neg = 5

        score_list = []
        score_list.append(company_score_pos)
        score_list.append(company_score_neg)

        if score_list[0] < score_list[1]:
            score_average = np.mean(score_list)
            score_average = score_average - 1
        else:
            score_average = np.mean(score_list)
        
        total_company_score.append(score_average)


final_df = pd.DataFrame()
final_df["company"] = df_name2
final_df["score"] = total_company_score

final_df.to_csv('data/ml_final.csv', sep=',', index=False, encoding='utf-8')