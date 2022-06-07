from django import views
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.publicacoes, name = 'publicacoes'),
    path('criar/', views.criar, name = 'criar'),
    path('excluir/<int:postagem_id>/',views.excluir,  name='excluir'),
    path('editar/<int:postagem_id>/', views.editar, name = 'editar'),
    path('feed/<str:cursos>/', views.feed, name='feed')
]
