from django.contrib import admin
from barbershop_server.models import Master
from barbershop_server.models import Service

admin.site.register(Master)
admin.site.register(Service)