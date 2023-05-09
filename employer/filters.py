import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['icontains'],
            'location': ['icontains'],
            'company_name': ['icontains'],
        }