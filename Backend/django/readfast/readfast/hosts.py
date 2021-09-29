from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'api', 'readfast.api_urls', name='api'),
    host(r'search', 'search.urls', name='search'),
    host(r'(www|)', settings.ROOT_URLCONF, name='www'),
)