from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class NewsView(TemplateView):
    template_name = 'news.html'
   

class ContactView(TemplateView):
    template_name = 'contact.html'

class HomeView(TemplateView):
    template_name = 'index.html'
