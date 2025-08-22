from django.urls import path
from .views import *

urlpatterns = [
    path('create/', crudInfo.as_view()),
    path('get/', crudInfo.as_view()),
    path('get/<int:user_id>', crudInfo.as_view())
]

