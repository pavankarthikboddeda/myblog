# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
   text = """<h1>An average Vidya farts at a rate of 100 farts per day. Thats pretty dope. </h1>"""
   return HttpResponse(text)
