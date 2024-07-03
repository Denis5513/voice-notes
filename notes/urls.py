from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_note, name='create_note'),
    path('', views.notes_list, name='notes_list'),
    path('note_detail/<int:note_id>', views.note_detail, name='note_detail'),
    path('add_user_tag', views.add_user_tag, name='add_user_tag'),
]