from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # self.assertTrue(response.contentt.startswith(b'<html>'))
    return HttpResponse(b'<html><title>To-Do lists</title></html>')
