from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return render(requset, 'menus/index.html')

def detail(request, menu):
    context = dict()
    if menu == 'chicken':
        context["name"] = '코딩에 빠진 닭 ' 
        context["description"] = '지금까지 이런 맛은 엇었다. 이것은 갈비인가 통닭인가'
        context["price"] = '20,000'
        context["img_path"] = 'menus/images/logo-gray.svg'
    return render(request, 'menus/detail.html', context=context)