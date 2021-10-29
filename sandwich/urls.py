from django.urls import path
from . import views
from . models import Magazine
import sandwich.views
from .views import *
from django.views.generic.detail import DetailView


# app_name = 'sandwich'
urlpatterns = [
# path('',views.index, name='index'),
    # path('',sandwich.views.index, name='index'),
    path('', views.magazine_list, name='index'),
    path('magazine/', views.magazine, name='magazine'),
    # path('<category_slug>/',views.magazine_in_category, name='magazine_in_category'),
    # path('<int:id>/<magazine_slug>/', views.magazine_detail, name='magazine_detail'),
    path('magazine_food/',views.magazine_food, name='magazine_food'),
    path('magazine_trip/',views.magazine_trip, name='magazine_trip'),
    path('magazine_literature/',views.magazine_literature, name='magazine_literature'),
    path('magazine_daily/',views.magazine_daily, name='magazine_daily'),
    path('magazine_sport/',views.magazine_sport, name='magazine_sport'),
    path('magazine_create/', MagazineCreateView.as_view(template_name='magazine/magazine_create.html'), name='magazine_create'),
    path('magazine_detail/<int:pk>/', MagazineDetailView.as_view(template_name='magazine/magazine_detail.html'), name='magazine_detail'),
    path('magazine_update/<int:pk>/', MagazineUpdateView.as_view(template_name='magazine/magazine_update.html'), name='magazine_update'),
    path('magazine_delete/<int:pk>/', MagazineDeleteView.as_view(template_name='magazine/magazine_confirm_delete.html'), name='magazine_delete'),


]