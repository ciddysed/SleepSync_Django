from django.db import models

class ProgressTracking(models.Model):  # Check this name
    progress_id = models.AutoField(primary_key=True)
    date = models.DateField()
    goal = models.CharField(max_length=50)
    progress_value = models.FloatField()

class SleepTrack(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    sleep_duration = models.TimeField()
    sleep_quality = models.CharField(max_length=15)
    sleep_stages = models.CharField(max_length=15)

    schedule_id = models.IntegerField() 

    def __str__(self):
        return f"{self.date} - {self.sleep_quality}"

class User(models.Model):
    userID = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)       # Unique constraint to prevent duplicates
    password = models.CharField(max_length=128)  # Store hashed passwords securely
    preferredWakeTime = models.TimeField()       # Store preferred wake-up time
    sleepGoals = models.TextField()              # Store user's sleep goals

    def __str__(self):
        return self.name  # Display name in Django admin or other views

class RelaxationRoutine(models.Model):
    routineID = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    routineType = models.CharField(max_length=100)
    routineStartTime = models.TimeField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key relationship

    def __str__(self):
        return f"{self.routineType} - {self.userID.name}"  # Display format in Django admin
    
class SmartAlarm(models.Model):
    alarmID = models.AutoField(primary_key=True)  # Auto-incrementing Alarm ID
    alarmTime = models.TimeField()                # Store the time for the alarm

    def __str__(self):
        return f"Alarm at {self.alarmTime}" 