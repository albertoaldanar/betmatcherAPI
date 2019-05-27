"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include(("cride.users.urls", "users"), namespace ="users")),
    path("", include(("cride.events.urls", "events"), namespace ="events")),
    path("", include(("cride.matches.urls", "matches"), namespace ="matches")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
