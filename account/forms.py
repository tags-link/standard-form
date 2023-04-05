from django.forms import ModelForm
from .models import profile
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class Registerform(UserCreationForm):
    class Meta :
        model = User
        fields = ('username','email','password1','password2',)

class NewProfleForm(ModelForm):
    class Meta :
        model = profile
        fields = '__all__'


