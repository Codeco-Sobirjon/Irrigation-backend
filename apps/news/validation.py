from django.core.exceptions import ValidationError
from urllib.parse import urlparse


def validate_http_https(value):
    parsed_url = urlparse(value)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValidationError(f"Схема URL должна быть «http» или «https», но есть '{parsed_url.scheme}'.")