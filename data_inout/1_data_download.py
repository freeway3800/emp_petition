from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import time
import re
import pandas as pd
import sys

# 2일 간격 한번 실행
# 데이터 다운로드 후 정리
""" class 데이터 추출.
    1. 제목
    2. 동의수
    3. 링크
    -->pandas-> 데이터 분석 -> 제목/ 추천수 검색

"""
df_txt= []
df_link_txt=[]
for page in range(1, 5, 1):
    url = "https://www1.president.go.kr/petitions/best?page={}".format(page)
    html = urlopen(url)
    petition = BeautifulSoup(html, 'html.parser')
    # 필요내용 추출
    df = petition.findAll('div', {'class': 'bl_wrap'})
    #필요 링크 추출(1)
    df_link= petition.findAll(href=re.compile('/petitions/+[0-9]{6,}\?'))
    #필요 링크 추출(2)
    link_search= re.compile('(?![/petitions/])[0-9]{6,}')
    #필요링크들
    links=link_search.findall (str(df_link))

    time.sleep(2)
    for Quantity in range(0, len(df), 1):
        try:
            # 제목 추출
            ds = df[Quantity].find('a', {'class': 'cb'}).get_text()
            # 조회수 추출
            df_qua = df[Quantity].find('div', {'bl_agree cb wv_agree'})
            qua_search = re.compile('[0-9]+')
            qua = qua_search.findall(str(df_qua))
            qua = int(qua[0] + qua[1])
            name = ds.strip('\n 제목 ')

            # 리스트 만들기
            doc_dict = {'name': name, 'qua': qua}
            df_txt.append(doc_dict)

        except:
            print('')

    for i in range(0, len(links), 1):
        link = "https://www1.president.go.kr/petitions/{}?navigation=best".format(links[i])
        df_link_txt.append(link)

df=pd.DataFrame(df_txt)
df['link']= df_link_txt
df.columns=["제목","청원수","링크"]
df.to_csv('df.csv')
