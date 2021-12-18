from django.contrib import admin

# Register your models here.
from .models import  Helpline, CustomUser

admin.site.register(CustomUser)
admin.site.register(Helpline)
