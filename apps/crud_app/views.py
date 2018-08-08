from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_index_page(request):
    return render(request,'index.html');
def get_about_page(request):
    return render(request,'about.html');
def register_user(request):
    if(request.method == 'GET'):
        return render(request, 'register.html');
    else:
        return HttpResponse('It is a post request');
