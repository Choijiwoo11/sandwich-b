from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views
from .views import *
from .views import PostListView, PostCreateView, PostDetailView, InquiryListView, InquiryDetailView, InquiryCreateView
from django.views.generic.detail import DetailView


urlpatterns=[
    path('list/', PostListView.as_view(template_name='board/post_list.html'), name='list'),
    # path('communication/',PostListView.as_view(), name='list'),
    path('add/', views.create, name='add'),
    # path('add/', PostCreateView.as_view(template_name='board/post_create.html'), name='add'),
    path('detail/<int:pk>/', PostDetailView.as_view(template_name='board/post_detail.html'), name='detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(template_name='board/post_update.html'), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(template_name='board/post_confirm_delete.html'), name='delete'),
    path('inquiry_list/', InquiryListView.as_view(template_name='board/inquiry_list.html'), name='inquiry_list'),
    path('inquiry_detail/<int:pk>/', InquiryDetailView.as_view(template_name='board/inquiry_detail.html'), name='inquiry_detail'),
    path('inquiry_create/', InquiryCreateView.as_view(template_name='board/inquiry_create.html'), name='inquiry_create'),
    path('inquiry_update/<int:pk>/', InquiryUpdateView.as_view(template_name='board/inquiry_update.html'), name='inquiry_update'),
    path('inquiry_delete/<int:pk>/', InquiryDeleteView.as_view(template_name='board/inquiry_confirm_delete.html'), name='inquiry_delete'),
    # path('comment/', comment, name='comment'),
]



