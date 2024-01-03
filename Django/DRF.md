## 1. 환경 설정

    $ pyenv install 3.9.11                                   # 파이썬 3.9.11 버전 설치
    $ pyenv virtualenv 3.9.11 venv                           # venv라는 가상 환경 생성
    $ mkdir movie_api                                        # 프로젝트를 위한 디렉토리(폴더) 생성
    $ cd movie_api                                           # 디렉토리 안으로 이동
    $ pyenv local venv                                       # venv 가상 환경 적용
    $ pip install django==4.0 djangorestframework==3.13.1    # Django 4.0, DRF 3.13.1 설치
    $ django-admin startproject movie_api

-   DRF를 사용하기 위해 settings.py에 있는 INSTALLED_APPS에 rest_framework를 추가

    INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'rest_framework'
    ]

## 2. 모델 생성

    $ cd movie_api
    $ python manage.py startapp movies

새로 만든 앱 등록

    INSTALLED_APPS = [
        # ...
        'django.contrib.staticfiles',
        'rest_framework',
        'movies'
    ]

다음으로, 영화에 대한 기본 정보를 담을 수 있는 Movie 모델을 생성, Movie 모델에는 name(이름),  
opening_date(개봉일), running_time(상영 시간), overview(간략한 소개 문구) 필드가 존재  
**projectName/appName/models.py**

    from django.db import models

    class Movie(models.Model):
        name = models.CharField(max_length=30)
        opening_date = models.DateField()
        running_time = models.IntegerField()
        overview = models.TextField()

테스트 데이터 넣고(movies.json) 마이그레이션

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py loaddata movies.json


## 3. 데이터 조회

#### 직렬화(Serialize)

-   프론트엔드는 데이터를 백엔드에 요청하고 백엔드는 요청에 맞게 처리하여 데이터를 반환
-   이 과정에서 사용하는 데이터 형식이 서로 달라 문제 발생
-   직렬화는 서버에서 파이썬 객체로 저장된 데이터를 JSON 형태로 바꿔준다.
-   역직렬화는 JSON 형태의 데이터를 파이썬 객체로 바꿔준다.

### 영화 데이터 조회 요청(GET)을 처리하는 API

#### 3-1. 시리얼라이저(직렬화기)

조회를 위해 모델에서 필요한 필드 매칭

**projectName/appName/serializers.py** 데이터 조회 시리얼라이저

    from rest_framework import serializers
    from .models import Movie

    class MovieSerializer(serializers.Serializer):
        # 사용할 필드 이름은 꼭 모델에서 사용하는 필드 이름과 일치시켜야 한다.
        id = serializers.IntegerField()
        name = serializers.CharField()
        opening_date = serializers.DateField()
        running_time = serializers.IntegerField()
        overview = serializers.CharField()


#### 3-2. 모델과 뷰 연결

**projectName/appName/views.py**

    from rest_framework.decorators import api_view
    from rest_framework.response import Response

    from .models import Movie
    from .serializers import MovieSerializer

    @api_view(['GET']) # 함수형 뷰가 GET 메소드만 허용하는 API를 제공한다는 걸 표시
    def movie_list(request):
        movies = Movie.objects.all()                        # 모든 객체 load
        serializer = MovieSerializer(movies, many=True)     # 객체 to dictionary
        return Response(serializer.data, status=200)        # dictionary to JSON

@api_view([ 'GET' ])은 데코레이터 함수이다. 이름 그대로 특정한 함수를 꾸미는 함수이다.  
기존 함수를 수정하지 않고 추가 로직을 넣고 싶을 때 사용한다.

#### 3-3. URL 설정하고 확인하기

**proejctName/proejctName/urls.py**

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('movies.urls')),
    ]

**proejctName/appName/urls.py**

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('movies.urls')),
    ]

## 3. 데이터 생성

### 영화 데이터 생성 요청(POST)을 처리하는 API

#### 4-1. 시리얼라이저

생성을 위해 시리얼라이저에 create()함수 정의

