from django.contrib import admin
from .models import ProgressTracking, SleepTrack, User, RelaxationRoutine, SmartAlarm

admin.site.register(ProgressTracking)
admin.site.register(SleepTrack)
admin.site.register(User)
admin.site.register(RelaxationRoutine)
admin.site.register(SmartAlarm)