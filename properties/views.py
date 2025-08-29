from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property
from django.http import JsonResponse
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache the whole view for 15 minutes
def property_list(request):
    properties = get_all_properties()  # Fetch using low-level cache
    data = [{"id": p.id, "name": p.name} for p in properties]  # Convert to JSON-friendly format
    return JsonResponse({"data": data})
    
    # Convert to a list of dictionaries
    data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": p.price,
            "location": p.location,
            "created_at": p.created_at
        }
        for p in properties
    ]
    
    return JsonResponse({"data": data})
