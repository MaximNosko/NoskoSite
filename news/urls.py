from django.urls import path
from news.views import index
from news.views import post
from news.views import cats
from news.views import cat
from news.views import reg
from news.views import my_login
from news.views import my_logout
from news.views import kw
from news.views import keywords
from news.views import delcom

urlpatterns = [path('',index),
                path('cat<int:cat_id>/', cat),
                path('kw<int:kw_id>/', kw),
               path('<int:post_id>/', post, name='post'),
               path('cats/',cats),
               path('reg/', reg),
               path('login/', my_login),
               path('logout/', my_logout),
               path('kws/', keywords),
               path('delcom/', delcom)]