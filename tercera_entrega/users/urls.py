from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.loginIn, name="login"), #Sadri - Sad1594.
    #path("profile/", views.profile, name="profile"), #Me quedé acá
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
