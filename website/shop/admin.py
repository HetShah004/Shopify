from django.contrib import admin
from shop import models
admin.site.register(models.Item)
admin.site.register(models.Order)