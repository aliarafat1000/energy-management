"""
Production settings
"""
from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["example.com"])

# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
