from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppBlog/index.html',
        context=contexto,
    )
    return http_response

def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppBlog/about.html',
        context=contexto,
    )
    return http_response