from pyoupyou.settings.common import *
import os

DEBUG = True

# SECRET_KEY must be provided via environment variable for security
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError(
        "SECRET_KEY environment variable must be set. "
        "For development, generate one using: python manage.py generate_secret_key"
    )

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}

# flag to add Django Debug Toolbar to urls.py
HAS_DDT = True

INSTALLED_APPS += ["debug_toolbar", "debug_toolbar_user_panel"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar_user_panel.panels.UserPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]

DEBUG_TOOLBAR_CONFIG = {"JQUERY_URL": "{}bootstrap/js/jquery.min.js".format(STATIC_URL)}

# needed by django debug toolbar
INTERNAL_IPS = ["127.0.0.1"]

SITE_HOST = "http://localhost:8000"
LOGIN_URL = "/admin/login/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"pyoupyou": {"handlers": ["console"], "level": os.getenv("DJANGO_LOG_LEVEL", "INFO")}},
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MAIL_HR = "hr@enioka.com"
MAIL_FROM = "pyoupyou@enioka.com"

SEEKUBE_SOURCE_ID = 5
SECRET_ANON_SALT = "dev-salt"

FORM_WEB_HOOK_PREFIX = "dev"
