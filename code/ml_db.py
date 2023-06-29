import pandas as pd     
import plotly           
import plotly.express as px
import csv
import plotly.offline as pyo
import webbrowser
from mydb__env import *
import pymysql

# DB연결
conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
# 커서생성
cur = conn.cursor()

sql = """

SELECT stack FROM recruting_info

"""
cur.execute(sql)

result_data = cur.fetchall()

# print(result_data)

# DB닫기
conn.close()

df = pd.DataFrame(result_data)

# print(df[0])

df[0]= df[0].str.replace("'",'')

stack = df[0]
total = []
for st in stack:
    stsp = st.split(',')
    # print(b)
    # print(len(b))
    for i in stsp:
        i = i.strip()
        # print(i.strip())
        total.append(i)
# print(total)

total_list = []
r_total = []
for i in total:
    if i == 'CSS 자바 스크립트':
        r_total.append('CSS')
        r_total.append('JavaScript')
    elif i == 'CSS3':
        r_total.append('CSS')
    elif i == '자바스크립트':
        r_total.append('JavaScript')
    elif i == 'VueJS':
        r_total.append('Vue.JS')
    elif i == 'HTML5':
        r_total.append('HTML')
    elif i == 'React.js':
        r_total.append('React')
    elif i == 'NodeJS':
        r_total.append('Node.js')
    elif i == 'C / C++':
        r_total.append('C')
        r_total.append('C++')
    elif i == 'Amazon Web Service':
        r_total.append('AWS')
    elif i == 'Spring Framework':
        r_total.append('Spring')
    else:
        r_total.append(i)

t_df = pd.DataFrame({'stack':r_total})
t_df = t_df['stack'].value_counts()[:20]
# t_df2 = t_df['stack'].value_counts()[10:20]

# print(t_df.index)
# print(t_df.values)

fig = px.bar(t_df, x= t_df.index, y= t_df.values,
            color_discrete_map = {'JavaScript': '#7FD4C1', 'B': '#30BFDD', 'C': '#8690FF', 
                                   'D': '#ACD0F4', 'E': '#F7C0BB'})
fig.update_layout(
        # hoverlabel_bgcolor="white",
        # hoverlabel_font_color="blue",
        hoverlabel=dict(
        bgcolor="white",
        font=dict(color="black",size=13),
        bordercolor="black"
        ),
        plot_bgcolor='white',
        xaxis=dict(
            title="<b>스택</b>"  # x축 값의 글꼴 두꺼움 설정
         ),
        yaxis=dict(
        title=None  # y축 제목 없음
        ),
        )
fig.update_traces(hovertemplate='스택: %{x} <br>'+'채용기업: %{y}', textfont_color='black',marker=dict(color='#0f4667'))
# fig.update_traces(hovertemplate='스택: %{x} <br>'+
#                                 '인기도: %{y} <br>')
fig.to_json()
fig.show()
# hoverlabel_font_size="텍스트 사이즈"
# hoverlabel_font_family="텍스트 서체"
pyo.plot(fig, filename='st9.html')

# webbrowser.open('st3.html')