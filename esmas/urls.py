from django.contrib import admin
from django.urls import path, include
from minha_auth.views import login

urlpatterns = [
    path('', login, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('servicos/', include('servicos.urls')),
    path('minha_auth/', include('minha_auth.urls')),
    path('accounts/', include("allauth.urls")),
]
