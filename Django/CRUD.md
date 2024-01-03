## 1. View 설계 (URL 구조 설계)

-   프로젝트의 URL 구조를 생각하고 전체 웹사이트의 틀 잡기
-   웹 사이트의 기능은 URL을 잘 정의하는 것에서 시작

''(root) -> 홈페이지  
/posts -> 전체 포스트 조회(Read)  
/posts/<post:id> -> 개별 포스트 조회(Read)  
/posts/new -> 포스트 작성(Create)  
/posts/<post:id>/edit -> 포스트 수정(Update)  
/posts/<post:id>/delete -> 포스트 삭제(Delete)

-   projectName/proejctName/urls.py
-   projectName/appName/urls.py  
    projectName/appName/views.py

## 2. Model 설계 (데이터 구조 설계)

title -> 글의 제목  
content -> 글의 내용  
dt_created -> 작성일  
dt_modified -> 마지막 수정일

-   projectName/appName/models.py
-   관리자 페이지에서 사용하기 위해서는 admin.py에 등록 필수  
    (projectRoot) $ python manage.py makemigrations  
    (projectRoot) $ python manage.py migrate
-   관리자 계정 생성  
    (projectRoot) $ python manage.py createsuperuser

## 3. Template 설계

-   projectName/appName/views.py
-   projectName/appName/templates/appName/htmlName.html  
    상속 관계 정리

#### linebreakbr

-   Django에서는 줄바꿈(Enter)이 \n으로 저장 -> HTML에서는 <br>태그로 줄 바꿈
-   본문에 있는 \n을 <br>태그로 변경하기 위해 Tempalte Filter인 linebreakbr 사용  
    {{post.content|linebreaksbr}}

#### 사이트 연결

-   url의 name 속성을 사용하면 하드코딩 하지 않고 경로를 잡을 수 있다.  
    path('posts/<int:post_id>', views.post_detail, name='post-detail')  
    <a href={% url 'post_list' %}>돌아가기</a>  
    <a href={% url 'post_detail' post.id %}>{{post.title}}</a>

#### 디자인

-   템플릿 태그 static을 이용해서 css파일과 연결

## 4. form 태그

-   labe : 입력창 앞에 단어
-   input : 입력 공간 (type 다양함)
-   name : 입력데이터의 key값, input에서 입력한 값이 value값
-   submit : input 내용을 form의 action에 보내는 버튼
-   value : submit 버튼위에 나올 단어
-   action : input 내용을 보낼 url
-   method : 보내는 방식

### 4-1. 글쓰기(Create)

-   projectName/appName/forms.py : 이곳에 form을 정의하고 템플릿과 뷰에서 가져다가 사용
<!-- 
from django import forms

class PostForm(forms.Form): # forms.CharField는 기본적으로 한 줄 입력을 위한 위젯을 가지고 있다.
title = forms.CharField(max_length=50, lable='제목') # 여러줄 입력을 위한 위젯으로 Textarea가 있다.
content = forms.CharField(label='내용', widget=forms.Textarea)
-->

-   urls에서 views를 호호출하게하고 views.py에서 함수 정의
<!-- 
from .forms import PostForm

def post_create(request):
post_form = PostForm()
return render(request, 'posts/post_form.html', {'form': post_form})
-->

-   projectName/appName/templates/appName/form.html  
    : view 까지 만들 었으니 이제 template을 만들면 된다.
    <!--
      {% comment %} action에 아무 url도 안적으면 현재 url, method는 get {% endcomment %}
      <form method="post">{% csrf_token %}
          {% comment %} .as_ul을 붙이면 ul태그처럼 보여준다. {% endcomment %}
          {{form.as_ul}}
          <input type="submit" value="전송">
      </form>
    -->

    -   as_ul : 리스트 형태로 form을 보여줌
    -   as_table : 표 형식으로 form을 보여줌
    -   as_p : p태그 처럼 form을 보여줌

-   projectName/appName/views.py : 서버에서 전달 받은 form logic 처리

#### Model Form (모델 기반으로 자동 form 생성 기능)

-   Form은 Model 기반으로 만드는 경우가 많다. (유저에게 데이터 입력받아 DB에 저장하는 기능이 많기 때문)
      <!-- 
      from django import forms
      from .models import Post
    
      class PostForm(forms.modelformset_factoryForm):
    
          class Meta:
              # 참조할 모델 명시
              model = Post
              # 참조할 필드 명시
              fields = ['title', 'content']
              # 모든 필드 참조하고 싶으면
              # fields = '__all__'
      -->

