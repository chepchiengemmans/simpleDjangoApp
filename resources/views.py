
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Trainer, Announcement
from django.urls import reverse_lazy

def home(request):
	return render(request, 'home.html')

# Courses Views
class CourseListView(ListView):
	model = Course
	template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'

class CourseCreateView(CreateView):
	model = Course
	fields = ['title', 'description', 'duration']
	template_name = 'courses/course_form.html'
	success_url = reverse_lazy('course-list')

# Trainers Views
class TrainerListView(ListView):
	model = Trainer
	template_name = 'trainers/trainer_list.html'

class TrainerDetailView(DetailView):
	model = Trainer
	template_name = 'trainers/trainer_detail.html'

class TrainerCreateView(CreateView):
	model = Trainer
	fields = ['name', 'bio', 'experience_years']
	template_name = 'trainers/trainer_form.html'
	success_url = reverse_lazy('trainer-list')

# Announcements Views
class AnnouncementListView(ListView):
	model = Announcement
	template_name = 'announcements/announcement_list.html'

class AnnouncementDetailView(DetailView):
	model = Announcement
	template_name = 'announcements/announcement_detail.html'

class AnnouncementCreateView(CreateView):
	model = Announcement
	fields = ['title', 'message']
	template_name = 'announcements/announcement_form.html'
	success_url = reverse_lazy('announcement-list')
