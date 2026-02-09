DEBUG = False
HAS_DDT = False

# CSRF Protection: Require HTTPS for CSRF cookie transmission
# This setting ensures the CSRF cookie is only sent over secure (HTTPS) connections
CSRF_COOKIE_SECURE = True

# ManifestStaticFilesStorage adds MD5 hash to filenames for cache busting
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}
