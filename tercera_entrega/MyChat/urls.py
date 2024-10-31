from django.urls import path, include
from MyChat import views

app_name = 'chat'

urlpatterns = [
    path("", views.chatPage, name="chatPage")
]