**projectName/appName/serializers.py** 데이터 생성 시리얼라이저

    from rest_framework import serializers
    from .models import Movie

    class MovieSerializer(serializers.Serializer):
        # ...

        def create(self, validated_data):   # validated_data는 유효성 검사를 마친 데이터
            return Movie.objects.create(**validated_data)   # **는 언팩킹

#### 4-2. 뷰

**projectName/appName/views.py**

    from rest_framework import status   # 추가

    @api_view(['GET', 'POST'])
    def movie_list(request):
        # 영화 목록 조회 요청이 들어온 경우
        if request.method == 'GET':
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # 영화 목록 생성 요청이 들어온 경우
        elif request.method == 'POST':
            data = request.data     # POST 요청으로 전달된 데이터에 접근
            serializer = MovieSerializer(data=data)
            if serializer.is_valid():   # 유효성 검사 통과하면
                serializer.save()       # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## 5. 데이터 조회, 수정, 삭제

데이터를 수정하거나 삭제하려면 모든 데이터들 중 특정 데이터를 따로 지정할 수 있어야 한다.  
이를 위한 새로운 엔드 포인트를 만들어야 한다.  
엔드 포인트란? 서버의 리소스(데이터)에 접근하게 해주는 URL을 뜻한다.

#### 5-1. 엔드포인트 : API 생성시 엔드포인트는 서버 리소스에 접근하게 해주는 URL을 의미

> GET | /moives/:id | 특정한 영화 데이터 조회  
> PATHCH | /movies/:id | 특정한 영화 데이터 부분 수정  
> PUT | /movies/:id | 특정한 영화 데이터 수정  
> DELETE | /movies/:id | 특정한 영화 데이터 삭제

-   movies/:id로 특정한 영화를 선택하여 조회, 수정, 삭제 가능
-   PUT, PATCH 모두 데이터 수정시 사용, 하지만 데이터를 수정하는 방식에는 차이 존재
    -   PUT : 기존 데이터를 완전 새로운 데이터로 바꿈
    -   PATCH : 모델에 존재하는 일부 필드만 수정 가능

**projectName/appName/urls.py** urls.py 설계하기

    from django.urls import path
    from .views import movie_list, movie_detail

    urlpatterns = [
        path('movies', movie_list),
        path('movies/< int:pk >', movie_detail),
    ]

**projectName/appName/views.py** 엔드포인트 연결하기

    @api_view(['GET', 'PATCH', 'DELETE'])
    def movie_detail(request, pk):
        pass

#### 5-2. 시리얼라이저

수정과 삭제를 위해 update(), delete() 정의

**proejctName/appName/serializers.py** 데이터 수정 시리얼라이저 (삭제 시리얼라이저는 없음)

    from rest_framework import serializers
    from .models import Movie

    class MovieSerializer(serializers.Serializer):
        # ...

        def create(self, validated_data):
            #...

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.opening_date = validated_data.get('opening_date', instance.opening_date)
            instance.running_time = validated_data.get('running_time', instance.running_time)
            instance.overview = validated_data.get('overview', instance.overview)
            instance.save()
            return instance

-   validated_data는 유효성 검사 마친 데이터, instance는 수정할 데이터(변경할 모델의 객체 intance에 유효성 검사 마친 데이터 넣으면 수정)
-   주의! PATCH이기 때문에 수정 요청이 들어온 필드만 수정하고, 나머지는 기존 값 그대로 사용 하기 위해 get()함수 사용
-   get()은 파라미터로 Key와 기본값을 받는데 키에 맞는 데이터가 존재하면 데이터를 반환하고, 없으면 기본값을 반환

#### 5-3. 뷰

**projectName/appName/views.py** 데이터 조회, 수정, 삭제 뷰

    # ...
    from rest_framework.generics import get_object_or_404

    # ...

    @api_view(['GET', 'POST'])
    def movie_list(request):
        # ...

    @api_view(['GET', 'PATCH', 'DELETE'])
    def movie_detail(request, pk):
        # get_object_or_404(조회할 모델, 조회할 pk)는 데이터가 존재하면 반환, 없으면 404에러 반환
        movie = get_object_or_404(Movie, pk=pk)
        # 데이터 조회
        if request.method == 'GET':
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 데이터 수정
        elif request.method == 'PATCH':
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 데이터 삭제
        elif request.method == 'DELETE':
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

