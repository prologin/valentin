from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Administration Demi-Finales Prologin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("written-exams/", include("written_exams.urls")),
    path("itw/", include("interviews.urls")),
    path("", include("semifinals.urls")),
    path("social/", include("social_django.urls", namespace="social")),
]
