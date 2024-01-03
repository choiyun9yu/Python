# Django

## 1. IDE

-   python 3.7.7
-   Django 2.2(LTS, Long Term Support)
-   Vitual Environment : pyenv, pyenv-virtualenv

## 2. env

### 2-1. for Window

#### WSL install

    - install 후 ubuntu 앱 실행

#### pyenv install (with ubuntu)

    $ sudo apt-get update
    $ sudo apt-get install -y make build-essential \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev git python-pip sqlite3

    $ mkdir codeit-django
    $ cd codeit-django
    $ code .    // VScdoe 실행

    // WARNING: seems you still have not added 'pyenv' to the load path. 오류 나는 경우
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"

    $ curl https://pyenv.run | bash // pyenv 설치

    $ echo $SHELL   // bash shell인 경우 계속 진행

    $ sed -Ei -e '/^([^#]|$)/ {a \
    export PYENV_ROOT="$HOME/.pyenv"
    a \
    export PATH="$PYENV_ROOT/bin:$PATH"
    a \
    ' -e ':a' -e '$!{n;ba};}' ~/.profile

    $ echo 'eval "$(pyenv init --path)"' >>~/.profile
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

### 2-2. for macOS

#### Homeborew install

#### pyenv install

    > brew install pyenv
    > brew install pyenv-virtualenv

    > echo $SHELL   // zsh shell

    > echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    > echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    > echo 'eval "$(pyenv init --path)"' >> ~/.profile
    > echo 'if [ -n "$PS1" -a -n "$BASH_VERSION" ]; then source ~/.bashrc; fi' >> ~/.profile
    > echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    > echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    > echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
    > echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    > echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

    > pyenv --version

### 2-3. 공통 부분

#### python install

    > pyenv install --list
    > pyenv install 3.7.13
    > pyenv install 3.8.13
    > pyenv versions

#### 가상환경 생성

pyenv는 가상환경을 끄고 킬 필요 없이, 해당 디렉토리로 이동했을 때 자동으로 가상환경이 적용된다.

    > pyenv virtualenv 3.7.13 django-envs   // 가상환경 생성
    > pyenv uninstall [envName]             // 가상환경 생성
    > pyenv global 3.8.13                   // Global 설정
    > cd codeit-django
    > pyenv local django-envs               // Local 설정
    > cd ..

#### django 설치

    > pip3 install django==2.2
    > django-admin --version

#### VScode EXTENSIONS

-   Python
-   Django
-   vscode-icons
-   indent-rainbow
-   Bracket Pair Colorizer 2

## 3. 프로젝트 생성

    # 프로젝트 생성
    $ django-admin startproject [ projectName ]

    # 프로젝스 실행
    $ python mange.py runserver // 해당 프로젝트 디렉토리 안에서 실행

    # 실행 중지
    $ ctrl + C

    # 개발 서버(디버깅 모드, 기본 포트 8000)
    $ django-admin runserver {ip:port}
    $ python manage.py runserver {ip:port}

#### 프로젝트 표준 시간 설정

-   projectName/appName/settings.py  
    TIME_ZONE = 기준으로 삼을 시간대 설정하는 변수  
    'UTC'(국제표준), 'Asia/Seoul'(한국 시간)

#### 3-1. 프로젝트 구조