-   get_object_or_404(조회할 모델, 조회할 pk)는 데이터가 존재하면 반환, 없으면 404에러 반환, 이후 요청에 따라 처리
-   (GET) MovieSerializer에 키워드 없이 받아온 영화 객체(movie)를 넣음, 오직 하나의 영화 데이터를 조회하기 때문에 many 옵션은 사용X
-   (PATCH) MovieSerializer에 수정하려는 영화 객체(movie)를 넣고, 수정할 데이터 request.data를 data옵션에 넣음, 부분 수정이기 때문에 partial=True, 만약 PUT메소드로 모든 데이터 수정이면 이 옵션 사용X
-   (DELETE) 삭제 요청이 들어오면 movie.delete()로 삭제, 반환 코드 없으니 204반환

## 6. 시리얼라이저 필드 정리

### 6-1. Serializer 클래스 필드 종류

#### CharField : 문자열 데이터 받는 필드

모델의 CharField 혹은 TextField 받기 위해 사용  
Django의 CharField와 다르게 길이를 설정하는 옵션이 필수X

    # 구조 CharField(max_length=None, min_length=None, allow_blank=False)
    name = serializers.CharField()

#### IntegerField : 정수형 데이터를 받는 필드

모델의 IntegerField, SmallIntegerField 등 정수와 관련된 필드를 받기 위해 사용

    # 구조: IntegerField(max_value=None, min_value=None)
    running_time = serializers.IntegerField()

#### DateField : 날짜 데이터를 받는 필드

모델의 DateField를 받으려면 Serializer의 DateField를 사용  
DateField에는 날짜 데이터의 포맷을 지정하는 format 옵션이 존재  
지정해 주지 않으면 ISO-8601 포맷(2022-01-01)이 기본으로 적용

    # 구조: DateField(format=api_settings.DATE_FORMAT)
    opening_date = serializers.DateField()

    # 만약 다른 포맷(2022/01/01)으로 날짜를 나타내고 싶다면
    opening_date = serializers.DateField(format="%Y/%m/%d")

#### DateTimeField : 날짜와 시간이 모두 담긴 데이터를 받는 필드

모델의 DateTimeField를 받으려면 Serializer의 DateTimeField를 사용

    # 구조: DateTimeField(format=api_settings.DATETIME_FORMAT)
    created = serializers.DateTimeField()

