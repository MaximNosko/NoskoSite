from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import News
from .models import Category
from .models import Keyword
from .models import Comment

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CommentForm,DelComment


# Create your views here.
print(HttpResponse("Новости"))
def index(request):
    try:
        post_spisok = News.objects.all()
    except News.DoesNotExist:
        return render(request, 'news/error.html')
    return render(request, 'news/index.html', {'post_spisok': post_spisok})
    #return HttpResponse("Новости")

def post(request, post_id):
    post = News.objects.get(id=post_id)
    #delComForm = DelComment()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/'+str(post_id))
    else:
        try:
            form = CommentForm()
        except News.DoesNotExist:
            return render(request, 'news/error.html')
    return render(request, 'news/post.html', {"post":post,"form":form}) #,"delform":delComForm}

def cats(request):
    try:
        category_spisok = Category.objects.all()
    except News.DoesNotExist:
        return render(request, 'news/error.html')
    return render(request, 'news/categories.html', {'category_spisok': category_spisok})

def cat(request,cat_id):
    try:
        cat = Category.objects.get(id=cat_id)
        post_spisok = cat.news_set.all()
    except News.DoesNotExist:
        return render(request, 'news/error.html')
    return render(request, 'news/category.html', {"post_spisok":post_spisok,"cat":cat})

def reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'news/reg.html', {'form': form})

def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)

            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})

def my_logout(request):
    logout(request)
    return redirect('/')

def kw(request,kw_id):
    try:
        kw = Keyword.objects.get(id=kw_id)
        news_set=News.objects.filter(keywords__in=[kw])
    except News.DoesNotExist:
        return render(request, 'news/error.html')
    return render(request, 'news/keyword.html', {"kw":kw,"news_set":news_set})

def keywords(request):
    try:
        kw_spisok = Keyword.objects.all()
    except News.DoesNotExist:
        return render(request, 'news/error.html')
    return render(request, 'news/keywords.html', {'kw_spisok': kw_spisok})


def delcom(request):
    if request.method == 'POST':
        Comment.objects.filter(id=request.POST.get('comment_id',"")).delete()
        return redirect("/"+str(request.POST.get('news_id',"")))
    return redirect("/")