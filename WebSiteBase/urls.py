from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Tutorial/', include('Tutorial.urls')),  # Include the `urls.py` of your `Tutorial` app
    path("summernote/", include("django_summernote.urls")),
    path('', lambda request: redirect('Tutorial/demo/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To serve media files during development
