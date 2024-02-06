from django.contrib import admin
# import your models here
from .models import Bird, Feeder, Perch

# Register your models here
admin.site.register(Bird)
admin.site.register(Feeder)
admin.site.register(Perch)