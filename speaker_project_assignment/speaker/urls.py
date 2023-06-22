from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_speakers, name='conference'),
    path('create/', views.create_a_new_speaker, name='create_a_new_speaker'),
    path('<int:speaker_id>/', views.view_single_speaker, name='view_single_speaker'),
    path('<int:speaker_id>/update', views.update_speaker, name='update_speaker'),
    path('<int:speaker_id>/delete', views.delete_speaker, name='delete_speaker'),
]