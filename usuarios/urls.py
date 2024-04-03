from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('atualiza_usuario/', views.att_usuario, name='atualiza_usuario'),
    path('update_evolucao/<int:id>/', views.update_evolucao, name="update_evolucao"),
    path('excluir_evolucao/<int:id>/', views.excluir_evolucao, name="excluir_evolucao"),
    path('update_usuario/<int:id>/' , views.update_usuario, name="update_cliente"),
]