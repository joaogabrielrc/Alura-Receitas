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

def register_user(form):
  username = form.data.get('username')    
  first_name = form.data.get('fname')        
  last_name = form.data.get('lname')        
  user = form.save()
  user.email = username
  user.first_name = first_name
  user.last_name = last_name
  user.is_staff = True    
  user.save()        
  return user


@login_required
def register_view(request):
  context = {}  
  if request.method == 'POST':
    credentials = {
      'username': request.POST.get('username'),
      'password1': request.POST.get('password1'),
      'password2': request.POST.get('password2'),
      'fname': request.POST.get('fname'),
      'lname': request.POST.get('lname')     
    }
    form = UserCreationForm(credentials)  
    if form.is_valid():            
      register_user(form)                  
      return redirect('/login/')
    else:    
      context['errors'] = get_form_errors(form)             
  return render(request, 'pages/register.html', context)
