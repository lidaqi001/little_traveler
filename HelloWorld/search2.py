# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf

# 接收POST请求数据


def search_post(request):
    Yuan={1:2,2:3,3:4,4:5,6:6}
    print(request.COOKIES)
    # return HttpResponse()
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
