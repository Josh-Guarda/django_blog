from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    
       
        
        #This prevents loading the helptext of the fields
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Remove help texts
            # self.fields['username'].help_text = ''
            # self.fields['password1'].help_text = ''
            # self.fields['password2'].help_text = ''
            
            #Remove Label
            # self.fields['username'].label = ''
            # self.fields['password1'].label = ''
            # self.fields['password2'].label = ''
            
        class Meta:
            
            
            model=User
            fields=['username','password1','password2']
             # fields=['first_name','last_name','email','username','password1','password2']
        
            widgets={
                'password1':forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Password'}),
                'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
                # 'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email@example.com'}),
                'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
                # 'first_name':forms.TextInput(attrs={'class':"form-control", 'placeholder':'Juan'}),
                # 'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Dela Cruz'}),
            }
            
    




