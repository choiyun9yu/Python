from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [ 
    # foods/index를 입렵받아 foods/와 매칭이되어서 이곳에서 index/처리
    # foods 앱 안의 views 모듈에서 index 함수 가져오기
    path('menu/', views.index),
    
    # 상세 페이지에 대한 URL
    # path('chicken/', views.chicken),
    
    # # 우아한 URL (<str:> 이부분이 동적으로 바뀌는 URL을 변수를 이용해 처리할 수 있게 해준다.)
    # path('menu/<str:food>', views.food_detail) 

    # 숫자로 받아서 foods/menu/다음에 숫자가 오면 그 값을 pk 변수로 받아서 디테일 뷰 호출
    path('menu/<int:pk>', views.food_detail)
]