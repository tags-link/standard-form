from django.urls import path
from .views import AboutView,NewsView,ContactView,HomeView

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view() ,name='about'),
    path('news/',NewsView.as_view() ,name='news'),
    path('contact/',ContactView.as_view() ,name='contact'),
]