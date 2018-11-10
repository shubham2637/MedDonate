from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doner)
admin.site.register(Collector)
admin.site.register(Acceptor)
admin.site.register(vehicle)
admin.site.register(assigned_vehicle)
admin.site.register(medicine)
admin.site.register(medicine_ledger)
admin.site.register(job)