[날짜시간 포맷 보러가기](https://www.w3schools.com/python/python_datetime.asp)

#### FileField&ImageField : 파일, 이미지 데이터 받는 필드

모델의 FileField와 ImageField를 받기 위해 사용  
use_url이 True면 파일의 경로가 URL 방식으로 나오고, False일 경우 파일의 경로만 나옴

    # 구조: FileField(max_length=None, allow_empty_file=False, use_url=True)
    file = serializers.FileField()

    # 구조: ImageField(max_length=None, allow_empty_file=False, use_url=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

#### SerializerMethodFiled

사용자가 정의한 함수를 통해 직렬화 과정에서 새로운 값을 생성할 수 있는 필드  
method*name 옵션은 함수의 이름을 설정, 설정하지 않으면 get*변수명으로 지정  
해당 필드를 사용하면 자신이 원하는 로직에 따라 새로운 변수를 생성 가능

    # 구조: SerializerMethodField(method_name=None)
    age = serializer.SerializerMethodField()

    # 만약 모델에 출생 정보가 존재하고, 이를 통해 새롭게 나이라는 값을 만들고 싶다면
    age = serializer.SerializerMethodField()
    def get_age(self, obj):
        return datetime.now().year - obj.birthday.year + 1

### 6-2. Serializer 옵션의 종류

필드에 상관없이 공통으로 사용할 수 있는 옵션

#### read_only

데이터를 직렬화 할 때 해당 필드를 사용하고, 역직렬화할 때는 사용하지 않을 때 True

#### write_only

read_only와 정 반대로 동작, 데이터 생성시 입력해야하지만 조회할 때는 보여주면 안되는 필드

#### required

필드를 필수적으로 입력해야 하는지 정의해주는 옵션으로 기본값은 True  
만약 입력하지 않으면 is_valid()를 실행할 때 에러 발생  
자동으로 데이터 생성일이 만들어지는 경우 False 옵션으로 에러 발생하지 않도록 처리

#### source

어떤 값을 참조할지 정의하는 옵션  
사용하는 필드명과 모델에서 사용하려는 필드명이 다를 경우 sorcue 옵션 사용

## 7. 모델 시리얼라이저

내부 Meta 클래스를 선언하고, 어떤 모델과 필드를 사용할지 정의하는 식으로 사용  
Django에서 ModelForm썻던 것 처럼, 훨씬 간단하게 시리얼라이저 정의 가능

    # Serializer 상속 받은 코드
    class MovieSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField()
        opening_date = serializers.DateField()
        running_time = serializers.IntegerField()
        overview = serializers.CharField()

        def create(self, validated_data):
            return Movie.objects.create(**validated_data)

        def update(self, instance, validated_data): # instance는 수정할 모델 객체 의미
            instance.name = validated_data.get('name', instance.name)
            instance.opening_date = validated_data.get('opening_date', instance.opening_date)
            instance.running_time = validated_data.get('running_time', instance.running_time)
            instance.overview = validated_data.get('overview', instance.overview)
            instance.save()
            return instance

    # ModelSerializer 상속 받은 코드
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

### Meta 클래스의 옵션들 정리

#### model : 어떤 모델로 시리얼라이저를 생성할지 지정해 주는 필수 옵션

#### fields : 어떤 필드를 사용할지 선언하는 옵션

fields를 **all**로 해주면 모델에 존재하는 모든 필드를 사용 가능

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

#### exclude : 모델을 기준으로 어떤 필드를 제외할지 명시

    # id, name, opening_date, running_time, overview 중에서 앞의 4개만 쓰고 싶을 때

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time']

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            exclude = ['overview']

#### read_only_fileds : 선택적으로 read_only추가하고 싶을때 read_only_fileds 사용

모델 시리얼라이저는 id 필드와 같이 데이터베이스에서 기본으로 생성되는 필드에 read_only 옵션 자동 추가

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
            read_only_fields = ['name']

#### extra_kwargs : 다양한 필드에 여러 옵션을 추가해야 할 경우 extra_kwargs를 사용

    # extra_kwargs를 사용한다면 간단하게 특정한 필드에 옵션을 추가할 수 있음.
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
            extra_kwargs = {
                'overview': {'write_only': True},
            }

#### 참고

read_only_fields나 extra_kwargs 같은 옵션을 사용하지 않고 필드를 직접 정의 가능

    class MovieSerializer(serializers.ModelSerializer):
        name = serializers.CharField(read_only=True)
        overview = serializers.CharField(write_only=True)

        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

## 8. 유효성 검사

데이터가 원하는 기준에 맞게 작성됐는지 확인하고, 잘못됐으면 오류를 반환해주는 과정  
시리얼라이저에 존재하는 모든 필드에는 validators 옵션을 사용 가능

### 8-1. validators 옵션

시리얼라이저에 존재하는 모든 필드에는 validators 옵션을 사용할 수 있다.  
보통은 유효성 검사 로직이 담긴 validator를 validators의 값으로 전달하는 식으로 사용  
이때 validator는 DRF와 Django에서 제공하는 것들 모두 사용 가능

#### 길이 제한 유효성 검사

    from django.core.validators import MaxLengthValidator, MinLengthValidator

    # ...

    class MovieSerializer(serializers.ModelSerializer):
        # ...
        overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])

#### 길이 제한 유효성 검사2

    # 유효성 검사 함수를 직접 만들어서 사용
    def overview_validator(value):
        if value > 300:
            raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
        elif value < 10:
            raise ValidationError('소개 문구는 최소 10자 이상으로 작성해야 합니다.')
        return value

    # ...

    class MovieSerializer(serializers.ModelSerializer):
        overview = serializers.CharField(validators=[overview_validator])
        # ...

