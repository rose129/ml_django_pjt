import pandas as pd     
import plotly           
import plotly.express as px
import csv
import plotly.offline as pyo
import webbrowser



csv_path='data/all_recruit_clean_v3.csv'
df = pd.read_csv(csv_path)

df['스택']= df['스택'].str.replace("'",'')

stack = df['스택']
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
    if i == 'CSS자바 스크립트':
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

t_df = pd.DataFrame({'스택':r_total})
t_df = t_df['스택'].value_counts()[:11]

print(t_df)


# print(t_df.index)
# print(t_df.values)

# fig = px.bar(t_df, x= t_df.index, y= t_df.values)
# fig.update_layout(
#         hoverlabel_bgcolor="white",
#         hoverlabel_font_color="blue"
#         )
# fig.update_traces(hovertemplate='스택: %{x} <br>'+
#                                 '인기도: %{y} <br>')
# fig.to_json()
# fig.show()
# hoverlabel_font_size="텍스트 사이즈"
# hoverlabel_font_family="텍스트 서체"
# pyo.plot(fig, filename='st.html')


# webbrowser.open('chart.html')