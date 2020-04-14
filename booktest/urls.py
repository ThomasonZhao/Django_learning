"""
@author: Thomason
@contact: ThomasonZhao@outlook.com 
@create: 2020/4/12 3:44 PM 
"""
from django.urls import path, include
from booktest import views

urlpatterns = [
    path('hog/', views.index)
]
