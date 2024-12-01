from django.shortcuts import render
from .models import Author, Material

def home(request):
    return render(request, 'main/home.html')

def about(request):
    authors = Author.objects.all()
    return render(request, 'main/about.html', {'authors': authors})

def materials(request):
    materials = Material.objects.all()
    return render(request, 'main/materials.html', {'materials': materials})

def resources(request):
    return render(request, 'main/resources.html')
