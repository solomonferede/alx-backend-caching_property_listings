from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get from cache first
    properties = cache.get('all_properties')
    if properties is None:
        # If not in cache, query the database
        properties = list(Property.objects.all().values())
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    return properties
