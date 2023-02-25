from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('get_all/', PostsList.as_view()),
    path('create/', PostCreate.as_view()),
    path('drop/<int:pk>', PostDetail.as_view()),
]
