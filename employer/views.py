from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm   
from django.contrib import messages

def home(request):
    # add person form
    form = PersonForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home1')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'employer/home1.html', ctx)

def jobdesc(request):
    return (request,'employer/jobdesc.html')