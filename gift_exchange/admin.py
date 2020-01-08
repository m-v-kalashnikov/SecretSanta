from django.contrib import admin
from gift_exchange.models import *


@admin.register(GiftExchange)
class GiftExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'gift_exchange')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass
