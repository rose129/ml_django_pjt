import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import nltk
import re
# warning 무시
import warnings
warnings.filterwarnings('ignore')

# '-' 깨짐 해결 모듈
import matplotlib as mpl

plt.rcParams["font.family"] = "Malgun Gothic"  # For Windows
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (8,4)
print(plt.rcParams["font.family"])

# 마이너스 깨짐 해결
mpl.rcParams["axes.unicode_minus"] = False

df = pd.read_csv('ml_datas/word_cloud_review_1.csv', encoding='utf-8')
df.head()

data1 = df.loc[df['기업명'] == '(주)굿닥', :]
[x for x in data1['장점']]
data2 = df.loc[df['기업명'] == '(주)굿닥', :]
[x for x in data2['단점']]

text1 = ''
for i in data1['장점']:
    text1 += i+'. '
# print(text1)
text2 = ''
for i in data2['단점']:
    text2 += i+'. '
# print(text2)

from konlpy.tag import Komoran
komoran = Komoran()
nouns1 = komoran.nouns(text1)
nouns2 = komoran.nouns(text2)
# nouns1[:10]
# nouns1

### list로 변경
nouns3 = []
for n in nouns1:
    if len(n) > 1:
        nouns3.append(n)
# nouns3
nouns4 = []
for n in nouns2:
    if len(n) > 1:
        nouns4.append(n)

from collections import Counter
count1 = Counter(nouns1)
count2 = Counter(nouns2)
top1 = count1.most_common(100)
top2 = count2.most_common(100)
# print(top1)
# print(top2)

kostw_data =  "https://raw.githubusercontent.com/byungjooyoo/Dataset/main/korean_stopwords.txt"
pd.read_csv(kostw_data).to_csv("ml_datas/korean_stopwords.txt", index=False, encoding="utf-8")

stop_words=[]
with open("ml_datas/korean_stopwords.txt", 'r', encoding="utf-8") as f:
    while True:
        line = f.readline().strip()
        stop_words.append(line)
        if not line: break
# print(stop_words)

stop_words = ['수','것'] + stop_words
dic1 = dict(top1)
for i in stop_words:
    if i in dic1:
        del dic1[i]
# print(dic1)

dic2 = dict(top2)
for i in stop_words:
    if i in dic2:
        del dic2[i]
# print(dic2)

pos = nltk.Text(nouns1)
plt.figure(figsize=(8,8))
plt.title("굿닥")
pos.plot(30) 

pos = nltk.Text(nouns2)
plt.figure(figsize=(8,8))
plt.title("굿닥")
pos.plot(30) 


icon = Image.open('images/thumbs_up.png').convert("RGBA")
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

stop_words = ['것','수','회사','사람','직원']
dic1 = dict(top1)
[dic1.pop(key) for key in stop_words]
f_path = 'fonts/NanumMyeongjoExtraBold.ttf'
wordcloud = WordCloud(font_path=f_path,
                      background_color='white', 
                      width=500, 
                      height=500,
                      mask=mask,
                      colormap='viridis').generate_from_frequencies(dic1)
fig = plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

icon2 = Image.open('images/thumbs_down.png').convert("RGBA")
# icon = Image.open('images/heart.png').convert("RGBA")
mask2 = Image.new("RGB", icon2.size, (255,255,255))
mask2.paste(icon2,icon2)
mask2 = np.array(mask2)

stop_words = ['것','수','회사','사람','직원']
dic2 = dict(top2)
[dic2.pop(key) for key in stop_words]
f_path = 'fonts/NanumMyeongjoExtraBold.ttf'
wordcloud = WordCloud(font_path=f_path,
                      background_color='white', 
                      width=800, 
                      height=800,
                      mask=mask2,
                      colormap='plasma').generate_from_frequencies(dic2)
fig = plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

