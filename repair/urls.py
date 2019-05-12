from django.urls import path

from . import views

app_name = 'repair'

urlpatterns = [
    path('', views.PhoneListView.as_view(), name='home'),
    path('dashboard/brands/', views.DashboardBrandListView.as_view(), name='dashboard_brand_list'),
    path('dashboard/phones/', views.DashboardPhoneListView.as_view(), name='dashboard_phone_list'),
    path('dashboard/problem_types/', views.DashboardProblemTypeListView.as_view(), name='dashboard_problem_type_list'),
    path('dashboard/phone_problems/', views.DashboardPhoneProblemListView.as_view(), name='dashboard_phone_problem_list'),
    path('dashboard/colors/', views.DashboardColorListView.as_view(), name='dashboard_color_list'),
    path('brand/create/', views.BrandCreateView.as_view(), name='add_brand'),
    path('brand/<int:pk>/edit/', views.BrandUpdateView.as_view(), name='brand_edit'),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),
    path('phone/create/', views.PhoneCreateView.as_view(), name='add_phone'),
    path('phone/<int:pk>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/<int:pk>/edit/', views.PhoneUpdateView.as_view(), name='phone_edit'),
    path('phone/<int:pk>/delete/', views.PhoneDeleteView.as_view(), name='phone_delete'),
    path('problem_type/', views.ProblemTypeListView.as_view(), name='problem_type_list'),
    path('problem_type/create/', views.ProblemTypeCreateView.as_view(), name='add_problem_type'),
    path('problem_type/<int:pk>/', views.ProblemTypeDetailView.as_view(), name='problem_type_detail'),
    path('problem_type/<int:pk>/edit/', views.ProblemTypeEditView.as_view(), name='problem_type_edit'),
    path('problem_type/<int:pk>/delete/', views.ProblemTypeDeleteView.as_view(), name='problem_type_delete'),
    path('schedule/<int:pk>/', views.ScheduleView.as_view(), name='schedule'),
    path('phone_problem/create/', views.PhoneProblemCreateView.as_view(), name='add_phone_problem'),
    path('color/create/', views.ColorCreateView.as_view(), name='add_color'),
    path('color/<int:pk>/edit/', views.ColorUpdateView.as_view(), name='color_edit'),
    path('color/<int:pk>/delete/', views.ColorDeleteView.as_view(), name='color_delete'),
]