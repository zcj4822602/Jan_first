# -*- coding:utf-8 -*-
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

url = 'https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html'
url1 = 'http://top.baidu.com/buzz?b=7&fr=topindex'
page = urlopen(url1).read()

soup = BeautifulSoup(page,'html.parser')
#name = <td class = keyword <a class =list-title
#search_count = <td class = last>
m = len(soup.select('.list-title'))
print(soup.select('.list-title'))
print(m)
# for i in range(m):
#     print(soup.select('.list-title')[i])
# soup.select('.last')
print(soup.select('.last > span'))
n = len(soup.select('.last > span'))
print(n)
i=0
#先初始化置空排行
with open(r'C:\Users\Jan\Desktop\list.txt', 'w') as f:
    f.writelines('')
#一次性输出
try:
    if m == n:
        for i in range(m):
            l = soup.select('.list-title')[i].get_text()
            k = soup.select('.last > span')[i].get_text()
            q = l +'     ' + k + '\n'
            with open(r'C:\Users\Jan\Desktop\list.txt','a') as f:
                f.writelines(q)
                print('今日小说排行榜：%s              搜索指数：%s' %(l,k))
    else:
        print('lenth is not the same')
except Exception as error:
    print('error')












