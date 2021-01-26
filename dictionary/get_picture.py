import json, re
import urllib.request as urllib2
import requests
from time import strftime, localtime,sleep


def getBaidu(keyword):
    keyword = urllib2.quote(keyword)
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+keyword+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word='+keyword+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=wallpaper&pn=1&rn=5s&gsm=1e&1534226537567='
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    try:
        request = urllib2.Request(url, headers=headers)
        source_code = urllib2.urlopen(request,timeout=20).read().decode('utf-8')

        pattern = re.compile(r'(?<="thumbURL":").*?(?=")"')
        pic_url = pattern.findall(source_code)

        all_url = []
        for i in pic_url:
            all_url.append(i)
        return json.dumps({'url':all_url})

    except urllib2.error.URLError:
        if hasattr(e,"code"):
            print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)


# Bing图片, 暂未启用
def getBing(keyword):
    keyword = urllib2.quote(keyword)
    url = "https://cn.bing.com/images/async?q={}&first=1&count=35&relp=35&tsc=ImageHoverTitle&datsrc=I&layout=RowBased&mmasync=1".format(keyword)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

    try:
        request = urllib2.Request(url, headers=headers)
        source_code = urllib2.urlopen(request, timeout=20).read().decode("utf-8")


        pattern = re.compile(r'src=".*?"')
        all_url = pattern.findall(source_code)

        for i in range(0, len(all_url)):
            all_url[i] = all_url[i].replace('"',"").replace("src=","")

        return all_url

    except urllib2.error.URLError:
        if hasattr(e,"code"):
            print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)


getBaidu("what")
