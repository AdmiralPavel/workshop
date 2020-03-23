
from django.contrib import admin

from barbershop_server.models import Master, Review, Session
from barbershop_server.models import Service

admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Session)
admin.site.register(Review)