#### 유일성 여부 확인

    # ...
    from rest_framework.validators import UniqueValidator

    class MovieSerializer(serializers.ModelSerializer):
        name = serializers.CharField(validators=[UniqueValidator(
            queryset=Movie.objects.all(),
            message='이미 존재하는 영화 이름입니다.',
        )])

        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

UniqueValidator() 에서 사용된 2개의 파라미터  
queryset은 유일성을 확인하기 위해 조회할 데이터를 적는 필수 옵션  
message는 이미 값이 존재할 때 보여줄 에러메시지 작성 옵션

    # UniqueTogetherValidator()는 두 개 이상의 필드에서 값이 유일한지 확인
    # 아래는 영화의 이름이 같더라도 소개 문구가 같지 않으면 데이터를 생성할 수 있도록 한 코드

    from rest_framework.validators import UniqueTogetherValidator

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
            validators = [
                UniqueTogetherValidator(
                    queryset=Movie.objects.all(),
                    fields=['name', 'overview'],
                )
            ]

UniqueTogetherValidator()는 두 개 이상의 필드를 검사하기 때문에 특정 필드의 validators 옵션에 사용할 수 없고 Meta 속성에 추가해야함  
fields는 queryset에서 조회한 데이터 중 어떤 필드들을 기준으로 유일성 검사를 할지 정의하는 필수 옵션  
하나의 필드는 중복이더라도 다른 필드가 다르면 생성가능하게 하는 함수

### 8-2. validate() 함수

#### validate\_필드명() 함수 : 하나의 필드에 대해서만 유효성 검사 진행하고 싶을 때 사용

    from rest_framework.serializers import ValidationError

    class MovieSerializer(serializers.ModelSerializer):
        # ...

        def validate_overview(self, value):
            if 10 <= len(value) and len(value) <= 300:
                return value
            raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')

#### validate() 함수 : 두 개 이상 필드의 유효성 검사를 한꺼번에 하고 싶을 때 사용

    from rest_framework.serializers import ValidationError

    class MovieSerializer(serializers.ModelSerializer):
    # ...

    def validate(self, attrs):
        if 10 > len(attrs['overview']) or len(attrs['overview']) > 300:
            raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
        if len(attrs['name']) > 50:
            raise ValidationError('영화 이름은 50자 이하로 작성해주세요.')
        return attrs

## 9. 직렬화 하기

**projectName/appName/models.py**

    class Movie(models.Model):
        name = models.CharField(max_length=30)
        opening_date = models.DateField()
        running_time = models.IntegerField()
        overview = models.TextField()

    class Review(models.Model):
        # Moive 모델 참조를 위해 ForeignKey 필드 사용
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
        username = models.CharField(max_length=30)
        star = models.IntegerField()
        comment = models.CharField(max_length=100)
        created = models.DateTimeField(auto_now_add=True)

    $ python manage.py makemigrations
    $ python manage.py migrate

### 9-1. 관계 직렬화하기

ForeignKey 필드 직렬화

**projectName/appName/serializers.py** # ...
from .models import Movie, Review # ...

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
            extra_kwargs = {
                'movie': {'read_only': True},
            }

기본적으로 movie와 같이 관계를 표현하는 필드를 직렬화 할 때는 pk, 즉 id 값이 사용  
그리고 extra_kwargs 옵션을 사용하여 movie 필드를 'read_only': True로 설정  
이는 리뷰를 생성할 때는 영화 정보(id)를 입력받지 않고 URL로 받아올 것이기 때문

**projectName/appName/urls.py**

    from .views import movie_list, movie_detail, review_list

    urlpatterns = [
        # ...
        path('movies/<int:pk>/reviews', review_list),
    ]

