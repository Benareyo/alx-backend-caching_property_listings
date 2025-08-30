from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Connect to Redis, retrieve keyspace_hits and keyspace_misses,
    calculate hit ratio, log and return metrics as a dictionary.
    """
    try:
        # Connect to Redis via django_redis
        redis_conn = get_redis_connection("default")
        
        # Get Redis stats
        info = redis_conn.info()
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        
        # Calculate hit ratio safely
        total = hits + misses
        hit_ratio = hits / total if total > 0 else 0.0

        # Create metrics dictionary
        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio,
        }

        # Log metrics
        logger.info(f"Redis cache metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Failed to retrieve Redis metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0.0
        }

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

