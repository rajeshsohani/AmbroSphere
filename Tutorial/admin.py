from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
#from django_summernote.widgets import SummernoteWidget
from django.db import models


class SubjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

admin.site.register(SubjectModel,SubjectAdmin)



class TopicAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }
admin.site.register(TopicModel,TopicAdmin)


class SubtopiAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

admin.site.register(SubtopicModel,SubtopiAdmin)


