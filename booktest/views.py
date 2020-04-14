from django.shortcuts import render
from django.http import HttpResponse
from booktest import models


# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    # return render(request, 'booktest/index.html')
    list = models.BookInfo.objects.all()
    context = {'booklist': list}
    return render(request, 'booktest/index2.html', context)
