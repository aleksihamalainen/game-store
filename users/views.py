# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')