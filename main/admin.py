from django.contrib import admin
from .models import * 

admin.site.register(Products)

admin.site.site_header = 'Glamourloom'