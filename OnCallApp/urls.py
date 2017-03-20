'''
Created on 20 Mar 2017

@author: fabien
'''

from django.conf.urls import url

import OnCallApp.views

urlpatterns = [
    url(r'^oncall/$', OnCallApp.views.home, name='home'),
]
