from django.shortcuts import render

# Create your views here.
def all_ninja(request):
    return render(request, 'ninja/all_ninja.html')