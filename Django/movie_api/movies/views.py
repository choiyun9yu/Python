from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer

# 페이지네이션을 위한 클래스
class MoviePageNumberPagination(PageNumberPagination):
        page_size = 2

class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination

# class MovieList(ListCreateAPIView):
#     queryset = Movie.objects.all() # 필수, GET 요청을 처리할 때 돌려줄 객체들을 지정
#     serializer_class = MovieSerializer  # 필수, 조회와 생성 시 사용할 시리얼라이저를 설정하는 옵션

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer
    # queryset 옵션 지정 X, GET 요청 처리할 때 돌려줄 객체
    # 특정 영화를 먼저 가져오고, 영화로 리뷰를 필터해야해서 queryset을 바로 설정할 수 없음
    
    # 그래서 get_queryset()함수를 사용해야함
    def get_queryset(self):
        # 이때 url로 받은 pk 값은 self.kwargs로 접근 가능
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    # 영화 id는 입력 데이터로 전달되지 않기 때문에 
    # 이 함수를 오버라이딩 하여 데이터 생성 시 movie 객체를 넣는다.
    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# class MovieList(APIView):
#     # APIView는 들어오는 요청을 함수로 구분하여 처리합니다.
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def review_list(request, pk):
#     movie = get_object_or_404(Movie, pk=pk) # Movie 모델에 pk와 일치하는 게 있는지 확인
#     if request.method == 'GET':
#         reviews = Review.objects.filter(movie=movie) # 특정 영화와 관련된 리뷰 받아오기
#         serializer = ReviewSerializer(reviews, many=True) # 직렬화 해서 보여주기
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data) # 요청값 직렬화해서
#         if serializer.is_valid():   # 요청값 유효성 검증
#             serializer.save(movie=movie)    # 저장(생성)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieDetail(APIView):
#     # 먼저 pk에 해당하는 특정 데이터 가져오기
#     def get_object(self, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie

#     # GET 요청 처리
#     def get(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     # PATCH 요청 처리
#     def patch(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE 요청 처리
#     def delete(self, request, pk):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     # 영화 목록 조회 요청이 들어온 경우
#     if request.method == 'GET': 
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # 영화 목록 생성 요청이 들어온 경우
#     elif request.method == 'POST':
#         data = request.data     # POST 요청으로 전달된 데이터에 접근 
#         serializer = MovieSerializer(data=data)
#         if serializer.is_valid():   # 유효성 검사 통과하면
#             serializer.save()       # 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk):
#     # get_object_or_404(조회할 모델, 조회할 pk)는 데이터가 존재하면 반환, 없으면 404에러 반환
#     movie = get_object_or_404(Movie, pk=pk)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()    
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # @은 데코레이터 함수이다. 이름 그대로 특정한 함수를 꾸미는 함수이다. 
# # 기존 함수를 수정하지 않고 추가 로직을 넣고 싶을 때 사용한다.
# @api_view(['GET']) # 함수형 뷰가 GET 메소드만 허용하는 API를 제공한다는 걸 표시
# def movie_list(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)   # many 옵션은 다수 데이터 로드
#     return Response(serializer.data, status=200)

# @api_view(['GET'])
# def actor_list(requset):
#     actors = Actor.objects.all()
#     serializer = ActorSerializer(actors, many=True)
#     return Response(serializer.data, status=200)

