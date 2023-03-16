from django.contrib import admin
from .models import Transacao, Bitcoin, Investimento

admin.site.register(Transacao)
admin.site.register(Bitcoin)
admin.site.register(Investimento)
