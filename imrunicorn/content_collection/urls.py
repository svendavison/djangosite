from django.urls import path, include
from . import views

app_name = 'content_collection'
urlpatterns = [
    path('', views.page_blank, name='blank'),

    path('videos/', views.page_video_list, name='video_list'),
    path('videos/<int:video_pk>', views.page_latest_video_by_pk, name='video_list'),

    path('videos/latest', views.page_latest_video, name='videos_latest'),

    path('carousel', views.page_carousel, name='carousel'),
    path('carousel/recent', views.page_carousel_recent, name='carousel_recent'),

    path('dnd5e', views.page_dnd5e_list, name='dnd5e_list'),
    path('dnd5e/<int:video_pk>', views.page_dnd5e_list_by_pk, name='dnd5e_list'),

]
