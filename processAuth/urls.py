from django.urls import path
from processAuth import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('logout/', views.logout_view, name='logout'),
]
