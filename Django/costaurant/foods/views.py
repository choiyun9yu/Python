from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from foods.models import Menu

# Create your views here.
# 쿼리는 request로 들어오는 듯
# def index(request):
#     return HttpResponse('''
#                         <h2>Hello, Django !</h2>
#                         <p>Just Codeit !</p>
#                         <p>Just Codeit !</p>
#                         <p>Just Codeit !</p>
#                         <p>Just Codeit !</p>
#                         <p>Just Codeit !</p>
#                         <p>Just Codeit !</p>
#                         ''')

# template으로 보여주기
# def index(request):
#     return render(request, 'foods/index.html')


def index(request):
    context = dict()
    today = datetime.today().date()    # 날짜 데이터 생성하기 오늘 날짜 가져온다.
    print(today)    # print 값은 서버 console 창에 출력된다.(브라우저 콘솔 아님)
    context["date"] = today
    menus = Menu.objects.all()  # 모든 데이터 가져와서 menus 변수에 담기
    context["menus"] = menus
    return render(request, 'foods/index.html', context=context)

# 상세페이지에 대한 함수
def chicken(requset):
    return render(requset, 'foods/chicken.html')

# # 우아한 URL 함수
# def food_detail(request, food):
#     context = dict()
#     if food == 'chicken':
#         context["name"] = "코딩에 빠진 닭"
#         context["description"] = "주머니가 가벼운 당신의 마음까지 생각한 가격 !"
#         context["price"] = 10000
#         context["img_path"] = "foods/images/chicken.jpg"
#     else : 
#         raise Http404("이런 음식은 없다구요 !") # raise는 파이썬에서 에러를 강제로 발생시킬 때 사용하는 문법
#     return render(request, 'foods/detail.html', context=context)

# pk를 id 값으로 사용해서 조회
def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request, 'foods/detail.html', context=context)