from django.db import models
from django.urls import reverse
from sandwich.models import User

# 게시판 테이블
class Board(models.Model):
    board_no = models.IntegerField(primary_key=True, verbose_name='게시판번호')
    board_name = models.CharField(max_length=20, verbose_name='게시판이름')

    def __str__(self):
        return self.board_name


# 게시글 테이블
class Post(models.Model):
    post_no = models.AutoField(primary_key=True, verbose_name='게시글 번호')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='아이디',null=False)
    post_title = models.CharField(max_length=20, verbose_name='제목')
    post_contents = models.TextField(verbose_name='내용')
    post_date = models.DateTimeField(blank=True, verbose_name='등록일', auto_now_add=True)
    board_no = models.ForeignKey(Board, null=True, blank=True, on_delete=models.CASCADE, verbose_name='게시판 유형')

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        return reverse('detail', args=[int(self.post_no)])

    def __str__(self):
        return self.post_title

#게시글 첨부파일 테이블
class Photo(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='파일번호')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, verbose_name='게시판번호')
    # post_no = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, verbose_name='게시글번호')
    # post_no = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글번호')
    # postfile = models.ImageField(upload_to='postfile/$Y/%m/$d', default='postfile/no_image.png', verbose_name='첨부파일명')
    image = models.ImageField(upload_to='post/',blank=True, null=True,verbose_name='첨부파일명')

    # def __int__(self):
    #     return self.id
# 게시글_댓글 테이블
class Comment(models.Model):
    comment_no = models.AutoField(primary_key=True, verbose_name='댓글번호')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글번호', related_name='comments')
    author = models.ForeignKey(User,  verbose_name='회원ID',on_delete=models.CASCADE)
    comment_contents = models.TextField(verbose_name='댓글내용')
    comment_date = models.DateTimeField(blank=True, verbose_name='등록일' ,auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']


    def __str__(self):
        return self.comment_contents