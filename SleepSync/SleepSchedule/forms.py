from datetime import datetime
from django import forms
from .models import SleepSchedule

class SleepScheduleForm(forms.ModelForm):
    class Meta:
        model = SleepSchedule
        fields = ['user_name', 'sleep_time', 'wake_time', 'date']

    def clean_sleep_time(self):
        time_str = self.cleaned_data['sleep_time']
        if not self.is_valid_time_format(time_str):
            raise forms.ValidationError("Invalid time format. Please use 'HH:MM AM/PM'.")
        return time_str

    def clean_wake_time(self):
        time_str = self.cleaned_data['wake_time']
        if not self.is_valid_time_format(time_str):
            raise forms.ValidationError("Invalid time format. Please use 'HH:MM AM/PM'.")
        return time_str

    def is_valid_time_format(self, time_str):
        try:
            # Check if the time matches the expected 'HH:MM AM/PM' format
            time_str = time_str.strip()
            # Correctly access strptime from datetime
            datetime.strptime(time_str, '%I:%M %p')  # %I for 12-hour hour, %M for minute, %p for AM/PM
            return True
        except ValueError:
            return False
