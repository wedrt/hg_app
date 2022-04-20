from django.contrib import admin

from .models import *

admin.site.register(Package)
admin.site.register(Point)
admin.site.register(Player)
admin.site.register(Kill)
admin.site.register(Message)