-   view도 이에 맞게 수정
<!--
def post_create(request):
   if request.method== 'POST':
       post_form = PostForm(request.POST)
       new_post = post_form.save()
 -->

### 4-2. 데이터 유효성 검사 (프론트와 백에서 모두 하는 것이 맞다.)

-   데이터가 우리가 원하는 규격에 맞는지 확인하는 과정
-   이름을 원하는데 숫자를 입력하거나. 필수 데이터 미입력, 들어가서는 안되는 특수문자가 입력되는지 확인
-   입력데이터가 유효하지 않을 때 다시 입력하게하거나 유효한 형식으로 만드는 과정을 고려해야함

#### (방법1) Field를 정의할 때 필수 옵션 인자로 주는 방법

-   데이터가 기본적인 유효성 검사를 요구할 때 사용
-   Model Field와 Form Field 2가지가 있는데 모델 폼을 사용하고 있으면 Moedl Field를 사용
-   projectName/appName/models.py : 각각의 필드마다 유효성 검증 추가
-   (장고에서 기본적으로 제공하는 옵션 인자 사용) :
    -   모든 항목은 빈칸없이 작성 : models.CharField(blank=False) / False가 default  
        null 옵션은 데이터에 빈 값을 null로 저장하는 것을 허용할지 결정하는 옵션  
        blank(폼에서 비어있는 값 허용 여부) / null(빈 값을 db에 null로 저장 허용 여부)
    -   제목은 50자 까지만 작성 : models.CharField(max_length=50)
    -   다른 제목과 중복 불가 : models.CharField(unique=True)
    -   내용은 10자 이상 작성 : models.TextField(min_length=10)
    -   내용에 '#'과 '@' 사용 불가 : models.TextField()
-   필드의 옵션인자를 통해 에러 메시지를 바꿀 수 있음
    -   models.CharFiled(unique=True, error_messages='중복된 제목입니다.')

#### (방법2) 따로 validator를 추가하는 방법

-   데이터가 보다 복잡한 유효성 검사를 요구할 때 사용
-   validaotor는 임의의 값을 받아서 내부의 기준을 충족하지 않으면 -> ValidationError 발생
-   vailidator는 하나의 필드에 종속되지 않고 여러 필드에 사용 가능
-   제공되는 Built_in Validator 사용 / User_custom Validator 사용

##### (방법2-1)Buind_in Validator

-   필요할때 검색해서 사용 : django-built_in validator 검색
-   최고 입력 10글자 이상
<!--
from django.core.validators import MinLengthValidator
models.TextField(validators=[적용할validator(, message='오류 메시지')])
 -->

##### (방법2-2)User_custom Validator

-   projectName/appName/validators.py : 직접 만들어서 사용
-   내용에 '#'과 '@' 사용 불가
<!-- 
projectName/appName/validators.py :
from django.core.exceptions import ValidationError
def validate_symbols(value):
    if ("@" in value) or ("#" in value):
        raise ValidationError("'@'와 '#'은 포함될 수 없습니다.", code='symbol-err')

projectName/appName/models.py :
form .validator import validate_symbols
models.TextField(validators=[validate_symbols])
-->

#### (방법3) Form에서 검증하는 방법

##### (방법3-1) 2-1과 2-2 그대로 사용가능

-   model에서 썻던 필드 옵션과 Validator들은 폼 필드에 에서도 그대로 사용 가능
-   ModelForm을 사용하는 경우 폼 필드가 없지만 일반 폼의 경우 각각의 폼 필드작성하고 옵션을 줄 수 있다.

##### (방법3-2) clean_data

-   class Meta 데이터 밑에 def clean_fieldName(self): 를 정의한다.
<!--
def clean_title(self):
    title = self.cleaned_data['title']
    if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
    return title
 -->

### 4-3. Form 디자인

-   장고에서 제공하는 것을 사용하지 않고 따로 디자인하면 유효성 검증에 대한 에러 처리 별도로 해줘야한다.
<!--
<h3>제목</h3>
<p>{{form.title}}</p>
{% for error in form.title.errors %}
    <p>{{error}}</p>
{% endfor %}
<h3>내용</h3>
<p>{{form.content}}</p>
{% for error in form.content.errors %}
    <p>{{error}}</p>
{% endfor %}
 -->

#### CSS 디자인 입히기1

-   projectName/appName/templates/appName/form.css :
<!--
.error {
    color : red;
} -->
-   css를 적용하기 위해선 HTML의 기본 구조를 잡아줘야한다.
-   base.html을 상속받아 css를 Link 태그로 연결
-   폼 영역도 base 태그 블럭안에 넣기
-   class 이름도 css에서 매칭되도록 태그에 적용하면 된다.

