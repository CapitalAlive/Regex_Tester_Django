
from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.welcome, name='welcome'),
    path('result/<int:pk>/', views.Result.as_view(), name='result'),
    path("history/", views.history, name="history")
]
