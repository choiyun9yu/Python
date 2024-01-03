from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.http import Http404
# from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm

class IndexRedirectView(RedirectView):
    # 리다이렉션할 urlname 적으면 된다.
    pattern_name = 'post-list'

class PostListView(ListView):
    model = Post                                # default : 없음
    ordering = ['-dt_created']                  # default : 없음
    paginate_by = 6                             # default : 없음
    # context_object_name = 'posts'             # default : oject_list, <modelName>_list
    # template_name = 'posts/post_list.html'    # default : <modelName>_list가 기본값
    # page_kwarg = 'page'                       # default : 'page'

class PostDetailView(DetailView):
    model = Post                                # default : 없음
    # template_name = 'posts/posts_detail.html' # default : <modelName>_list가 기본값
    # pk_url_kwarg = 'post_id'                  # default : 'pk'
    # context_object_name = 'post'              # default : oject, <modelName>

class PostCreateView(CreateView):
    # form으로 템플릿에 컨텍스 전달                     
    form_class = PostForm                       # default : 없음
    model = Post                                # default : 없음                   
    # template_name = 'posts/post_form.html'    # default : <modelName>_list가 기본값
    def get_success_url(self) :
        return reverse('post-detail', kwargs={'pk':self.object.id})
            # reverse = url네임을 이용해서 타고올라간다.
            # kwargs = 키워드릴 이용해서 인자를 전달할 때 사용
    
class PostUpdateView(UpdateView):
    model = Post                                # default : 없음
    form_class = PostForm                       # default : 없음
    # template_name = 'posts/posts_detail.html' # default : <modelName>_list가 기본값
    # pk_url_kwarg = 'post_id'                  # default : 'pk'
    # 수정된 데이터의 유효성 검증이 성공하면 이동할 url 정의
    def get_success_url(self) :
        return reverse('post-detail', kwargs={'pk': self.object.id})
    
class PostDeleteView(DeleteView):
    model = Post                                # default : 없음
    # template_name = 'posts/posts_detail.html' # default : <modelName>_list가 기본값
    # pk_url_kwarg = 'post_id'                  # default : 'pk'
    # context_object_name = 'post'              # default : oject, <modelName>
    def get_success_url(self):
        return reverse('post-list')


# def index(request):
#     return redirect('post-list')

# # 페이지네이터 적용
# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6) # 6개의 포스트 당 1페이지
#     curr_page_number = request.GET.get('page')  # 쿼리스트링의 page라는 key의 value 받기
#     if curr_page_number is None:
#         # 처음 페이지에 접속한 경우 페이지 넘버는 1
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page':page})

# def post_list(request):
#     posts = Post.objects.all()
#     context = {"posts" : posts}
#     return render(request, 'posts/post_list.html', context)

# def post_detail(request, post_id):
#     posts = get_object_or_404(Post, id=post_id)
#     context = {"post" : posts}
#     return render(request, 'posts/posts_detail.html', context)

# # page_create를 class형 view로 만들기
# class PostCreateView(View):
#     # get 방식일 때
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form':post_form})
#     # post 방식일 때 
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#         return render(request, 'posts/post_form.html', {'form': post_form})

# def post_create(request):
#     if request.method== 'POST':
#         # 유저가 요청한 POST를 바로 PostForm으로 바인딩
#         post_form = PostForm(request.POST)
#         # 데이터 유효성 검증 하는 함수 is_valid
#         if  post_form.is_valid():        
#             # 바인딩된 데이터 저장 
#             new_post = post_form.save()
#             # 저장된 내용을 보기위해 리다이렉트, redirect('이동할url or urlname', 넘길 인자)
#             return redirect('post-detail', post_id=new_post.id)
#         # 데이터가 유효하지 않은 경우
#         else : 
#             # post_form = PostForm()를 넣으면 유효하지 않는 경우 처음부터 다시 입력
#             return render(request, 'posts/post_form.html', {'form': post_form})
#     else : # GET 방식으로 들어왔을 때, 서버에 요청하기전, Form을 달라
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
    
# def post_create(request):
#     if request.method== 'POST':
#         # POST 요청에서 값을 받아와서
#         title = request.POST['title']
#         content = request.POST['content']
#         new_post = Post(
#             title = title,
#             content = content,
#         )
#         new_post.save() # 저장하고
#         # 저장된 내용을 보기위해 리다이렉트, redirect('이동할url or urlname', 넘길 인자)
#         return redirect('post-detail', post_id=new_post.id)
#     else : # GET 방식으로 들어왔을 때, 서버에 요청하기전, Form을 달라
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
    
# def post_update(request, post_id):
#     try: 
#         # 수정하기니까 기존의 데이터를 먼저 가져와야한다
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404()

#     # 저장하는 로직
#     if request.method == 'POST':
#         # 새로운 모델 객체를 갖는 폼을 생성하는 게 아니라 기존에 작성되었던 Post 모델 인스턴스와 수정된 데이터를 갖는 폼을 만든다.
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id) 
#     else: 
#         # 글 수정도 사용자의 입력을 받는 것이니까 폼 사용
#         post_form = PostForm(instance=post) #instance인자는 기존의 데이터 넣어주는 용도
#     return render(request, 'posts/post_form.html', {"form":post_form})
    
# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else: 
#         return render(request, 'posts/post_confirm_delete.html', {'post':post})

# def post_delete(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return redirect('post-list')