#### CSS 디자인 입히기2

-   장고 폼에서 자동으로 위젯 스타일을 지정하고 있으면 바로 id나 class를 적용할 수 없다.
-   projectName/appName/templates/appname/post_form.html 에서 바로 접근할 수 없고  
    projectName/appName/forms.py 에서 접근할 수있다.
-   post_form.html은 form.py를 참고하고 form.py는 ModelForm이어서 models.py를 참고하고 있다.  
    models.py에서 사용하는 CharFiled는 장고 공식문서에 따르면 TextInput 위젯을 사용한다.
-   forms.py의 Meta 클래스에 widgets 속성으로 접근
<!-- 
projectName/appName/forms.py 에서 
class Meta:
    model = Post
    fields = ['title', 'content']
    widgets = {'필드이름' : 적용할 위젯} / widgets = {'title': forms.TextInput(attrs={'class':'title'}) }

proejctName/appName/static/appName/form.css에서
.title {
width: 400px;
}
-->

### 4-4. 수정하기

-   urls 경로를 잡고, template에 버튼 만들어서 연결, 로직을 views에서 구현
-   수정하기니까 기존의 데이터 불러오고, 사용자의 입력도 받아야해서 from 태그에 넘겨줌
<!--
def post_update(request, post_id):
    # 수정하기니까 기존의 데이터를 먼저 가져와야한다
    post = Post.objects.get(id=post_id)

    # 저장하는 로직 create와 비슷

    # 글 수정도 사용자의 입력을 받는 것이니까 폼 사용
    post_form = PostForm(instance=post) #instance인자는 기존의 데이터 넣어주는 용도
    return render(request, 'posts/post_form.html', {"form":post_form})
 -->

### 4-5. 삭제하기

-   urls 경로를 잡고, template에 버튼 만들어서 연결, 로직을 views에서 구현
-   삭제할 글을 가져와서 삭제
<!--
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post-list')
 -->
-   삭제글은 한 번 더 물어봐주는 세심함이 필요

## 5. 다양한 상황 대처하기

#### 데이터 전부 삭제

python manage.py shell  
from posts.models import Post  
Post.objects.all().delete()

### 5-1. 아직 저장된 데이터가 없을 때

-   UX에 의하면 텅 비어있으면 불친절하게 느껴짐
-   글 작성을 독려하는 문구 넣어주면 더 좋음
-   post_list.html에 조건문을 넣어서 데이터가 없을때 조건문 발동
<!--
{% if posts %}
    {% comment %} 게시글이 있을 때 {% endcomment %}
{% else %}
    {% comment %} 게시글이 없을 때 {% endcomment %}
{% endif %}
 -->

### 5-2. 가져올 데이터가 존재하지 않을 때 (비정상 접속 오류처리 다 해줘야함)

-   try문 사용
<!--
from django.http import Http404
def post_update(request, post_id):
    try:
        # 수정하기니까 기존의 데이터를 먼저 가져와야한다
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404()
 -->
