from django.contrib import admin

from api.models import Message
from api.models import ApiUser

admin.site.register(Message)
admin.site.register(ApiUser)
