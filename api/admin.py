from django.contrib import admin
from .models import Account, InternalTransfer, ExternalTransfer
# Register your models here.

admin.site.register(Account)
admin.site.register(InternalTransfer)
admin.site.register(ExternalTransfer)
