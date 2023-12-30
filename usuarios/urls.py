from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('atualiza_usuario/', views.att_usuario, name='atualiza_usuario')
]