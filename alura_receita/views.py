import re

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def login_view(request):
  return render(request, 'pages/login.html')


@login_required
def logout_view(request):
  pass


def get_form_errors(form) -> list:
  errors = []  
  username_errors = form.errors.get_json_data().get('username')
  password_errors = form.errors.get_json_data().get('password2')

  if username_errors:    
    for error in username_errors:
      errors.append(error['message'])      
  
  if password_errors:    
    for error in password_errors:
      errors.append(error['message'])

  return errors


@login_required
def register_view(request):
  context = {}
  form = UserCreationForm(request.POST or None)  
  if form.is_valid():    
    username = request.POST.get('username')    
    first_name = request.POST.get('fname')        
    last_name = request.POST.get('lname')        
    user = form.save()
    user.email = username
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = True    
    user.save()
    return redirect('/login/')
  else:    
    context['errors'] = get_form_errors(form)             
  return render(request, 'pages/register.html', context)
