from django.contrib import admin
from .models import Post, Board, Comment, User, Photo


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_no', 'board_name')

admin.site.register(Board, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_no', 'post', 'author', 'comment_contents', 'comment_date')
admin.site.register(Comment, CommentAdmin)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('post_no', 'author', 'post_title', 'post_contents', 'post_date', 'board_no')
# admin.site.register(Post, PostAdmin)

# class PostFileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'postfile','post_no')
# admin.site.register(PostFile, PostFileAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image')
admin.site.register(Photo, PhotoAdmin)
#!!!!!!!!!!photo 테이블은 27-29번이랑 33번 주석 풀고 사용하기!!!
# Photo 클래스를 inline으로 나타낸다.
# class PhotoInline(admin.TabularInline):
#     model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다.
class PostAdmin(admin.ModelAdmin):
    # inlines = [PhotoInline, ]
    list_display = ('post_no', 'author', 'post_title', 'post_contents', 'post_date','board_no')


# Register your models here.
admin.site.register(Post, PostAdmin)