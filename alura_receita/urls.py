from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
  LogoutView,
  LoginView,
  RegisterView
)


urlpatterns = [
  path('admin/', admin.site.urls),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', include('receitas.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
