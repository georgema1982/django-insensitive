'''
Created on 2011-06-12

@author: George
'''
from django.conf.urls.defaults import *
from insensitive.views import login

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='auth_login_case_insensitive'),
)

