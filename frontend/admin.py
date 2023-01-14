from django.contrib import admin

# Register your models here.
from frontend.models import BTCUSExchange, Task

admin.site.register(BTCUSExchange)
admin.site.register(Task)
