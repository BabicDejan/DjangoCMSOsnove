from django.shortcuts import render
from .models import  Band
# Create your views here.
def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all()
    #first_band = Band.objects.first()
    return render(request, 'bands/band_listing.html', {'bands': bands})
def band_detail(request,band_id):
    """A view of a band detail"""
    band = Band.objects.get(pk=band_id) # SELECT * FROM BAND WHERE ID = BAND_ID
    #first_band = Band.objects.first()
    return render(request, 'bands/band_detail.html', {'band': band})
def homepage(request):
    """A view of all bands."""
    return render(request, 'bands/homepage.html', {})
def band_search(request):
    """A search for a band"""
    queried_band = request.GET['q']
    band = None
    try:
        band = Band.objects.get(name=queried_band) # SELECT * FROM BAND WHERE NAME = query
        queried_band_exists = True
        print(queried_band_exists)
    except:
        queried_band_exists = False
    
    #first_band = Band.objects.first()
    return render(request, 'bands/band_searched.html', {'band': band, 'results': queried_band_exists})
