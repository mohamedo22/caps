from django.contrib import admin
from .models import flats , flat_images , users , admins_s
# Register your models here.
admin.site.register(flats)
admin.site.register(flat_images)
admin.site.register(users)
admin.site.register(admins_s)
