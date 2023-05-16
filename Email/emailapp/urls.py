from . import views
from django.urls import path, include

urlpatterns = [
    # path('', views.email, name='email'),
    # path('', views.form, name='form'),
    path('set', views.session, name='session'),
    path('get', views.getsession, name='getsession'),

    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('index', views.index, name='index'),


]


