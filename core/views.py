from django.shortcuts import render

# Add an empty line here

def index(request):
    return render(request,'core/index.html')

