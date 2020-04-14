"""
@author: Thomason
@contact: ThomasonZhao@outlook.com 
@create: 2020/4/12 3:44 PM 
"""
from django.urls import path, include, re_path
from booktest import views

urlpatterns = [
    path('', views.index),
    re_path('^(\d+)/$', views.detail),
]
