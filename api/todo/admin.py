from django.contrib import admin
from .models import Todo


admin.site.register(Todo)#tell it to the site admin we regestering that model so that it can appear on the admin side


