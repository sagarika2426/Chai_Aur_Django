from django.shortcuts import render

# Create your views here.
def app1_home(request):
    return render(request, './website/home.html')