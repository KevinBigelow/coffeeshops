from django.shortcuts import render
from collection.models import business

# Create your views here.
def index(request):
    businesses = business.objects.all()
    # Passing the variable to the view
    return render(request, 'index.html', {
        'business': businesses,
    })
