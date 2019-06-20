from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assignments/', views.ass_index, name='ass_index'),
    path('assignments/<int:ass_id>/', views.ass_detail, name='detail'),
    path('assignments/create/', views.AssCreate.as_view(), name='cats_create'),
    # path(''),
]