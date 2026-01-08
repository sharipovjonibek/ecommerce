from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput,TextInput

# Registration form

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields=['username','email','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)
        
        # Make email field as required

        self.fields['email'].required=True


    # Email Validation

    def clean_email(self):

        email=self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('This email is invalid')
        
        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")
        
        return email
        


# Login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())

    password = forms.CharField(widget=PasswordInput())

    

