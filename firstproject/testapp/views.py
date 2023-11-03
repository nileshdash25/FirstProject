from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Wellcome(req):
    s='<h1>hello nilesh</h1>'
    return HttpResponse(s)
 