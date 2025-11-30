
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Courses
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),

    # Trainers
    path('trainers/', views.TrainerListView.as_view(), name='trainer-list'),
    path('trainers/<int:pk>/', views.TrainerDetailView.as_view(), name='trainer-detail'),
    path('trainers/create/', views.TrainerCreateView.as_view(), name='trainer-create'),

    # Announcements
    path('announcements/', views.AnnouncementListView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/create/', views.AnnouncementCreateView.as_view(), name='announcement-create'),
]
