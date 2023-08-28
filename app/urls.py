from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    #Old clients
    path('client/add', views.add_client, name='add_client'),
    path('add/newClient', views.add_new_client, name='add_new_client'),
    path('get/client', views.get_client, name='get_client'),
    path('view/client', views.view_client, name='view_client'),
    path('update/client', views.update_client, name='update_client'),
    path('delete/client', views.delete_client, name='delete_client'),

    #API Greyhounds
    path('api/v1/greyhounds/profile/get/', views.greyhounds_profile_get, name='greyhounds_profile_get'),
    path('api/v1/greyhounds/profile/filter/', views.greyhounds_profile_filter, name='greyhounds_profile_get'),
    path('api/v1/greyhounds/profile/new/', views.greyhounds_new, name='greyhounds_profile_get'),
    path('api/v1/races/day/filter', views.races_day_filter, name='greyhounds_profile_filter'),
    path('api/v1/races/day/new', views.races_day_new, name='greyhounds_profile_new'),
    path('api/v1/races/day/remove', views.races_day_remove, name='greyhounds_profile_remove'),
    path('api/v1/races/new', views.races_new, name='greyhounds_profile_new'),
    path('api/v1/races/filter', views.races_filter, name='greyhounds_profile_filter'),
    path('api/v1/race/update', views.race_update, name='greyhounds_profile_update'),
    path('api/v1/race/calculates', views.race_calculates),
    path('api/v1/race/delete', views.race_delete, name='greyhounds_profile_delete'),

]
