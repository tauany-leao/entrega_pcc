from django.urls import path

from . import views

from .views import index


urlpatterns = [
    path('cadastrar/', views.cadastrarUserEmpresa, name='cadastrarUserEmpresa'),
    path('cadastrarEmpresa/', views.cadastrarEmpresa, name='cadastrarEmpresa'),
    path('', index.as_view(), name='index'),
]