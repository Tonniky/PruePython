# import urllib.request
# from bs4 import BeautifulSoup
#
# url="http://finance.qq.com/gdyw.htm"
# head = {}
# head['user_agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
#
# html=urllib.request.urlopen(url).read()
# soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())
#


import requests
import re
from bs4 import BeautifulSoup
import csv

url = ['https://cq.lianjia.com/ershoufang/']
for i in range(2,101):
    url.append('https://cq.lianjia.com/ershoufang/pg%s/'%(str(i)))

 # 模拟谷歌浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

for u in url:
    r = requests.get(u,headers=headers)
    soup = BeautifulSoup(r.text,'lxml').find_all('li', class_='clear LOGCLICKDATA')
    for i in  soup:
        ns = i.select('div[class="positionInfo"]')[0].get_text()
        region = ns.split('-')[1].replace(' ','').encode('gbk')
        rem = ns.split('-')[0].replace(' ','').encode('gbk')
        ns =  i.select('div[class="houseInfo"]')[0].get_text()
        xiaoqu_name = ns.split('|')[0].replace(' ','').encode('gbk')
        huxing = ns.split('|')[1].replace(' ','').encode('gbk')
        pingfang = ns.split('|')[2].replace(' ','').encode('gbk')
        chaoxiang = ns.split('|')[3].replace(' ','').encode('gbk')
        zhuangxiu =  ns.split('|')[4].replace(' ','').encode('gbk')
        danjia =  re.findall("\d+",i.select('div[class="unitPrice"]')[0].string)[0]
        zongjia = i.select('div[class="totalPrice"]')[0].get_text().encode('gbk')
        out=open("/data/data.csv",'a')
        csv_write=csv.writer(out)
        data = [region,xiaoqu_name,rem,huxing,pingfang,chaoxiang,zhuangxiu,danjia,zongjia]
        csv_write.writerow(data)
        out.close()


# import urllib.request
# import urllib.error
# try:
#     headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu;Linux x86_64; rv:57.0) Gecko/20100101Firefox/57.0'}
#     response = urllib.request.Request('http://python.org/',
#                                        headers=headers)
#     html = urllib.request.urlopen(response)
#     result = html.read().decode('utf-8')
# except urllib.error.URLError as e:
#     if hasattr(e, 'reason'):
#         print('错误原因是' + str(e.reason))
# except urllib.error.HTTPError as e:
#     if hasattr(e, 'code'):
#         print('错误状态码是' + str(e.code))
# else:
#     print('请求成功通过。')
