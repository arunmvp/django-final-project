from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', signup , name="Signup"),
    path("signupFun/", signupFun, name="SignupFun"),
    path("log_in/", loginview, name="Login"),
    path("loginFun/", loginPage, name="LoginFun") 
] 

name = "arun"