from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Return all Property objects. Use Redis cache to store queryset for 1 hour.
    """
    # Try to get properties from Redis
    properties = cache.get('all_properties')    
    if properties is None:
        properties = list(Property.objects.all())
        # Store in cache for 3600 seconds (1 hour)
        cache.set('all_properties', properties, 3600)
    
    return properties

