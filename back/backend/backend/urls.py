# backend/backend/urls.py   ← открой именно этот файл!

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Welcome to the Flashcard App API"})
urlpatterns = [
    path('', home),                                   # ← теперь главная работает
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),                # ← наши API
    path('api-auth/', include('rest_framework.urls')),  # логин для browsable API (удобно)
]