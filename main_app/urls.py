from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('assignments/', views.ass_index, name='ass_index'),
    path('assignments/<int:ass_id>/', views.ass_detail, name='detail'),
    path('assignments/create/', views.AssCreate.as_view(), name='ass_create'),
]