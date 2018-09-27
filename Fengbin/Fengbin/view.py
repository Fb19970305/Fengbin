# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response

def login(request):
    return render_to_response('login.html')

def index(request):
    websites = Website.objects.all()
    print(websites)
    return render_to_response('index.html', locals())
