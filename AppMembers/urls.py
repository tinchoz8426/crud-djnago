from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_user, name="Login"),
    path('logout', views.logout_user, name="Logout"),
    path('register', views.regiter_user, name="Register"),
]