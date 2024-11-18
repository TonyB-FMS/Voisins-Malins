from django.contrib import admin
from .models import Skill, TimeSlot, Task, AuthenticatedUser

admin.site.register(Skill)
admin.site.register(TimeSlot)
admin.site.register(Task)
admin.site.register(AuthenticatedUser)
