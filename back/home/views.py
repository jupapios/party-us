# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def index(request):
    data = {}
    return render_to_response('home/index.html', data)