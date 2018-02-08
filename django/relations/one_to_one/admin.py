from django.contrib import admin
from .models import Place, Waiter, Restaurant

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)