from django.urls import path
from custom_user.views import CreateUser

urlpatterns = [
    path('register/', CreateUser.as_view()),
]