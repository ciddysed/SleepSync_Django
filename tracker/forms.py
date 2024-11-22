from django import forms
from .models import ProgressTracking, SleepTrack, User, RelaxationRoutine, SmartAlarm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

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

class RelaxationRoutineForm(forms.ModelForm):
    class Meta:
        model = RelaxationRoutine
        fields = ['routineType', 'routineStartTime', 'userID']
        widgets = {
            'routineStartTime': forms.TimeInput(attrs={'type': 'time'}),
        }

class SmartAlarmForm(forms.ModelForm):
    class Meta:
        model = SmartAlarm
        fields = ['alarmTime']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'name', 'preferredWakeTime', 'sleepGoals']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Password input field

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'preferredWakeTime', 'sleepGoals']
        widgets = {
            'preferredWakeTime': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)