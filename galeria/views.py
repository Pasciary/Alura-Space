from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao nosso espaço de fotos</p>'.encode('utf-8'), content_type='text/html; charset=utf-8')