-   함수 사용 (더 간편)
<!--
from django.shortcuts import get_object_or_404
def post_update(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
 -->

### 5-3. 초기에 필요한 데이터가 있을 때

-   시딩(seeding)이란? : 사용할 데이터를 데이터베이스에 추가하는 것
-   테스트에 필요한 데이터 준비, 초기 데이터를 입력해야 하는 경우에 유용!
-   python manage.py loaddata seed_file : 명령어로 하나의 파일에 데이터 두고 심을 수 있음  
    seed_file은 JSON, XML 등이어야 한다.
-   JSON 구조를 파악하는 가장 쉬운 방법은 django로부터 데이터를 하나 받아보는 것이다.  
    (1) 데이터 입력해보고
    (2) python manage.py dumpdata posts --indent=2 > posts_data.json
    (3) JSON 파일이 하나 생김 그거 확인
-   데이터를 넣어보기
    (1) python manage.py loaddata posts_data.json

#### 더 많은 시드데이터가 필요할 때 (데이터는 형식이 있다.)

-   django-seed : 다양한 데이터 필드를 포함한 대량의 데이터를 생성해야할 때 유용한 패키지
-   pip install django-seed
-   porjectName/projectName/settings/INSTALLED_APPS에 django_seed 추가
-   python manage.py seed posts --number=갯수 ('psycopg2' 모듈이 깔려있어야한다.)  
    단점 : 유효성 검증은 거치지 않음, 까다로운 유효성을 요구하는 테스트 데이터는 별도로 관리해야한다.

### 5-4. 유효성 검증을 뒤늦게 추가했을 때 (이전 데이터를 다시 유효성 검증에 맞추는게 문제)

-   포인트는 기존 데이터의 유실을 최소화하면서 유효성을 맞추는 것이다.
-   validators.py와 같은 경로에 validate_data.py 생성
<!--

# 기존의 데이터를 새로 추가된 유효성에 맞춰주는 로직 작성

# 1. 모든 포스트 데이터 가져오기

from .models import Post

def validae_post():
posts= Post.ojbects.all()

    # 2. 각각의 포스트 데이터를 보면서 내용 안에 &가 있는지 체크(추가 유효성)
    for post in posts:
        if '&' in post.content:
            print(post.id, '번 글에 &가 있습니다.')
    # 3. 만약 '&'가 있다면 해당 '&'를 삭제 처리
            post.content = posts.content.repalce('&', '')
    # 4. 데이터 저장하기
            post.save

        # 시간 데이터 처리 (생성일 보다 수정일이 먼저라면)
        if post.dt_modified < post.dt_created:
            print(post.id, '번 글의 수정일이 생성일보다 과거입니다.')
            posts.save

-->

-   python manage.py shell  
    from posts.validate_data import validate_post  
    validate_post()

### 5-5. 한 페이지에 데이터가 너무 많을 때 (페이지 네이션)

-   python manage.py shell  
    from django.core.paginator import Paginator  
    from posts.models import Post  
    posts = Post.objects.all()  
    posts.count()
    <!-- 6개씩 잘라서 한 페이지 만들겠다는 의미 -->
    pages = Paginator(posts, 6)  
    pages.page_range
    <!-- 하나의 페이지 가져오기 -->
    page = pages.page(1)
    page.object_list
    <!-- 지금 페이지 다음에 페이지가 또 존재하는지 알고 싶다면 -->
    page.has_next()
    <!-- 이전페이지를 알고 싶다면 -->
    page.has_previous()
    <!-- 다음 페이지 번호 알고 싶을 때 -->
    page.next_page_number()

### 5-6. 페이지네이션 구현

-   views 먼저 수정
<!--
from django.core.paginator import Pagenator
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6) # 6개의 포스트 당 1페이지
    curr_page_number = request.GET.get('page')  # 쿼리스트링의 page라는 key의 value 받기
    if curr_page_number is None:
        # 처음 페이지에 접속한 경우 페이지 넘버는 1
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page':page})
 -->
-   template 수정 (post_list.html)
<!--
{% comment %} 각각의 페이지로 이동할 수 있게 하는 부분 {% endcomment %}
<div class="paginator">
    {% comment %} 이전페이지가 있다면 이전 버튼 활성화 {% endcomment %}
    {% if page.has_previous %}
        <a href="?page=1" class="first">first</a>
        <a href="?page={{ page.previous_page_number }}" class="prev">prev</a>
        {% comment %} 현재 몇번째 페이지에 있는지 표시 {% endcomment %}
    {% endif %}
        <span>
            <p>{{page.number}} of {{page.paginator.num_pages}}</p>
        </span>
    {% if page.has_next  %}
        <a href="?page={{page.next_page_number}}" class="next">next</a>
        <a href="?page={{page.paginator.num_pages}}" class="last">last</a>
    {% endif %}
</div>
 -->

## 6. 클래스형 뷰

-   위에서는 함수형 뷰에 대해서 다뤘다. 클래스는 함수와 달리 상속을 받을 수 있다.
-   장고는 개발자들이 자주 쓸만한 view를 클래스로 만들어 뒀다.
<!-- 
from django.views import View

# page_create를 class형 view로 만들기

class PostCreateView(View): # get 방식일 때
def get(self, request):
page_form = PostForm()
return render(request, 'posts/post_form.html', {'form':page_form}) # post 방식일 때
def post(self, request):
post_form = PostForm(request.POST)
if post_form.is_valid():
new_post = post_form.save()
return redirect('post-detail', post_id=new_post.id)
return render(request, 'posts/post_form.html', {'form': post_form})
-->

