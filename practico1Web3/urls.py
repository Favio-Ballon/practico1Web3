from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('restaurante/', permanent=True)),  # Redirige todo a /restaurante/
    path('restaurante/', include("restaurante.urls")),
]
