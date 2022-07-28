from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm

from alura_receita.views import register_user


class UserAuthenticationTest(TestCase):
  user = None
  username = 'joao@mail.com'  
  password1 = 'Password.123'
  password2 = password1    
  first_name = 'João Gabriel'
  last_name = 'Cardoso'  

  def setUp(self) -> None:
    credentials = {
      'username': self.username,
      'password1': self.password1,
      'password2': self.password2,
      'fname': self.first_name,
      'lname': self.last_name     
    }
    form = UserCreationForm(credentials)    
    self.user = register_user(form)     

  def test_user_registration(self) -> None:    
    self.assertTrue(self.user.is_authenticated)
  
  def test_user_registration_name(self) -> None:        
    full_name = f'{self.first_name} {self.last_name}'        
    self.assertEqual(full_name, self.user.get_full_name())

  def test_email_username_equality(self) -> None:        
    email = self.user.email
    username = self.user.username
    self.assertEqual(email, username)
