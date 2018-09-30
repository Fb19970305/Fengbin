# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response
from rest_framework.authtoken.models import Token

def login(request):
    return render_to_response('login.html')

def index(request):
    websites = Website.objects.all()
    return render_to_response('index.html', locals())

def add(request):
    return render_to_response('add.html')
