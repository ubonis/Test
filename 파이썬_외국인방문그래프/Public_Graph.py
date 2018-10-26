import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import json
import pandas as pd


# 한글 폰트 등록
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
Tour_data = []
Tour_date = []
American_Visit_data = []
American_Visit_date = []
Japan_Visit_data = []
Japan_Visit_date = []
China_Visit_data = []
China_Visit_date = []
with open("서울특별시_관광지입장정보_2011_2016.json", 'r', encoding='utf8') as rfile:
    TourPoint = json.load(rfile )
for item in TourPoint:
    if item['resNm'] == '경복궁':
        Tour_data.append(item['ForNum'])
        Tour_date.append(item['yyyymm'])
    #     print(item['resNm'], item['ForNum'], item['yyyymm'])

with open("미국_해외방문객정보_2011_2016.json", 'r', encoding='utf8') as rfile:
    VisitForin = json.load(rfile)
#print(VisitForin)
for item in VisitForin:
    American_Visit_data.append(item['visit_cnt'])
    American_Visit_date.append(item['yyyymm'])

with open("일본_해외방문객정보_2011_2016.json", 'r', encoding='utf8') as rfile:
    VisitForin = json.load(rfile)
#print(VisitForin)
for item in VisitForin:
    Japan_Visit_data.append(item['visit_cnt'])
    Japan_Visit_date.append(item['yyyymm'])

with open("중국_해외방문객정보_2011_2016.json", 'r', encoding='utf8') as rfile:
    VisitForin = json.load(rfile)
#print(VisitForin)
for item in VisitForin:
    China_Visit_data.append(item['visit_cnt'])
    China_Visit_date.append(item['yyyymm'])
#     print(item['nat_name'], item['visit_cnt'], item['yyyymm'])
# print(Tour_data)
# print(Visit_data)
df1 = pd.DataFrame(Tour_data, index=Tour_date, columns=['경복궁'])
df2 = pd.DataFrame(American_Visit_data,index=American_Visit_date, columns=['미국인'])
df3 = pd.DataFrame(Japan_Visit_data,index=Japan_Visit_date, columns=['일본인'])
df4 = pd.DataFrame(China_Visit_data,index=China_Visit_date, columns=['중국인'])
print(df1)
print(df2)
print(df3)
print(df4)

result = pd.concat([df1,df2,df3,df4],axis=1)
sort_result = result.sort_values(by='경복궁', ascending=True)
print(sort_result)
plt.figure()
plt.scatter(sort_result.loc[:,['미국인']], sort_result.loc[:,['경복궁']], label='미국인')
plt.scatter(sort_result.loc[:,['일본인']], sort_result.loc[:,['경복궁']], label='일본인')
plt.scatter(sort_result.loc[:,['중국인']], sort_result.loc[:,['경복궁']], label='중국인')
plt.legend()
plt.xlabel("외국인 입국수")
plt.ylabel('경복궁 입장인원')
plt.show()
