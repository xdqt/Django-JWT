from django.conf.urls import url
from verifytoken import views
urlpatterns = [
    url('posts/', views.posts),
]