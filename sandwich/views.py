from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from sandwich import admin
from sandwich.models import Magazine, Category


# def magazine_in_category(request, category_slug=None):
#     current_category = None
#     categories = Category.objects.all()
#     magazines = Magazine.objects.filter(available_display=True)
#
#     if category_slug:
#         current_category = get_object_or_404(Category, slug=category_slug)
#         magazines = magazines.filter(category=current_category)
#     return render(request, 'magazine/magazine.html', {'current_category': current_category,'categories': categories,
#                                                       'magazines': magazines})

def magazine_detail(request, id, magazine_slug=None):
    magazine = get_object_or_404(Magazine, id=id, slug=magazine_slug)

    return render(request, 'magazine/magazine_detail.html', {'magazine': magazine})

def magazine_list(request):
    magazine = Magazine.objects.all()
    return render(request,'magazine/magazine_list.html', {'magazine': magazine})

def magazine(request):
    magazine = Magazine.objects.all()
    return render(request,'magazine/magazine.html', {'magazine': magazine})

def magazine_food(request):
    magazine_f = Magazine.objects.all()
    magazine_f = magazine_f.filter(cid=1)
    return render(request,'magazine/magazine_food.html', {'magazine_f': magazine_f})

def magazine_trip(request):
    magazine_t = Magazine.objects.all()
    magazine_t = magazine_t.filter(cid=2)
    return render(request,'magazine/magazine_trip.html', {'magazine_t': magazine_t})

def magazine_literature(request):
    magazine_l = Magazine.objects.all()
    magazine_l = magazine_l.filter(cid=3)
    return render(request,'magazine/magazine_literature.html', {'magazine_l': magazine_l})

def magazine_daily(request):
    magazine_d = Magazine.objects.all()
    magazine_d = magazine_d.filter(cid=4)
    return render(request,'magazine/magazine_daily.html', {'magazine_d': magazine_d})

def magazine_sport(request):
    magazine_s = Magazine.objects.all()
    magazine_s = magazine_s.filter(cid=5)
    return render(request,'magazine/magazine_sport.html', {'magazine_s': magazine_s})



# def magazine_detail(request):
#     magazine = Magazine.objects.all()
#     return render(request, 'magazine/magazine_detail.html', {'magazine': magazine})

class MagazineCreateView(LoginRequiredMixin ,CreateView):
    model = Magazine
    fields = ['cid','eid','title','info', 'image', 'file']
    success_url = reverse_lazy('magazine')
    template_name_suffix = '_create'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.username # 현재 로그인 한 사용자로 설정
        if form.is_valid(): # 입력된 값 검증
            form.instance.save() # 이상이 없다면, 데이터베이스에 저장하고,
            return redirect('/magazine/') # 메인 페이지로 이동
        else:
            return self.render_to_response({'form':form}) # 이상이 있다면, 작성된 내용을

class MagazineDetailView(DetailView):
    model = Magazine
    template_name = 'magazine/magazine_detail.html'

def index(request):
    # return HttpResponse(request, 'sandwich/index.html')
    return render(request, 'sandwich/index.html')

class MagazineUpdateView(LoginRequiredMixin, UpdateView):
    model = Magazine
    fields = ['cid','eid','title','info', 'image', 'file']
    success_url = reverse_lazy('magazine')

class MagazineDeleteView(LoginRequiredMixin, DeleteView):
    model = Magazine
    success_url = reverse_lazy('magazine')