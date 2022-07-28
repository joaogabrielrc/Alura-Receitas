from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.views import View


User = get_user_model()

class LogoutView(View):
  def get(self, request) -> HttpResponse:
    logout(request)
    return redirect('/login/')


class LoginView(View):
  def get(self, request) -> HttpResponse:
    return render(request, 'pages/login.html')

  def post(self, request) -> HttpResponse:    
    credentials = request.POST
    form = AuthenticationForm(request, data=credentials)      
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('/')          
    return render(request, 'pages/login.html')


class RegisterView(View):
  def get(self, request) -> HttpResponse:
    return render(request, 'pages/register.html')

  def post(self, request) -> HttpResponse:
    context = {}    
    credentials = request.POST
    form = UserCreationForm(credentials)
    if form.is_valid():               
      self.__register_user(form)  
      return redirect('/login/')  

    context['errors'] = self.__get_form_errors(form)       
    return render(request, 'pages/register.html', context)
    

  def __register_user(self, form: UserCreationForm) -> None:
    username = form.cleaned_data.get('username')    
    first_name = form.data.get('fname')        
    last_name = form.data.get('lname')    
    user = form.save(commit=False) 
    user.email = username
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = True    
    user.save() 

  def __get_form_errors(self, form: UserCreationForm) -> list:
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
