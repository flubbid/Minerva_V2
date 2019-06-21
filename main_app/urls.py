from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('students/create', views.StudentCreate.as_view(), name='stud_create'),
    # path('students/', views.student_index, name='stud_index'),
    path('assignments/', views.ass_index, name='ass_index'),
    path('assignments/<int:assignment_id>/', views.ass_detail, name='detail'),
    path('assignments/create/', views.AssCreate.as_view(), name='ass_create'),
]