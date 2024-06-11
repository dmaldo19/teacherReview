from django.urls import path
from . import views


app_name = 'profesor'
urlpatterns = [
    path('profesores/', views.ProfesorView.as_view(), name='profesores'),
]