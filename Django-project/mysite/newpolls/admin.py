from dataclasses import field
from django.contrib import admin

from .models import Betting ,Person
# Register your models here.

admin.site.register(Betting)
admin.site.register(Person)