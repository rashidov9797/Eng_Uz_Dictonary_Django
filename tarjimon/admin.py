from django.contrib import admin
from .models import Lugatlar

# Register your models here.

class LugatAdmin(admin.ModelAdmin):
  list_display = ['english','uzbek']
admin.site.register(Lugatlar,LugatAdmin)  