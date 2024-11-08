from django.db import models

class SleepSchedule(models.Model):
    user_name = models.CharField(max_length=100)
    sleep_time = models.CharField(max_length=10)  # 'HH:MM AM/PM' format
    wake_time = models.CharField(max_length=10)  # 'HH:MM AM/PM' format
    date = models.DateField()

    def __str__(self):
        return f"{self.user_name}'s Schedule on {self.date}"
