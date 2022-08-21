from django.urls import path
from .views import *


urlpatterns = [
    path('view_user/<int:pk>', ViewUser.as_view(), name='view_user'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', HomeNews.as_view(), name='home'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', add_news, name='add_news')
]