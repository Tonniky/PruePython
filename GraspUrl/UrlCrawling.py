import urllib.request
from bs4 import BeautifulSoup

url="http://finance.qq.com/gdyw.htm"
head = {}
head['user_agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())

# print('dd')