**projectName/appName/views.py**

    from .models import Movie, Review
    from .serializers import MovieSerializer, ReviewSerializer
    # ...

    @api_view(['GET', 'POST'])
    def review_list(request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        if request.method == 'GET':
            reviews = Review.objects.filter(movie=movie)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### 9-2. 역관계 직렬화하기

Review 모델에서 ForeignKey로 Movie 모델 참조하는 것이 관계 직렬화라면,  
Movie 모델에서 Review 모델을 참조하는 것을 역관계  
ForeignKey, ManyToManyField, OneToOneField 등 관계를 표현하는 필드에 참조되는 모델에는 이런 역관계가 존재

**예시**
Movie와 Review의 관계는 1:N 관계이기 때문에, 특정한 Movie 객체를 참조하는 Review 정보들은 review_set에 담겨있다. (역관계 이름은 [역관계를 가지는 모델명]\_set 형태로 사용)

    # 1(Movie):N(Review) 관계를 가지는 모델
    class Movie(models.Model):
        pass

    class Review(models.Model):
        movie = models.ForeignKey(Movie)

    # 1번 영화의 리뷰들을 조회하는 방법(역관계를 사용하는 경우)
    movie = Movie.objects.get(pk=1)
    reviews = movie.review_set.all()
        # Movie와 Review의 관계는 1:N 관계이기 때문에,
        # 특정한 Movie 객체를 참조하는 Review 정보들은 review_set에 담겨있다.

**projectName/appName/serializers.py**

    # MovieSerializer는 자동으로 필드를 정의해 주는 ModelSerializer를 사용하기 때문에,
    # fields에 review_set을 추가해 주면 역관계 필드를 쉽게 사용 가능
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'review_set', 'opening_date', 'running_time', 'overview']
            read_only_fields = ['review_set']

review_set 필드는 영화에 속하는 리뷰 정보들을 생성할 수도 있다.  
그러나 데이터 생성(POST) 시 영화에 속하는 리뷰를 함께 생성하는 것은 API 기획 의도와 맞지 않다.  
때문에 review_set 필드에 read_only 옵션을 추가해준다.

**proejctName/appName/models.py**
역관계 이름을 바꾸면 그 이름을 그대로 fields에서 사용할 수 있다.  
역관계 이름을 바꾸기 위해선 ForeignKey 필드에 related_name 옵션을 사용하면 된다.

    class Review(models.Model):
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

**projectName/appName/serializers.py**

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']
            read_only_fields = ['reviews']

### 9-3. 다양한 관계 직렬화하기 (pk 사용하지 않고, 관계필드 직렬화)

#### StringRelatedField

Django 모델에는 모델 객체를 문자열로 나타낼 때 사용할 **str**() 함수를 정의할 수 있다.  
**projectName/appName/models.py**

    class Review(models.Model):
        # ...

        def __str__(self):
            return self.comment

그리고 이때 사용하는 필드가 StringRelatedFiled이다.  
**projectName/appName/serializers.py**

    # MovieSerializer에 Review 정보 추가
    class MovieSerializer(serializers.ModelSerializer):
        # reviews의 타입을 StringRelatedField로 설정
        reviews = serializers.StringRelatedField(many=True)

        class Meta:
            model = Movie
            fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']

반대로 리뷰 데이터 조회 시 Movie에 대한 정보를 추가
**projectName/appName/models.py**

    class Movie(models.Model):
        # ...

        def __str__(self):
            return self.name  # 영화 객체 출력 시 이름이 나온다.

다음으로, ReviewSerializer의 movie 필드를 StringRelatedField 필드로 수정
**projectName/appName/serializers.py**

    # ReviewSerializer에 Movie 정보 추가
    class ReviewSerializer(serializers.ModelSerializer):
        movie = serializers.StringRelatedField()

        class Meta:
            model = Review
            fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
            # 기존에 pk 값이 나오던 movie 필드가 영화 이름으로 수정

#### Nested Serializer

관련된 객체의 보든 정보(필드)를 직렬화 하고 싶을 때 사용  
Nested Serializer는 일반적으로 데이터 생성 시에는 사용하지 않고, 데이터 조회 시에만 사용  
기존에 MovieSerializer에서 단순히 reviews에 대한 pk 값들이나 문자열들이 출력되었던 것과 다르게 ReviewSerializer에 존재하는 모든 필드가 출력

**projectName/appName/serializers.py**

    # MovieSerializer에 Review 정보 추가
    class MovieSerializer(serializers.ModelSerializer):
        # !주의 MovieSerializer 선언 전에 ReviewSerializer가 선언되어야함.
        reviews = ReviewSerializer(many=True, read_only=True)

        class Meta:
            model = Movie
            fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']

