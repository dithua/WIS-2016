from django.contrib import admin

# Register your models here.

from django.contrib import admin
# Register your models here.
from . models import Posts,Comments

admin.site.register(Posts)
admin.site.register(Comments)