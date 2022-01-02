from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import time

html= urlopen("https://www1.president.go.kr/petitions/best?page=1")
petition= BeautifulSoup(html, 'html.parser')
