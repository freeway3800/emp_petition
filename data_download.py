from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import re
import sys

sys.stdout= open('df.txt','w')
document = []
for page in range(1, 3, 1):
    url = "https://www1.president.go.kr/petitions/best?page={}".format(page)
    html = urlopen(url)
    petition = BeautifulSoup(html, 'html.parser')
    # 필요내용 추출
    df = petition.findAll('div', {'class': 'bl_wrap'})
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
            print(name,qua,sep='\t')

            # 리스트 만들기
            doc_dict = {'name': name, 'qua': qua}
            document.append(doc_dict)

        except:
            print('')


sys.stdout.close()



