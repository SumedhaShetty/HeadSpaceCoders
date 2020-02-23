from django.contrib import admin
from django.urls import path, include
from . import views
from organize import views as organize_views

app_name = 'organize'

urlpatterns = [
    path('sems/',views.sems, name='sems'),
    path('sems/post_create/',views.post_create, name="post_create"),
    path('sems/post_detail/<int:id>',views.post_detail, name="post_detail"),   
    path('sems/post_list/',views.post_list, name="post_list"),
    path('sems/post_join/<int:id>',views.post_join, name="post_join"),
    path('sems/post_update/<int:id>',views.post_update, name="post_update"),
    path('sems/post_delete/<int:id>',views.post_delete, name="post_delete"),
 
]