**projectName/appName/serializers.py**

    # ReviewSerializer에 Movie 정보 추가
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']
            read_only_fields = ['reviews']

    class ReviewSerializer(serializers.ModelSerializer):
        # !주의 ReviewSerializer 선언 전에 MovieSerializer가 선언되어야함.
        movie = MovieSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ['id', 'movie', 'username', 'star', 'comment', 'created']

## 10. Request와 Response

@api_view()는 Django 기반의 함수형 뷰를 DRF 기반의 함수형 뷰로 변경하는 데코레이터 함수  
대표적으로 HttpRequest 대신 Request를, HttpResponse 대신 Response를 사용하게 해준다.

### 10-1. POST 요청 처리과정에서의 Request

-   DRF에서 POST 요청은 Request 객체에 담겨서 전달 된다.
-   그 과정에서 JSON 형식으로 들어온 데이터를 파싱해서 파이썬 딕셔너리 형태로 변환한다.  
    ('파싱'이란 데이터를 추출하여 가공하기 쉬운 상태로 바꾸는 것을 의미)
-   파이썬 딕셔너리로 변환된 데이터는 시리얼라이저를 통해 파이썬 객체 형태로 변경된다.
-   시리얼라이저가 JSON 데이터를 바로 파이썬 객체로 바꾸는 게 아니라,  
    중간에 Request를 통해 먼저 JSON 데이터를 파이썬 딕셔너리로 바꿔 주는 과정이 있는 것이다.

### 10-2. GET 요청 처리과정에서의 Response

-   DRF에서 GET 요청이 들어오면 조회한 결과값은 serializer라는 변수에 담긴다.
-   시리얼 라이저는 파이썬 객체 형태로 저장된 데이터를 파이썬 딕셔너리 형태로 바꿔준다.
-   그리고 Response가 딕셔너리 형태를 JSON 형태로 다시 변환한다.

## 11. APIView(클래스형 뷰)

-   함수형 뷰 : 읽기 쉬움 / 확장, 재사용 어려움
-   클래스형 뷰 : 확장, 재사용 쉬움 / 읽기 어려움
-   제네릭 뷰 :

### 11-1. 클래스형 뷰 : 데이터 조회 생성

**projectName/appName/views.py**

    from rest_framework.views import APIView
    # ...

    class MovieList(APIView):
        # APIView는 들어오는 요청을 함수로 구분하여 처리합니다.
        def get(self, request):
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

**projectName/appName/urls.py**

    from .views import MovieList

    urlpatterns = [
        # 작성된 뷰를 URL과 연결하려면 .as_view() 함수 사용
        path('movies', MovieList.as_view()),
    ]

### 11-2. 클래스형 뷰 : 데이터 조회 수정 삭제

