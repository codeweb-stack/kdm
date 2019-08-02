from django.contrib import admin

# Register your models here.
from .models import Speaker,Program,sponsors,pastspeakers,post

admin.site.register(Speaker)
admin.site.register(Program)
admin.site.register(sponsors)
admin.site.register(pastspeakers)
admin.site.register(post)
