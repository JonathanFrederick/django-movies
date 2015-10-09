from django.contrib import admin

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
