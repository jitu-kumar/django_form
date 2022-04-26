from django.contrib import admin
from .models import JeetuModel
# Register your models here.


@admin.register(JeetuModel)
class JeetuModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'img']
