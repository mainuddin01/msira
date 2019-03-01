from django.urls import path

from . import views

app_name = 'repair'

urlpatterns = [
    path('', views.PhoneListView.as_view(), name='home'),
    path('phone/create/', views.PhoneCreateView.as_view(), name='create'),
    path('phone/<int:pk>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/<int:pk>/edit/', views.PhoneUpdateView.as_view(), name='phone_edit'),
    path('phone/<int:pk>/delete/', views.PhoneDeleteView.as_view(), name='phone_delete'),
    path('problem_type/', views.ProblemTypeListView.as_view(), name='problem_type_list'),
    path('problem_type/<int:pk>/create/', views.ProblemTypeCreateView.as_view(), name='problem_type_create'),
    path('problem_type/<int:pk>/', views.ProblemTypeDetailView.as_view(), name='problem_type_detail'),
    path('problem_type/<int:pk>/edit/', views.ProblemTypeEditView.as_view(), name='problem_type_edit'),
    path('problem_type/<int:pk>/delete/', views.ProblemTypeDeleteView.as_view(), name='problem_type_delete'),
    path('schedule/<int:pk>/', views.ScheduleView.as_view(), name='schedule'),
]