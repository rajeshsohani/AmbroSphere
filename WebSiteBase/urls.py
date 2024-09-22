from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('Tutorial/', include('Tutorial.urls')),  # Include the `urls.py` of your `Tutorial` app
    path("summernote/", include("django_summernote.urls")),
    path('', lambda request: redirect('Tutorial/demo/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To serve media files during development
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
