from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import django_filters
from accounts.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from employer.models import Job
from employer.filters import JobFilter

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def contactus(request):
    return render(request, 'contactus.html')

def about(request):
    return render(request, 'about.html')
def index(request):
    jobs = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=jobs)
    ctx = {
        'job_filter': job_filter,
    }
    return render(request, 'index.html', ctx)
@login_required
def dashboard(request):
    # check if user has a profile set
    try:
        profile = Profile.objects.get(user=request.user)
        return redirect('/jobseeker/home/')
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')


@login_required
def job(request, id):
    job = get_object_or_404(Job, pk=id)
    ctx = {
        'job': job,
    }
    return render(request, 'job.html', ctx)
