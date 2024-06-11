from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('', views.PublicacionView.as_view(), name='index'),
    path('profesor/<int:pk>/', views.ProfesorView.as_view(), name='profesor'),
    path('materia/<int:pk>/', views.MateriaView.as_view(), name='materia'),
    path('crear_resena/', views.ResenaCreateView.as_view(), name='crear_resena')
]