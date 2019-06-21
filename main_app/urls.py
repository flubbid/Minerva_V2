from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('students/create', views.StudentCreate.as_view(), name='stud_create'),
    # path('students/', views.student_index, name='stud_index'),
    path('Assignments/', views.ass_index, name='ass_index'),
    path('Assignments/<int:dog_id>/', views.ass_detail, name='detail'),
    path('Assignments/create/', views.AssCreate.as_view(), name='ass_create'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
