# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from idlelib.idle_test.test_format import Editor
from typing import Type

from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# class UserType(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=10, choices=TYPE, default='N', verbose_name='회원유형')
#
#     def __str__(self):
#         return self.type_name

class User(AbstractUser):
    # id= models.IntegerField(primary_key=True, verbose_name='회원번호')
    username = models.CharField(max_length=10, primary_key=True, verbose_name='회원ID')
    phone = models.CharField(max_length=13, null=True, blank=True,verbose_name='핸드폰번호')
    birthdate = models.DateField(null=True, blank=True, verbose_name='생년월일')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    class Meta:
        ordering = ['date_joined']
        verbose_name = 'User'  # 단수
        verbose_name_plural = 'Users' # 복수

    def __str__(self):
        return self.username


class Category(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='카테고리번호')
    name = models.CharField(max_length=10, db_index=True, verbose_name='카테고리명')
    meta_description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'  # 단수
        verbose_name_plural = 'categories' # 복수

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('magazine_in_category', args=[self.slug])

class Editor(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='번호')
    name = models.CharField(max_length=10, verbose_name='이름')
    myself = models.TextField(blank=True, null=True, verbose_name='자기소개')

    def __str__(self):
        return self.name

class Magazine(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='잡지번호')
    title = models.CharField(max_length=45, db_index=True, verbose_name='잡지제목')
    eid = models.ForeignKey(Editor, on_delete=models.CASCADE, verbose_name='에디터')
    image = models.ImageField(upload_to='magazine_img/%Y/%m/%d',verbose_name='대표이미지',blank=True, null=True)
    info = models.TextField(verbose_name='설명',blank=True, null=True)
    date = models.DateTimeField(verbose_name='등록일', auto_now_add=True)
    file = models.FileField(upload_to='pdf/',blank=True, null=True, verbose_name='PDF 첨부파일')
    cid = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='카테고리')
    available_display = models.BooleanField('Display', default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('sandwich:magazine_detail', args=[self.id, self.slug])



class Subscription(models.Model):
    sub_no = models.IntegerField(primary_key=True,verbose_name='구독권 번호')
    sub_name = models.CharField(max_length=10, verbose_name='구독권명')
    sub_price = models.IntegerField(verbose_name='구독권금액')

    def __str__(self):
        return self.sub_name

class Pay(models.Model):
    pay_id = models.AutoField(primary_key=True, verbose_name='결제번호')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원번호')
    sub_no = models.ForeignKey(Subscription, on_delete=models.CASCADE, verbose_name='구독권번호')
    price = models.IntegerField(verbose_name = '결제금액')
    PAYTYPE = {
        ('선택안함', '선택안함'),
        ('TRUE', 'TRUE'),
        ('FALSE', 'FALSE'),
    }
    card_payment = models.CharField(max_length=10, choices=PAYTYPE, default='N', verbose_name='카드결제여부')
    bank_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='계좌번호')
    pay_date = models.DateTimeField(blank=True, verbose_name='결제일')
    start_date = models.DateTimeField(blank=True, verbose_name='이용시작일')

    def __int__(self):
        return self.pay_id

# 다운로드 테이블
class Inquiry(models.Model):
    inquiry_no = models.IntegerField(primary_key=True, verbose_name='조회번호')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원번호')
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE, verbose_name='잡지번호')
    inquiry_date = models.DateTimeField(blank=True, verbose_name="다운로드일")

    def __int__(self):
        return self.inquiry_no

