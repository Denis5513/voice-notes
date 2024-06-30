from django.urls import path
from .views import create_note

urlpatterns = [
    path('new/', create_note, name='create_note'),
]