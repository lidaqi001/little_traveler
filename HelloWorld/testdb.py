# -*- coding:utf-8 -*-
from django.http import HttpResponse

from TestModel.models import Test

import random
import json
import pickle


# 数据库操作


def testdb(request):
    test1 = Test(name='runoob' + str(random.randint(0, 999)))
    test1.save()
    return HttpResponse('<p>数据添加成功！</p>')


def testshow(request):
    # 初始化
    response = "1"
    # response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = 12

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Test.objects.order_by('name')[0:2]

    # 数据排序
    # Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    # Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    # for var in list:
    #     response += var.name + "<br>"
    assert type(response3) == str or type(response3) == int, 'no str'
    print(response3)
    response3 = str(response3)
    return HttpResponse("<p>" + response3 + "</p>")


def testup(request, id):
    if id == False: return HttpResponse('没有传值')

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    try:
        test1 = Test.objects.filter(id=id)
        if test1.exists():
            # test1.name = 'Google'
            # test1.save()
            test1.update(name = 'Google');
        else:
            return HttpResponse('id=' + str(id) + '的数据不存在！')
    except Exception:
        return HttpResponse('出错了！')

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


def testdel(request, id):
    # id = request.GET['id']
    if id == False:
        return HttpResponse('没有传值')
    # 删除id=1的数据
    test1 = Test.objects.get(id=id)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")
