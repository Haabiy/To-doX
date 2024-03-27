from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# for authentication
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

# import from models
from . models import todo, Profile

# Registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

# Authentication
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class usertodolist(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'content',]
        exclude = ['user',]

# Update Profile username and email, password is excluded, however, if we would like to update everything
# there is no need to create another form, we could have just used 'CreateUserForm'.
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]
        exclude = ['password1', 'password2',]

# file upload 
class UpdateProfileForm(forms.ModelForm):
    ProfilePicture = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['ProfilePicture',]

