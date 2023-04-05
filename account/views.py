from .models import profile
from django.urls import reverse
from .forms import Registerform,NewProfleForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView,CreateView,UpdateView


# Create your views here.
# def register(request):
#     form = Registerform(request.POST or None)
#     if request.method == 'POST':
#         form = Registerform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/dashboard')
#         else:
#             form = Registerform(request.POST or None)
#     return render(request,'register.html',{'form':form})

class LoginView(LoginView):
    template_name = 'login.html'
    
class UserRegistration(CreateView):
    template_name = 'register.html'
    form_class = Registerform
    success_url = '/login'


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login'
    

class NewProfile(LoginRequiredMixin,UpdateView):
    template_name = 'new_profile.html'
    form_class = NewProfleForm
    model = profile
    success_message = 'profile updated successfully'
    success_url = '/dashboard'

   
   
# class DeleteNewProfile(DeleteView):
#     template_name = 'delete_profile.html'
#     model = profile
#     success_url = '/dashboard'
#     context_object_name = 'profile'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = NewProfleForm
    #     return context


