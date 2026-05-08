from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import BlogUser
from django import forms


# from crispy_forms.helper import FormHelper



class CreateUserForm(UserCreationForm):
    
    # def __init__(self, *args, **kwargs):
    #     super(CreateUserForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_show_labels = True 
    
    
    #This prevents loading the helptext of the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # # Remove help texts
        self.fields['first_name'].help_text = ''
        self.fields['last_name'].help_text = ''
        
        # self.fields['username'].help_text = ''
        # self.fields['password1'].help_text = ''
        # self.fields['password2'].help_text = ''
        
        # # Remove Label
        # self.fields['username'].label = ''
        # self.fields['password1'].label = ''
        # self.fields['password2'].label = ''
        
        """
        NOTE: to remove the * of a field that is being default for REQUIRED field in Django Crispyforms, you need to manually set this to you Css file.
        
        .asteriskField {
                display: none;
            }

        """
        
        
    class Meta:
        model=User
        # fields=['username','password1','password2']
        fields=['first_name','last_name','email','username','password1','password2']

        widgets={
            'password1':forms.PasswordInput(attrs={'class':"form-control"}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email@example.com'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':"form-control", 'placeholder':'Juan'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Dela Cruz'}),
        }
            
    

