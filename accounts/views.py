from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm # custom Form
from django.contrib import messages # messages
from django.contrib import auth  # import for auth methods



def register(request):
    hide_nav=True
    hide_category=True
    hide_footer=True
    
    if request.user.is_authenticated: #Condition to set to redirect user that is currently login, if they access the login/ url directly to the address this prevents the Logged in user to access LOGIN page again.
        print('the user is already Login')
        messages.add_message(request,messages.INFO,'You must logout to process registration')
        return redirect('home')

    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()        
            messages.add_message(request, messages.SUCCESS, 'Register Successfully, Please Login..')
            return redirect('login')
        else:
            form = CreateUserForm(request.POST)
            messages.add_message(request, messages.ERROR,f'Register Failed: {str(form.errors.as_text())}')
            
            context ={
                'hide_nav':hide_nav,
                'hide_category':hide_category,
                'hide_footer':hide_footer,
                'form':form,
            }
            return render(request,'auth_template/register.html',context)
            
    # fields = User._meta.get_fields() #Command to get all the fields of a Django builtin Model
    # print(fields)
    
    form = CreateUserForm()
    context ={
        'hide_nav':hide_nav,
        'hide_category':hide_category,
        'hide_footer':hide_footer,
        'form':form
    }
    return render(request,'auth_template/register.html',context)



def login(request):
    hide_nav=True
    hide_category=True
    hide_footer=True
    
    #Toast Message when anonymous use access @login_required pages --> so that this displays Message
    if request.GET.get('next'):
        messages.add_message(request, messages.ERROR, 'You need to LOGIN to perform this action')
        
    if request.user.is_authenticated: #Condition to set to redirect user that is currently login, if they access the login/ url directly to the address this prevents the Logged in user to access LOGIN page again.
        print('the user is already Login')
        messages.add_message(request,messages.SUCCESS,'User is already Logged In')
        return redirect('home')

    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        # print(form)
        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,f'Login Successfully, Welcome {request.user.first_name} ')
            
            # print(request.user.first_name)
            return redirect('home')

        else:
            # print(str(form.errors.as_text()))
            messages.add_message(request,messages.ERROR,str(form.errors.as_text()))
            
            context={
                
                'form':form,
                'hide_nav':hide_nav,
                'hide_category':hide_category,
                'hide_footer':hide_footer,
            }
            return render(request,'auth_template/login.html',context)
        
    else:
        form = AuthenticationForm()
        
        context = {
            'hide_nav':hide_nav,
            'hide_category':hide_category,
            'hide_footer':hide_footer,
            'form':form
        }
        return render(request,'auth_template/login.html',context)
    
  
  
def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.ERROR,'You are now Logout')
    return redirect('login')