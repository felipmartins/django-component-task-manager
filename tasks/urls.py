from django.urls import path
from tasks.views import index


urlpatterns = [
    path("", index, name="tasks-page"),
    path("login/", index, name="login-page"),
]
