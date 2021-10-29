from django.contrib import admin
from .models import User, Magazine, Category, Editor, Pay,  Inquiry, Subscription   # 같은 경로의 models.py에서 User라는 클래스를 임포트한다.
# Board, Comment, Post, PostFile,
# Register your models here.
# class UserTypeAdmin(admin.ModelAdmin) :
#     list_display = ('id','name')
#
#
# admin.site.register(UserType, UserTypeAdmin) #site에 등록

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username','date_joined')

admin.site.register(User, UserAdmin) #site에 등록

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_display = ('id', 'name','slug')
    # prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class MagazineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date','eid', 'cid', 'available_display')
    # list_display = ('id', 'title', 'slug', 'date', 'editor_id', 'category_id', 'available_display')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Magazine, MagazineAdmin)



class EditorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'myself')
admin.site.register(Editor, EditorAdmin)

class PayAdmin(admin.ModelAdmin):
    list_display = ('pay_id', 'author', 'sub_no', 'price', 'card_payment', 'bank_number', 'pay_date', 'start_date')
admin.site.register(Pay, PayAdmin)

# class BoardAdmin(admin.ModelAdmin):
#     list_display = ('board_no', 'board_name')
#
# admin.site.register(Board, BoardAdmin)
#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('comment_no', 'post_no', 'author', 'comment_contents', 'comment_date')
# admin.site.register(Comment, CommentAdmin)
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('post_no', 'author', 'post_title', 'post_contents', 'post_date', 'board_no')
# admin.site.register(Post, PostAdmin)
#
# class PostFileAdmin(admin.ModelAdmin):
#     list_display = ('file_no','post_no', 'postfile')
# admin.site.register(PostFile, PostFileAdmin)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('inquiry_no', 'author', 'magazine', 'inquiry_date')
admin.site.register(Inquiry, InquiryAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('sub_no', 'sub_name', 'sub_price')
admin.site.register(Subscription, SubscriptionAdmin)