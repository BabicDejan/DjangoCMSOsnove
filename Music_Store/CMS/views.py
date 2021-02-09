from django.shortcuts import render
from .models import Service,FAQ
from .forms import FAQForm
# Create your views here.d

def pricing(request):
    """A view of all bands."""
    services = Service.objects.all()

    form = FAQForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'cms/pricing.html', {'services':services,'form':form})

def homepage(request):
    """A view of all bands."""
    faqs = FAQ.objects.all()
    return render(request, 'cms/homepage.html', {'faqs':faqs})
def add_faq(request):
    return render(request, 'cms/thanks.html', {})
