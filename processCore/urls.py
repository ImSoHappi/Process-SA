from django.urls import path
from . import views

urlpatterns = [
    path('client_list', views.client_list, name="client_list"),
    path('client_list/add_client', views.add_client, name="add_client"),
    
    path('unidad_list/<int:client_pk>/', views.unidad_list, name="unidad_list"),
    path('unidad_list/<int:client_pk>/agregar_unidad', views.agregar_unidad, name="agregar_unidad"),
    
    path('process_list/<int:client_pk>/', views.process_list, name="process_list"),
    path('process_list/<int:client_pk>/add_process', views.add_process, name="add_process"),

    path('flujo_list/<int:client_pk>/<int:process_pk>/', views.listado_flujo, name="listado_flujo"),
    path('flujo_list/<int:client_pk>/<int:process_pk>/agregar_flujo', views.agregar_flujo, name="agregar_flujo"),
    
    path('process_detail/<int:client_pk>/<int:process_pk>/<int:task_pk>/reportar_problema', views.reportar_problema, name="reportar_problema"),
    path('problema_list', views.problema_list, name="problema_list"),

    path('process_detail/<int:client_pk>/<int:process_pk>/', views.process_detail, name="process_detail"),
    path('process_detail/<int:client_pk>/<int:process_pk>/add_task', views.add_task, name="add_task"),
    path('process_detail/<int:client_pk>/<int:process_pk>/<int:task_pk>', views.subordinada_list, name="subordinada_list"),
    path('process_detail/<int:client_pk>/<int:process_pk>/<int:task_pk>/agregar_subordinada', views.agregar_subordinada, name="agregar_subordinada"),
    path('process_detail/<int:client_pk>/<int:process_pk>/<int:task_pk>/reject_task', views.reject_task, name="reject_task"),
    path('process_detail/<int:client_pk>/<int:process_pk>/<int:task_pk>/<int:reject_pk>/detail_reject', views.detail_reject, name="detail_reject"),
    
]
