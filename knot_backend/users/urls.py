from django.urls import path
from .views import AddEnterpriseView, UserSignUpView, UserLoginView


urlpatterns = [
     path('addenterprise/',AddEnterpriseView.as_view()),
     path('usersignup/',UserSignUpView.as_view()),
     path('userlogin/',UserLoginView.as_view()),
]