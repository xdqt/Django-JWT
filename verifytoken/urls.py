from django.conf.urls import url
from verifytoken import views
from django.urls import path
urlpatterns = [
    url('posts', views.posts),
    path('register', views.RegisterView.as_view(), name='auth_register'),
    url('auth',views.authenticate_user,name='gettoken'),
]