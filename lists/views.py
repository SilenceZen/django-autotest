from django.shortcuts import render


# Create your views here.
def home_page(request):
    # self.assertTrue(response.contentt.startswith(b'<html>'))
    return render(request, 'home.html')
