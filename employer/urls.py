from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('employer/', views.jobdesc,name='job description')
]