-   projectName : Project Root // 이름 바꿔도 괜찮다.
-   prjevtName/**manage.py** : Django 프로젝트 관리를 위한 명령어 지원, App 생성, 데이터베이스 관련 명령, 개발 서버 실행 등
-   projectName/**db.sqlite3** : 프로젝트에서 사용하는 데이터베이스 파일
-   projectName/**projectName** : Proeject App // 이름을 마음대로 바꾸면 안된다.
-   projectName/projectName/**\_\_init\_\_.py** : 디렉토리를 하나의 파이썬 패키지로 인식되게끔 하는 역할  
    (python 3.3 이상부터는 없어도 패키지로 인식하지만 하위 버전 호환을 위해 사용)
-   projectName/projectName/**settings.py** : 시간대 설정, 데이터페이스 설정, 여러 경로 설정 등 프로젝트의 전반적인 설정 담당
-   projectName/projectName/**urls.py** : 요청이 들어오면 url에 따라 어떤 처리를 할지 결정
-   projectName/projectName/**wsgi.py** : 위스키(WebServer Gateway Interface), 웹 서버와 장고가 소통하는데 필요한 일종의 프로토콜

### 3-2. 앱 생성

Project : 웹 서비스 전체  
App : 기능을 나타내는 단위(여러 프로젝트에 들어갈 수 있음, 재사용 가능)

    # 앱 생성
    $ python manage.py startapp [ appName ]

    # 앱 등록
    $ projectName/projectName/settings.py   // INSTALLED_APPS 리스트에 앱을 등록해야함.

#### Reusable App Guide

-   한 가지 앱은 한 가지 기능을 하고, 그 기능을 잘 수행해야 한다.
-   장고 개발자는 프로젝트를 많은 앱으로 구성하는 것을 두려워하면 안된다.
-   각각의 앱을 유연하게 작성해야 한다.
-   다른 사람에게 배포가 가능하도록 만들어야 한다.

### 3-3. 앱 구조

-   projectName/appName/\_\_init\_\_.py
-   projectName/appName/db.sqlite3
-   projectName/appName/manage.py
-   projectName/appName/**migrations** : 데이터베이스의 변경 사항 히스토리 누적
-   projectName/appName/**admin.py** : 앱을 django 관리자와 연동하기 위해 필요한 설정 파일
-   projectName/appName/**apps.py** : 앱에 대한 설정을 넣어두는 파일
-   projectName/appName/**models.py** : 앱에서 사용할 데이터 모델 정의, 데이터베이스 연동과 관련된 파일
-   projectName/appName/**views.py** : 앱의 메인 로직 처리와 관련된 파일
-   projectName/appName/**tests.py** : 테스트 코드 작성하는 곳

### 3-4. url연결

    # projectName/projectName/**urls.py**
    urlpatterns = [ path('경로/', 작업) ]

    # domain/foods/index/ 처럼 두겹인 경우 foods/를 먼저 매칭해서 이동시키고 index/를 처리
    path('foods/', include('foods.urls'))

### 3-5. MVT Architecture

-   **M**odel : 데이터 구조 생성, 데이터베이스와 소통 (CRUD)
-   **V**iew : 웹 사이트의 로직을 담당, Model과 Template 사이를 연결  
    들어온 요청을 Model과 소통해서 처리하고 그 값을 Tempate에게 전달
-   **T**emplate : 웹 사이트의 화면 구성 담당, 매번 바뀌는 동적인 화면을 구성(Template Language)

## 4. Template(view)

-   Template : 화면 구성을 담당하는 부분
-   appName/templates/appName/htmlName.html : AppDir 안에 template 파일들을 넣어줄 dir 생성
    (Djang HTML은 < DOCTYPE >이나 < HEAD >, < BODY >를 따로 정의하지 않아도 된다.)
-   def funcName(request):
    return render(request, 'foods/htmlName.html')

### 4-1. 템플릿 구조

-   appName/templates/appName, appName/static/appName 처럼 샌드위치 구조로 정리
-   템플릿은 샌드위치 구조가 아니면 app이 여러개 일 때, 경로가 꼬인다.  
    (settings.py의 INSTALLED_APPS 리스트의 순서대로 template을 찾기 때문에 다른 app의 template을 사용하는 불상사 발생)
-   정적파일은 배포시 한 곳으로 모으는데 그때 같음 이름의 파일이 있으면 충돌이 발생한다.

#### render 함수(html)

-   render( request, template_name, context=None, content_type=None, status=None, using=None )
-   필수 인자 : request, template_name
-   선택인자
    -   context : 템플릿에 추가할 값들이 들어 있는 사전형 인자로 기본값은 아무것도 없는 None
    -   content_type : 결과로 만들어 내는 문서의 유형을 말하며 기본값은 'text/html' 즉 HTML 웹 페이지
    -   status : 상태 코드(Status Code) 값이며 기본값은 200(성공)입니다. 상태 코드는 클라이언트의 요청이 성공적으로 처리되었는지에 대한 정보를 주는 코드
    -   using : 템플릿을 렌더하는 템플릿 엔진을 지정할 수 있는 인자, 원하는 경우 다른 템플릿 엔진을 사용하여 템플릿을 렌더링 가능

### 4-2. 정적 파일(css, js, font, img ...) 적용하기

-   정적 파일(static files) : 웹페이지를 렌더링하는 과정에서 필요한 추가적인 파일
-   appName/static/appName : 내부에 css, images, fonts 디렉토리 각각 생성
-   정적 파일들을 사용하도록 템플릿 수정
    -   appName/tempalte/appName/index.html : 맨 위에 {% load static %} <- 탬플릿 태그
    -   css, img, font들의 경로도 수정 : href={% static 'foods/css/style.css' %} <- 탬플릿 태그

#### Template Language

-   HTML 문서를 작성할 때 프로그래밍을 하듯 작성할 수 있게 해준다.

-   템플릿 변수 : 우리가 지정한 데이터로 변환  
    {{ 변수명 }}  
    템플릿이 렌더될 때 우리가 지정한 데이터로 변환, view에서 넘겨 받은 값으로 변환  
    {{ 변수명.속성 }} 형태의 점연산자 지원, 템플릿 변수 내부 속성에 접근할 때 사용

-   템플릿 필터 : 템플릿 변수를 특정 형식으로 변환
    {{ 변수명|filter:args }} : 필터 뒤 인자  
    {{ 변수명|default:"coffee" }} : 기본 값 설정  
    {{ 변수명|capfirst }} : 첫글자 대문자  
    {{ 변수명|upper }}, {{ 변수명|lower }} : 대소문자화  
    {{ 변수명|random }} : 반복 가능한 템플릿 변수에 대해 무작위로 하나를 추출해서 변환  
    {{ 변수명|ljust:"length" }}, {{ 변수명|rjust:"length" }} : 좌우 정렬

-   템플릿 태그 : 템플릿 작성에 로직을 사용
    {{% 태그 %}}, {{% 태그 %}}{{% end태그 %}}  
    반복 : {{% for %}} {{% endfor %}}  
    조건 : {{% if %}} {{% else %}} {{% endif %}}  
    상속 : {{% block %}} {{% endblock %}}, {{% extends %}}

-   템플릿 주석 : 템플릿 언어의 주석처리를 담당
    {{# 주석 #}}

#### 템플릿의 중복(상속)

템플릿의 반복적인 부분을 템플릿 상속을 통해 해결  
부모 템플릿에서 변경되는 부분(자식 템플릿이 코드를 넣어주는 부분)은 블록으로 지정

< div class="food-container" >
{% block food-container %}
...(디폴터 값을 넣어둘 수 있음)
{% endblock food-container %}
</ div >

변경되지 않는 부분은 그대로 남겨두면 된다.  
자식 템플릿에서는 !최상단 첫줄에 어떤 부모 템플릿을 상속 받을 것인지 명시

    {% extends './base.html' %}

채울 블럭 명시하고 안을 채우면 된다.  
 {% block food-container %}
...
{% endblock food-container %}

-   만약 자식 템플릿에서 구현하지 않으면 부모 템플릿에 있는 내용을 그대로 사용하게 된다.  
    (부모템플릿에서 디폴트 처럼 내용을 담아둘 수 있음)

### 4-3. 동적 웹 페이지(템플릿 수정 없이 자동으로 변하는 웹페이지)

-   view에서 로직을 담당, views.py 함수에서 구현
-   뷰에서 템플릿에 데이터 넘길때 render 함수의 세번째 파라미터로 전달 (!주의 dictionary 형태로)
-   템플릿에서는 {{ 변수명 }}으로 넘겨준 데이터 받는다.

### 4-4. Elegant URL (우아한 URL)

-   장점 : URL을 우리가 원하는 형태로 구성 직관적이고 알아보기 쉬운 구조

#### Dynamic URL, 동적 URL (상세페이지 구현)

-   urls.py에 경로를 잡아주고 -> views.py에서 함수 생성 -> template에서 a태그 같은 url 설정
-   그런데 이렇게 일일이 경로 잡고 함수 만들고 하면 복잡하다. url을 이쁘게 정리하는 방법이 있다.
-   일정한 패턴을 가지고 입력하게 되는 URL에 대해서 다이나믹 URL을 지원한다.
-   우아한 URL (< str:> 이부분이 동적으로 바뀌는 URL을 변수를 이용해 처리할 수 있게 해준다.)  
    path('menu/< str:food>', views.food_detail) -> menu/ 다음에 모든 URL을 문자열로 보고,  
    food에 담아서 food_detail 함수를 호출할 때 인수로 넣어준다. (< str:> 이외에도 < int:>, < slug:> 등이 있다.)
    view에서는 food에 담겨서 넘어오는 것을 받아줄 파라미터를 정의해야한다.

        def food_detail(request, food):
            context = dict()
            if food == 'chicken':
                context["name"] = "코딩에 빠진 닭"
                context["description"] = "주머니가 가벼운 당신의 마음까지 생각한 가격 !"
                context["price"] = 10000
                context["img_path"] = "foods/images/chicken.jpg"
            return render(request, 'foods/detail.html', context=context)

    장고 안에서는 temaplate tag를 중첩해서 사용할 수 없다. (템플릿 태그는 이중 불가!)  
    그래서 get_static_prefix 사용

        < img src={% get_static_prefix %}{{img_path}} >

## 5. 에러 페이지 처리

요청이 잘못되었는지 아닌지 상태코드를 통해 알 수 있음

-   100번대 : 요청을 받아서 작업을 진행하고 있음
-   200번대 : 요청에 대한 처리 결과가 정상
-   300번대 : 요청을 완료하기 위해 추가적인 동작이 필요하다(redirection), 304요청에 대한 변경사항 없음
-   400번대 : 클라이언트의 요청에 문제가 있음, 404 요청한 자원이 없음, 403 접근권한이 없음
-   500번대 : 서버가 요청을 처리하는 과정에서 문제 발생 (서버쪽 에러)

### 5-1. 404에러 처리

Http404 모듈 삽입하고, raise로 오류 발생(raise는 파이썬에서 에러를 강제로 발생시킬 때 사용)

from django.http import Http404
if .. :
정상처리
else :
raise Http404("이런 음식은 없다구요 !")

## 6. Model

-   데이터의 구조를 잡고 데이터베이스와 소통하는 역할
-   (데이터의 구조)우리가 저장할 데이터의 형태, 데이터 모델링
-   (데이터베이스)실제로 데이터를 저장하는 곳
-   (소통)ORM(Object-Relational Mapper)지원, python 코드로 DB와 소통

### 6-1. 데이터 모델링

-   appName/models.py : class objName(models.Model): 형태로 클래스와 필드 형태로 생성 (models.Model 상속 받아야한다.)
    -   models.CharField(max_length=None) : 제한된 길이의 문자열 필드
    -   models.IntegerFiled() : 정수 값을 위한 필드
    -   models.BooleanFiled() : 불린 값을 위한 필드
    -   models.DateFiled(auto_now=Flase, auto_now_add=False) : datetime.date 객체 형태로 표시되는 날짜 필드 (auto_now: true로 설정되면 객체가 변경될 때마다 필드값 지금으로 수정, 마지막 수정시간 / auto_now_add: 모델이 처음 생성될 때 한 번, 자동으로 필드 값을 지금으로 설정, 생성된 시간)
    -   mdoels.DateTimeField(auto_now=False, auto_now_add) : 파이썬의 datetime.datetime 객체 형태
    -   models.EmailFiled(max_length=254) : 문자열이 이용 가능한 이메일 주소인지 확인
    -   models.FileFiled(upload_to=None, max_length=100) : 파일 업로드를 위한 필드
    -   models.ImageField(upload_to=None, height_field=None, width_filed=None, max_length=100) : FileField에서 업로드된 파일이 정상적인 이미지 파일인지 확인하는 과저이 추가된 필드
-   그리고 모델이 바뀌었음을 장고에게 알려줘야한다.  
    루트 디렉토리에서 python manage.py makemigrations <- 마이그레이션 만들기  
    python manage.py migrate <- 마이그레이션 적용하기

#### 마이그레이션(migration)

-   Django의 데이터베이스 변경 사항에 대한 버전 컨트롤 시스템
-   변경 사항을 저장해둔 목록 (개발자가 모델을 생성하거나 변경했을 때 마이그레이션을 하나씩 만듬)
-   만든 마이그레이션을 실제 데이터베이스에 적용하는 것이 migrate 명령어
-   python manage.py showmigrations <- 마이그레이션 목록 보기
-   python manage.py sqlmigrate appName [마이그레이션 번호 0001 이렇게] <- 해당 마이그레이션 파일이 ORM을 통해 어떻게 sql로 변환되었는지 보기

### 6-2. 데이터 추가하기(Create)

-   python manage.py shell <- 장고 기능 사용할 수 있는 Shell(사용자의 명령어를 받아서 해석한 다음, 프로그램을 실행시켜주는 것) 환경

-   from appName.models import modelName <- 데이터 모델 불러오기
-   modelName.objects.create(fieldName=value)
-   exit() <- 종료

-   QuertSet : Django의 ORM을 통해서 데이터베이스와 소통할 때 발생하는 자료형으로 리스트와 매우 비슷

### 6-3 데이터 조회하기(Read)

-   from appName.models import modelName <- 데이터 모델 불러오기
-   modelName.objects.all() <- 현재 데이터베이스에 저장되어 있는 모든 메뉴 데이터 가져오기
-   modelName.objects.all().values() <- 안쪽 데이터 까지 모두 보기,
-   modelName.objects.all().values('filedName') <- 보고 싶은 필드만 조회 !주의 코테이션으로 감싸기
-   modelName.objects.order_by('fildName') <- 해당 필드 기준 오름차순 정렬 / '-fieldName'은 내림차순

-   [get(하나의 데이터 조회), filter(여러 데이터 조회)] + 조건키워드(fieldName**조건키워드 )  
    Menu.objects.filter(name**contains="코") <- name 필드 중 "코"를 포함하는 것 모두 조회  
    Menu.objects.filter(price\_\_range=(2000,10000))<- 범위 내의 자료 조회
-   get으로 조회하는데 조회 결과가 두개 이상이라면 에러 발생, 그래서 고유 식별자 조회시 사용

### 6-4. 데이터 수정하기(Update)

-   수정할 데이터를 먼저 가져와서 변수에 할당한 뒤 수정  
    data = Menu.objects.get(id=1) / data.query <- data가 쿼리문일 때 SQL문 보여줌
    data.name = "코빠닭"
-   수정한 후 데이터베이스에 반영  
    data.save()

### 6-5. 데이터 삭제하기(Delete)

삭제할 데이터를 먼저 가져와서 변수에 할당한 뒤 삭제  
 data = Menu.objects.get(id=3)
data.delete()

### 6-6. 관리자(Admin) 도구 사용하기

관리자 계정 생성하기 : 루트 디렉토리에서 python manage.py createsuperuser  
관라자 계정 로그인 : localhost:8000/admin으로 접속  
관리자 페이지에서 관리할 수 있도록 데이터 모델 추가  
appName/admin.py 안에서

    from foods.models import Menu
    admin.site.register(Menu)

### 6-7. Model 적용하기

view

    def index(request):
        context = dict()
        today = datetime.today().date()    # 날짜 데이터 생성하기 오늘 날짜 가져온다.
        print(today)    # print 값은 서버 console 창에 출력된다.(브라우저 콘솔 아님)
        context["date"] = today
        menus = Menu.objects.all()  # 모든 데이터 가져와서 menus 변수에 담기
        context["menus"] = menus
        return render(request, 'foods/index.html', context=context)

template

    {% extends './base.html' %}
    {% load static %}

    {% block date-block %}
    {% comment %} <div>12 Aug, 2020</div> {% endcomment %}
    <div>{{date}}</div>
    {% endblock date-block %}

    {% block food-container  %}

    {% for menu in menus %}
        <div class="food">
        <img src={% get_static_prefix %}{{menu.img_path}} 'foods/images/chicken.jpg' width="300px" height="200px"/>
        <div class="info">
            <h3>{{menu.name}}</h3>
            <P>{{menu.description}}</p>
            <a href="#">메뉴 보기</a>
        </div>
        </div>
    {% endfor %}

    {% endblock food-container  %}

## 7. 데이터베이스 셋업

### 7-1. DB 설치

#### WSL

    $ sudo apt update
    $ sudo apt install mysql-server

#### macOS

    $ brew update
    $ brew install mysql

### 7-2. DB접속

#### WSL

    $ sudo service mysql start
    $ sudo mysql
    $ sudo service mysql stop
    $ sudo service mysql restart

#### macOS

    $ brew services start mysql
    $ mysql -uroot
    $ brew services stop mysql      # 서버 종료
    $ brew services retsart mysql   # 서버 재시작

### 7-3. DB 생성

    SHOW databases; # 현재 데이터베이스 조회

    CREATE DATABASE dbname
    CHARACTER SET utf8mb4   # 한글이나 이모지를 데이터베이스에 저장하기 위함
    COLLATE utf8mb4_0900_ai_ci;

### 7-4. 유저 생성

    CREATE USER 'username'@'localhost' IDENTIFIED MY 'password';    # 생성
    GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';     # 권한부여
    quit

#### WSL

    mysql -uusername -ppassword

#### macOS

    sudo mysql -uusername -ppassword

### 7-5. 데이터베이스 사용

    USE dbname

## 8. 데이터베이스 연결

### 8-1. mysqlclient 설치

#### WSL

    sudo apt install python3-dev default-libmysqlclient-dev build-essential
    pip install mysqlclient # 위에 방법 설치 실패시 시도

#### macOS

    pip install mysqlclient

### 8-2. Django 프로젝트 settings.py 설정

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dbname',
            'HOST': 'localhost',
            'PORT': '3306',
            'USER': 'username',
            'PASSWORD': 'password',
        }
    }

### 8-3. 마이그레이션

    python manage.py migrate

-   마이그레이션 : 한종류의 데이터베이스에서 다른 종류의 데이터베이스로 데이터를 옮기는 것
