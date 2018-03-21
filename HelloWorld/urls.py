"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import *
from django.urls import path
from . import view, testdb, search, search2
urlpatterns = [
    # path('', view.hello),  # 首页
    path('', view.scrape),  # 首页
    path('admin', admin.site.urls),  # django管理工具
    path('testdb', testdb.testdb),  # 添加数据
    path('test', testdb.testshow),  # 展示数据
    path('testup/<int:id>', testdb.testup),  # 修改数据
    path('testdel/<int:id>', testdb.testdel),  # 删除数据
    path('search_form', search.search_form),  # 表单搜索（显示）
    path('search', search.search),  # 表单（处理）
    path('search-post', search2.search_post)  # 表单（post提交）

]
