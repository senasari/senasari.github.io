from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]


