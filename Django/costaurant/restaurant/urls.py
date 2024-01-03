"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# URL의 경로 항목에 어떤 URL을 입력하든 가장 먼저 이 파일과 접촉한다.
# 

from django.contrib import admin
from django.urls import path, include

# 입력된 URL과 매칭이 되는 Pattern이 있는지 확인
urlpatterns = [ 
    # path('경로', 시키는 동작)
    # 주소/admin과 매칭이되면 admin.site.urls로 가라
    path('admin/', admin.site.urls),
    # 주소에 foods와 매칭이 되면 foods앱 안의 urls.py 파일을 살펴봐라
    # foods/ 이후를 처리해주기 위해서 foods.urls 파일에서 정의                 
    path('foods/', include('foods.urls')),   
    path('greetings/', include('greetings.urls')),
    path('menus/', include('menus.urls')),
]
