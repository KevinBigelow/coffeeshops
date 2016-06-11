from django.shortcuts import render

# Create your views here.
def index(request):
    # Defining the variable
    number = 6
    name = 'kevin bigelow'
    # Passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
        'name': name,
    })
