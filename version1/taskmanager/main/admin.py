from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


admin.site.register(Profile)
admin.site.register(Forum)