-   urls.py : class는 className.as_view()를 반드시 붙여야 한다.
<!--
urlpatterns = [
    path('posts/new', views.PostCreateView.as_view(), name='post-create'),
 -->

#### 제네릭 뷰

-   개발자들이 자주 쓸만한 view를 하나의 형태로 만들어 둔 것

### 6-1. Generic Create View (작성)

-   제네릭은 context 따로 지정하지 않아도 우리가 지정한 템플릿에 form을 form이라는 키워드로 템플릿에 전달한다.
<!-- 
from django.views.generic import CreateView
from django.urls import reverse

class PostCreateView(CreateView):
model = Post
form_class = PostForm
template_name = 'posts/post_form.html'

    def get_success_url(self) :
        return reverse('post-detail', kwargs={'posts_id':self.object.id})

-->

### 6-2. Generic List Class View (목록보기)

<!--
from django.views.generic import ListView
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    # 넘겨줄 데이터의 이름
    context_object_name = 'posts'
    # 정렬(-는 내림차순)
    ordering = ['-dt_created']
    # 페이지네이션
    paginate_by = 6
    # 현재 페이지를 어떤 값으로 조회하는 지 알 수 있음
    page_kwarg = 'page'
 -->

-   post_list.html
<!--
제네릭 뷰는 page가 아니라 page_obj로 템플릿에 데이터를 넘겨준다.
{% if page_obj.has_previous %} 이런식으로
 -->

### 6-4. Generic Detail Class View (상세보기)

<!--
from django.views.generic import DetailView
class PostDetailView(DeleteView):
    model = Post
    template_name = 'posts/posts_detail.html'
    # 특정 id에 해당하는 포스트를 보여주니까 id를 인자로 받는다.
    pk_url_kwarg = 'post_id'
    # 조회한 데이터 context로 넘겨줄 때 사용
    context_object_name = 'post'
 -->

### 6-5. Generic Update Class View (수정)

<!--
from django.views.generic import UpdateView
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'
    # 수정된 데이터의 유효성 검증이 성공하면 이동할 url 정의
    def get_success_url(self) :
        return reverse('post-detail', kwargs={'post_id': self.object.id})
 -->

### 6-6. Generic Delete Class View (삭제)

<!--
from django.views.generic import DeleteView
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'    # url에서 id 가져오기
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')
 -->

#### RedirectView

-   새로운 URL로 리다이렉트해주는 기능만 있는 뷰
<!--
class IndexRedirectView(RedirectView):
    # 리다이렉션할 urlname 적으면 된다.
    pattern_name = 'post-list'
 -->

### 6-7. 제네릭 뷰의 context

-   제네릭은 클래스 변수에 알맞은 값만 전달해주는 형태로 사용
-   context를 전달하는 부분이 따로 없다.
-   기본적으로 제네릭 CRUD 뷰들은 모델 데이터를 템플릿으로 전달한다.
-   제네릭은 각각의 뷰에서 다루는 데이터를 자동으로 템플릿에 전달한다.
-   그럼 템플릿에서는 같은 데이터를 전달 받은 키값으로 접근 가능
-   context_object_name을 따로 지정하지 않으면 아래 명시한 키로 전달한다.

#### ListView

-   목록을 보여줘야하니까 데이터 전체가 필요
-   데이터베이스에서 조회한 모든 데이터가
-   object_list, <모델명>\_list 두개의 키로 템플릿에 전달
-   그외 다양한 데이터 템플릿에 전달 (paginated_by를 명시한 경우)
    -   paginator : 장고에서 제공하는 Paginator 객체
    -   page_obj : Page 객체
    -   is_paginated : True
    -   Paginator가 활성화 되면 모든 데이터가 아닌 현재 페이지 데이터 목록만 전달

#### DetailView

-   하나의 데이터에 대한 조회
-   데이터베이스에서 조회한 하나의 데이터가
-   object, <모델명> 두개의 키로 템플릿에 전달

#### CreateView

-   새로운 데이터를 생성해서 템플릿으로 전달되는 모델 데이터가 없다.

#### UpdateView

-   DetailView 처럼 이미 존재하는 하나의 데이터를 다룬다.
-   데이터베이스에서 조회한 하나의 데이터가
-   object, <모델명> 두개의 키로 템플릿에 전달

#### DeleteView

-   DetailView 처럼 이미 존재하는 하나의 데이터를 다룬다.
-   데이터베이스에서 조회한 하나의 데이터가
-   object, <모델명> 두개의 키로 템플릿에 전달

### 6-8. 더 빠르게 더 간단하게

-   제네릭 뷰는 모델이나 템플릿 파일의 이름 등 다양한 클래스 변수를 정의하고 있다.
-   클래스 변수 중에는 정의해주지 않았을 때 자동으로 찾게되는 값이 있다. (defualt가 있다.)
-   default를 사용하도록 하면 코드가 더 간결해진다.
