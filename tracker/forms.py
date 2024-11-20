from django import forms
from .models import ProgressTracking, SleepTrack, User, RelaxationRoutine, SmartAlarm

class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['date', 'goal', 'progress_value']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SleepTrackForm(forms.ModelForm):
    class Meta:
        model = SleepTrack
        fields = ['date', 'sleep_duration', 'sleep_quality', 'sleep_stages', 'schedule_id']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'sleep_duration': forms.TimeInput(attrs={'type': 'time'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'preferredWakeTime', 'sleepGoals']

class RelaxationRoutineForm(forms.ModelForm):
    class Meta:
        model = RelaxationRoutine
        fields = ['routineType', 'routineStartTime', 'userID']

class SmartAlarmForm(forms.ModelForm):
    class Meta:
        model = SmartAlarm
        fields = ['alarmTime']