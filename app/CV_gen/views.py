import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from CV_gen.forms import CVDataForm

def index(request):
    cv_form = CVDataForm()
    return render(
        request,
        "CV_gen/index.html", {
        "cv_form":cv_form
    })

def cv_list(request):
    return render(request, "CV_gen/list.html")

def submit(request):
    pass