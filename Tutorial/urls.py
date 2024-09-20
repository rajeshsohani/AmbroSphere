from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home),  # This maps the root URL to the home view
    path('demo/',demo),
    path('admin01/',admin01,name="ad_min"),
    path('pdftools/',mypdf,name='pdftools'),
    path('deletepage/',deletpage,name='deletpage'),
    path('merge_pdfs/',merge_pdfs,name='merge_pdfs'),
    path('pdf_to_word/',pdf_to_word,name='pdf_to_word'),
    path('word_to_pdf/',word_to_pdf,name='word_to_pdf'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To serve media files during development
