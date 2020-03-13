from django.contrib import admin

# Register your models here.
from .models import Kudos

# admin.site.register(Kudos)
@admin.register(Kudos)
class KudosAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', )