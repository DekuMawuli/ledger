from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token),
    path("logout/", views.user_logout),
    path("register/", views.UserCreateView.as_view())
]
