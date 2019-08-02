# from django.contrib import admin
from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config('web_app').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

# Register your models here.
# from .models import Speaker,FollowSpeaker
 
# admin.site.register(Speaker)
# admin.site.register(FollowSpeaker)