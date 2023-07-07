from django.urls import path
from .views import index_hw

urlpatterns = [
    path('', index_hw)
]