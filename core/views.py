from django.shortcuts import render

# Add an empty line here

def index(request):
    return render(request,'core/index.html')

def contact(request):
    return render(request,'core/contact.html')