from django.contrib import admin
from .models import Auto
from .models import User
from .models import DriverLicense
from .models import Usage
# Register your models here.

admin.site.register(Auto)
admin.site.register(User)
admin.site.register(DriverLicense)
admin.site.register(Usage)