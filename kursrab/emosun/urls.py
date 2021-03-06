"""
Definition of urls for emosun.
"""

from datetime import datetime
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.home, name='home'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  path('login/',
      LoginView.as_view
      (
        template_name='app/login.html',
        authentication_form=forms.BootstrapAuthenticationForm,
        extra_context=
        {
          'title': 'Log in',
          'year' : datetime.now().year,
        }
      ),
      name='login'),
  path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
  path('admin/', admin.site.urls),
  path('registration/', views.registration, name='registration'),
  path('blog/', views.blog, name='blog'),
  path('blog/<postnum>/', views.blogpost, name='blogpost'),
  path('shop/', include('shop.urls'), name='shop'),
  path('cart/', include('cart.urls'), name='cart'),
  path('order/', include('order.urls'), name='order'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)