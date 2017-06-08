# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.

def hello(request):
   return render(request, 'home.html')
