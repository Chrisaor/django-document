from django.contrib import admin

# Register your models here.
from multi_table.models import Place, Restaurant

admin.site.register(Place)
admin.site.register(Restaurant)