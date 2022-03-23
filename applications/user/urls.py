from django.urls import path

from applications.user import views


uplpatterns = [
    path('user/', views.UserView.as_view())
]