# # 게시판 테이블
# class Board(models.Model):
#     board_no = models.IntegerField(primary_key=True, verbose_name='게시판번호')
#     board_name = models.CharField(max_length=20, verbose_name='게시판이름')
#
#     def __str__(self):
#         return self.board_name
#
# # 게시글 테이블
# class Post(models.Model):
#     post_no = models.IntegerField(primary_key=True, verbose_name='게시글번호')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원ID')
#     post_title = models.CharField(max_length=45, verbose_name='게시글제목')
#     post_contents = models.TextField(verbose_name='게시글내용')
#     post_date = models.DateTimeField(blank=True, verbose_name='등록일', auto_now_add=True)
#     board_no = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='게시판번호')
#
#     class Meta:
#         ordering = ['-post_date']
#
#     def __int__(self):
#         return self.post_no
#
#
# #게시글 첨부파일 테이블
# class PostFile(models.Model):
#     file_no = models.IntegerField(primary_key=True, verbose_name='파일번호')
#     post_no = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글번호')
#     filename = models.ImageField(upload_to='postfile/$Y/%m/$d', default='postfile/no_image.png', verbose_name='첨부파일명')
#
#     def __int__(self):
#         return self.file_no
#
# # 게시글_댓글 테이블
# class Comment(models.Model):
#     comment_no = models.IntegerField(primary_key=True, verbose_name='댓글번호')
#     post_no = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글번호')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원ID')
#     comment_contents = models.TextField(verbose_name='댓글내용')
#     comment_date = models.DateTimeField(blank=True, verbose_name='등록일' ,auto_now_add=True)
#
#     class Meta:
#         ordering = ['-comment_date']
#
#     def __int__(self):
#         return self.comment_no





# class User(models.Model):
#     members_no = models.IntegerField(primary_key=True)
#     members_name = models.CharField(max_length=20, verbose_name = '사용자명')
#     members_id = models.CharField(max_length=45, verbose_name = '사용자id')
#     members_pw = models.CharField(max_length=45, verbose_name = '사용자pw')
#     members_birthday = models.DateField()
#     members_phone = models.CharField(max_length=30)
#     members_email = models.CharField(max_length=45)
#     registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
#     type_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#
#     def __str__(self):
#         return self.members_name  ## 관리자 페이지에 표시하는거--
#
#
# class Board(models.Model):
#     board_no = models.IntegerField(primary_key=True)
#     board_name = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'board'
#
#
# class Categories(models.Model):
#     categories_no = models.IntegerField(primary_key=True)
#     categories_name = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'categories'
#
#
# class Comments(models.Model):
#     comments_no = models.IntegerField(primary_key=True)
#     post_no = models.IntegerField()
#     members_no = models.IntegerField()
#     comments_contents = models.TextField()
#     comments_date = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'comments'
#
#
# class Editor(models.Model):
#     members_no = models.IntegerField()
#     contract_start = models.DateField(blank=True, null=True)
#     contract_end = models.DateField(blank=True, null=True)
#     myself = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'editor'
#
#
# class EditorImg(models.Model):
#     img_no = models.IntegerField()
#     members_no = models.IntegerField()
#     editor_img_route = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'editor_img'
#
#
# class Magazine(models.Model):
#     magazine_no = models.IntegerField(primary_key=True)
#     magazine_name = models.CharField(max_length=45)
#     magazine_date = models.DateField()
#     categories_no = models.IntegerField()
#     members_no = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'magazine'
#
#
# class MagazineDetail(models.Model):
#     magazine_detail_no = models.IntegerField()
#     magazine_no = models.IntegerField()
#     magazine_detail_filename = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'magazine_detail'
#
#
# class MemberType(models.Model):
#     type_id = models.IntegerField(primary_key=True)
#     type_name = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'member_type'
#
#
#
#
#
# class Pay(models.Model):
#     pay_no = models.IntegerField()
#     members_no = models.IntegerField()
#     card_payment = models.CharField(max_length=10)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'pay'
#
#
# class Post(models.Model):
#     post_no = models.IntegerField(primary_key=True)
#     members_no = models.IntegerField()
#     post_title = models.CharField(max_length=45)
#     post_contents = models.TextField()
#     post_date = models.DateField()
#     board_no = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'post'
#
#
# class PostFile(models.Model):
#     post_file_no = models.IntegerField()
#     post_no = models.IntegerField()
#     post_file_route = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'post_file'