**projectName/appName/views.py**

    class MovieDetail(APIView):
        # 먼저 pk에 해당하는 특정 데이터 가져오기
        def get_object(self, pk):
            movie = get_object_or_404(Movie, pk=pk)
            return movie

        # GET 요청 처리
        def get(self, request, pk):
            movie = self.get_object(pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

        # PATCH 요청 처리
        def patch(self, request, pk):
            movie = self.get_object(pk)
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE 요청 처리
        def delete(self, request, pk):
            movie = self.get_object(pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

**projectName/appName/urls.py**

    from .views import MovieList, MovieDetail

    urlpatterns = [
        ...,
        path('movies/<int:pk>', MovieDetail.as_view()),
    ]

### 11-3. 제네릭 뷰 : 데이터 조회 생성

#### ListCreateAPIView : 데이터 조회와 생성을 위한 제네릭 뷰

GET 요청이 들어오면 모델에 존재하는 모든 데이터 조회  
POST 요청이 들어오면 ㄷ모델에 새로운 데이터 생성

**projectName/appName/views.py**

    from rest_framework.generics import ListCreateAPIView
    # ...

    class MovieList(ListCreateAPIView):
        queryset = Movie.objects.all() # 필수, GET 요청을 처리할 때 돌려줄 객체들을 지정
        serializer_class = MovieSerializer  # 필수, 조회와 생성 시 사용할 시리얼라이저를 설정하는 옵션

    # 관계 직렬화 맺은 ReviewList도 제네릭으로 변환
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

**projectName/appName/urls.py**

    from .views import MovieList, ReviewList
    # ...

    urlpatterns = [
        path('movies', MovieList.as_view()),
        path('movies/<int:pk>/reviews', ReviewList.as_view()),
        # ...
    ]

### 11-4. 제네릭 뷰 : 데이터 수정 삭제

#### RetrieveUpdateDestroyAPIView : 특정한 데이터를 조회·수정·삭제할 수 있는 제네릭 뷰

**projectName/appName/views.py**

    from rest_framework.generics import RetrieveUpdateDestroyAPIView
    # ...

    class MovieDetail(RetrieveUpdateDestroyAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer

## 12. 페이지네이션

많은 데이터가 저장된 모델을 한 번에 전부 조회하면 시간이 오래 걸린다.  
한 번에 조회할 데이터 개수를 정하고, 사용자가 더 많은 데이터를 요청하면 추가로 조회하는게 효율적이다.

#### 제네릭 뷰를 사용한 전역 페이지네이션 설정

전역 페이지네이션은 '앞으로 호출할 모든 API에서 결과의 개수를 조절하겠다'라는 의미

**proejctName/projectName/settings.py**

    REST_FRAMEWORK = {
        # 페이지네이션 의미
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 3, # 프로젝트에 존재하는 모든 API는 한번 요청할 때 최대 3개 반환
    }

위와 같이 페이지네이션 기능을 추가하면 API 요청에 따른 결과물이 다음과 같은 변수들로 반환됩니다.

-   count: 해당 API에 존재하는 실제 데이터의 개수
-   next: 데이터의 개수가 최대 결과물 개수보다 클 경우 다음 데이터의 URL (없으면 null)
-   previous: 현재 요청한 데이터 이전의 데이터가 존재하는 경우 이전 데이터의 URL (없으면 null)
-   results: 요청한 데이터를 페이지네이션한 결과

#### 제네릭 뷰를 사용한 개별 페이지네이션 설정

특정한 뷰에 조회 갯수 다르게 설정하고 싶은 경우 사용

**proejctName/appName/views.py**

    from rest_framework.pagination import PageNumberPagination
    #...

    class MoviePageNumberPagination(PageNumberPagination):
        page_size = 2

## 13. CORS 에러 처리

#### CORS(Cross-Origin Resource Sharing, 교차 출처 리소스 공유)란?

-   서로 다른 출처에서 리소스를 공유하는 것 (출처는 프로토콜+호스트+포트 부분)
-   CORS는 출처가 다른 자원들을 공유한다는 뜻으로 한 출처에 있는 자원에서 다른 출처에 있느 자원에 접근하도록 하는 개념
-   그런데 CORS를 위해서는 별도의 설정이 필요하다. 필요한 설정을 하지 않은 채 서로 다른 출처에서 리소스를 공유하려고 하면 에러가 발생할 수 있다.
-   예를 들어 그동안 백엔드 개발하며 사용했던 URL 출처는 http://localhost:8000/이었다. 그런데 프론트엔드의 출처는 일반적으로 http://localhost:3000/이 많이 사용된다. 이렇게 서로의 출처에 차이가 있지만 별도의 설정을 하지 않았기 때문에, 백엔드와 프론트엔드를 바로 연결하려고하면 문제가 생기는 에러를 CORS 에러라고 한다.

#### DRF에서 CORS 처리하기

    $ pip install django-cors-headers

**projectName/projectName/settings.py**

    INSTALLED_APPS = [
        ...,
        'corsheaders',
    ]

    MIDDLEWARE = [
        # 최상단에 작성
        'corsheaders.middleware.CorsMiddleware',
            ...,
    ]

    CORS_ALLOWED_ORIGINS = [
        'http://localhost:3000',
    ]

CORS_ALLOWED_ORIGINS 목록에 API 요청을 허용하고 싶은 출처(예를 들어 http://localhost:3000)를 입력하면 된다.
