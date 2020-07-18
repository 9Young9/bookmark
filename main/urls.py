from django.urls import path
from .views import * # views.py에 있는 모든 걸(*) 가져와라

app_name = 'main'

urlpatterns = [
    path('', show, name = "show"),
    path('new/', new, name = "new"),
    path('edit/<int:pk>', edit, name = "edit"),  # <int:pk> : 순서
    path('delete/<int:pk>', delete, name = "delete"),
]