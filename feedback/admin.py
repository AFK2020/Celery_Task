from django.contrib import admin
from .models import Subscriber, Newsletter
# Register your models here.

admin.site.register(Newsletter)
admin.site.register(Subscriber)