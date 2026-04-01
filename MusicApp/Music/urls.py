from django.urls import path

from . import views # Импорт представлений из текущего приложения

# Пространство имен для URL-шаблонов приложения

app_name = 'music'

# Список всех URL-маршрутов приложения
urlpatterns = [
    # Главная
    path('', views.home, name='home'),
    path('albums/', views.album_list, name='album_list'),
    path('tracks/', views.track_list, name='track_list'),

    # Альбомы
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/create/', views.album_create, name='album_create'),
    path('albums/<int:pk>/update/', views.album_update, name='album_update'),
    path('albums/<int:pk>/delete/', views.album_delete, name='album_delete'),

    # Треки
    path('tracks/<int:pk>/', views.track_detail, name='track_detail'),
    path('tracks/create/', views.track_create, name='track_create'),
    path('tracks/<int:pk>/update/', views.track_update, name='track_update'),
    path('tracks/<int:pk>/delete/', views.track_delete, name='track_delete'),
   
]