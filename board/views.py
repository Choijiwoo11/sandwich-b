from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# index.html 페이지를 부르는 index 함수
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import ListView

from board.forms import CommentForm
from board.models import Post, Photo, Board, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# def communication(request):
#     post_list = Post.objects.all()
#     return render(request, 'board/communication.html',{'post_list': post_list,})
class PostListView(ListView):
    model = Post
    paginate_by = 6
    # queryset = Post.objects.filter(board_no=1)

@login_required
def post_detail(request):
    post = Post.objects.all()
    return render(request, 'board/detail.html', {'post': post })


class PostDetailView(LoginRequiredMixin ,DetailView):
    model = Post

# @login_required(login_url='common:login')
# def comment_create_question(request, post_no):
#     """
#     pybo 질문댓글등록
#     """
#     post = get_object_or_404(Post, pk=post_no)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['board_no','post_title', 'post_contents']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.username # 현재 로그인 한 사용자로 설정
        if form.is_valid(): # 입력된 값 검증
            form.instance.save() # 이상이 없다면, 데이터베이스에 저장하고,
            return redirect('/board/list') # 메인 페이지로 이동
        else:
            return self.render_to_response({'form':form}) # 이상이 있다면, 작성된 내용을


def create(request):
    if (request.method == 'POST'):
        post = Post()
        # post.board_no = request.POST['no']
        post.post_title = request.POST['title']
        post.post_contents = request.POST['content']
        post.post_date = timezone.datetime.now()
        post.author = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return redirect('/board/list/')
    else:
        return render(request, 'board/post_create.html')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['board_no','post_title', 'post_contents']
    template_name_suffix = '_update'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('list')

# blog.html 페이지를 부르는 blog 함수
# def inquiry(request):
#     return render(request, 'board/inquiry.html')

class InquiryListView(ListView):
    model = Post
    paginate_by = 6
    queryset = Post.objects.filter(board_no=2)

@login_required
def inquiry_detail(request):
    inquiry = Post.objects.all()
    return render(request, 'board/inquery_detail.html', {'inquiry': inquiry})

class InquiryDetailView(LoginRequiredMixin ,DetailView):
    model = Post

class InquiryCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['board_no','post_title', 'post_contents']
    success_url = reverse_lazy('inquiry_list')
    template_name = 'board/inquiry_create.html'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.username # 현재 로그인 한 사용자로 설정
        if form.is_valid(): # 입력된 값 검증
            form.instance.save() # 이상이 없다면, 데이터베이스에 저장하고,
            return redirect('/board/inquiry_list') # 메인 페이지로 이동
        else:
            return self.render_to_response({'form':form}) # 이상이 있다면, 작성된 내용을

class InquiryUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['board_no','post_title', 'post_contents']
    success_url = reverse_lazy('inquiry_list')

class InquiryDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('inquiry_list')
