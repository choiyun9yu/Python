from django.urls import path
# from .views import movie_list, actor_list, movie_detail, actor_detail, review_list, 
from .views import MovieList, ReviewList, MovieDetail, actor_list, actor_detail

urlpatterns = [
    # 작성된 뷰를 URL과 연결하려면 .as_view() 함수 사용
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('movies/<int:pk>/reviews', ReviewList.as_view()),
    path('actors', actor_list), 
    path('actors/<int:pk>', actor_detail),
]