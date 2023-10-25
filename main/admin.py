from django.contrib import admin
from .models import * 
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Products)
admin.site.register(Order)

admin.site.site_header = 'Glamourloom'