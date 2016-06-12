from django.shortcuts import render, redirect
from collection.models import Business
from collection.forms import BusinessForm

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

def edit_business(request, slug):
    business = Business.objects.get(slug=slug)
    # Set the form we're using
    form_class = BusinessForm
    # If we're coming to this view from a submitted form
    if request.method == 'POST':
        # Grab the data from the submitted form
        form = form_class(data=request.POST, instance=business)
        if form.is_valid():
            # Save the new data
            form.save()
            return redirect('business_detail', slug=business.slug)

    # Otherwise just create the form
    else:
        form = form_class(instance=business)

    # And render the template
    return render(request, 'businesses/edit_business.html', {
        'business': business,
        'form': form,
    })
