from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property

# This view lists all properties and caches the result for 60 seconds
@cache_page(60)  # cache duration in seconds
def property_list(request):
    properties = Property.objects.all()  # fetch all properties from DB
    return render(request, "properties/list.html", {"properties": properties})

