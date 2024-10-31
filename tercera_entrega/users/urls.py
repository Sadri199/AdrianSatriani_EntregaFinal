from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.loginIn, name="login"), #Sadri -  Sad15977
    path("profile/", views.myProfile, name="myProfile"),
    path("profile/edit", views.editProfile, name="editProfile"),
    path("profile/password", views.ChangePassword.as_view(), name="ChangePassword"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
