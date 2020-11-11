# pages/urls.py
from django.urls import path 
from django.views.generic import TemplateView
from .views import homePageView, RenderedTaskView
urlpatterns = [
    path('hm', RenderedTaskView.as_view(), name='/'),
    path('home', homePageView, name='home'),
]