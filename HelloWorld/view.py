from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test, User
from TestModel.helper import myThread
# 爬虫相关
from urllib.request import urlopen;
from bs4 import BeautifulSoup;


def hello(request):
    # 创建新线程
    repet = 1
    while repet <= 5:
        print(repet)
        thread = {}
        thread[repet] = myThread(repet, "Thread-" + str(repet), 1)
        # 开启新线程
        thread[repet].start()
        # thread[repet].join()
        repet += 1
    print ("退出主线程")
    response = ''
    context = {}
    # return HttpResponse("hello world !")
    context['datas'] = Test.objects.all().values('name', 'id')
    print(context['datas'])
    # context['datas'] = {'key1':1,'key2':2}
    return render(request, 'hello.html', context)  # !/usr/bin/python3


# 爬虫
def scrape(request):
    # res = User.objects.all()
    # print(res)
    obj = getNode()
    print(obj)
    if obj == None:
        print("节点不存在！");
    else:
        print("节点存在：" + str(obj.body.h1))
    return HttpResponse("it's over")  # !/usr/bin/python3


# 获取节点
def getNode():
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    # except (HTTPError, URLError) as e
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
    except AttributeError as e:
        return None
    return bsObj
