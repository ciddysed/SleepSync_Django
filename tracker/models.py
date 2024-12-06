from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import timedelta

class ProgressTracking(models.Model):  # Check this name
    progress_id = models.AutoField(primary_key=True)
    date = models.DateField()
    goal = models.CharField(max_length=50)
    progress_value = models.FloatField()

class SleepTrack(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Correct the import issue
    date = models.DateField()
    sleep_duration = models.FloatField()  # Change to FloatField to store duration in hours
    sleep_quality = models.CharField(max_length=15)
    sleep_stages = models.CharField(max_length=15)
    schedule_id = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.sleep_quality}"

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    userID = models.AutoField(primary_key=True)  # Explicitly define the primary key
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=100, blank=True)
    preferredWakeTime = models.TimeField(null=True, blank=True)
    wake_time = models.TimeField(null=True, blank=True)
    sleepTime = models.TimeField(null=True, blank=True)
    sleepGoals = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # Fix the syntax error

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

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

