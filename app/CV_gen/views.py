import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    return render(request, "CV_gen/index.html")

def cv_list(request):
    return render(request, "CV_gen/list.html")

def submit(request):
    pass