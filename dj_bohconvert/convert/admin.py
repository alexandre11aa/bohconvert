from django.contrib import admin
from .models import Convert

@admin.register(Convert)
class ConversaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'decimal', 'precisao', 'binario', 'octal', 'hexadecimal', 'data_hora')
    search_fields = ('decimal', 'precisao', 'binario', 'octal', 'hexadecimal')
