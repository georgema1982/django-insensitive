'''
Created on 2011-07-20

@author: George
'''
from django.contrib.auth import views as auth_views, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm

def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm):
    return auth_views.login(request, template_name, redirect_field_name, authentication_form)
