import os
import re
import time
import requests
from bs4 import BeautifulSoup
import lxml




#找规律
# <img class="inn-archive__item__thumbnail__img inn-card_painting__item__thumbnail__img inn__thumbnail__img innsleep-lazyloaded" src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/20617160461771754895.jpg" data-src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/20617160461771754895.jpg" alt="原神萤【ll2021021341326】" width="200" height="300">
# <img class="inn-archive__item__thumbnail__img inn-card_painting__item__thumbnail__img inn__thumbnail__img inn-lazyloaded" src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/16435813002033878947.jpg" data-src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/16435813002033878947.jpg" alt="完具21.2.3小秘书视图 25P+2V628M【ll2021021134108】" width="200" height="300">
# <img class="inn-archive__item__thumbnail__img inn-card_painting__item__thumbnail__img inn__thumbnail__img inn-lazyloaded" src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/96457406400921713096.jpg" data-src="http://xyac88.dsn.zbfxhw.net/wp-content/uploads/2021/02s/96457406400921713096.jpg" alt="狼先生猫小姐视图 [81P+11V65M]【ll2021021133489】" width="200" height="300">

#https://www.xysqu.com/category/sjbz/page/2/
#https://www.xysqu.com/category/sjbz/page/3/

def get_urls(page):
    url = f'https://www.xysqu.com/category/sjbz/page/{page}/'
    r = requests.get(url)
    r.encoding = "utf-8"
    # print(r.text)
    soup = BeautifulSoup(r.text,"lxml")
    links = {}
    linkslist = soup.find_all("img",attrs={"width":"200","height":"300"})
    # print(linkslist)
    for link in linkslist:
        links[link["alt"]] = link["data-src"]
    # print(links)
    # for key,value in links.items():
    #     print(key,value)
    return links

# print(get_urls(1))

    
def download(fname,url):
    r = requests.get(url)
    time.sleep(1)
    try:
        path = fname.replace("/",",")   #有的图片名字里有"/"影响了路径，要把它替换掉
        with open ("%s.jpg"%path,"wb") as fout:
            fout.write(r.content)
    except:
        print("异常",fname)

for page in range(223):
    print("正在爬%d页"%(page+1))
    for fname,url in get_urls(page).items():
        download(fname,url)

