from django.contrib import admin
from .models import *
from .models import CustomerUser
# Register your models here.

class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'pwd', 'fname', 'lname', 'contact', 'email', 'address', 'city', 'image', 'usertype')

admin.site.register(CustomerUser,CustomerUserAdmin)