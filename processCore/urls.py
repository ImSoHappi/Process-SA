from django.urls import path
from . import views

urlpatterns = [
    path('client_list', views.client_list, name="client_list"),
    path('client_list/add_client', views.add_client, name="add_client"),

    path('process_list/<int:client_pk>/', views.process_list, name="process_list"),
    path('process_list/<int:client_pk>/add_process', views.add_process, name="add_process"),

    path('process_detail/<int:client_pk>/<int:process_pk>/', views.process_detail, name="process_detail"),
    path('process_detail/<int:client_pk>/<int:process_pk>/add_task', views.add_task, name="add_task"),
    
]
