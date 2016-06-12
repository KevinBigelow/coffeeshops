from django.shortcuts import render
from collection.models import Business

def index(request):
    businesses = Business.objects.all()
    # Passing the variable to the view
    return render(request, 'index.html', {
        'business': businesses,
    })

def business_detail(request, slug):
    # Grab the object
    business = Business.objects.get(slug=slug)
    # and pass it to the template!
    return render(request, 'businesses/business_detail.html', {
        'business': business,
    })
