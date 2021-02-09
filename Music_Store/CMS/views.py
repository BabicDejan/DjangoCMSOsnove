from django.shortcuts import render
from .models import Service
# Create your views here.d

def pricing(request):
    """A view of all bands."""
    services = Service.objects.all()
    return render(request, 'cms/pricing.html', {'services':services})