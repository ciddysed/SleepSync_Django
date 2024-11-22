from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import ProgressTracking, SleepTrack, User
from .forms import ProgressTrackingForm, SleepTrackForm, UserRegistrationForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import datetime

def landing_page(request):
    return render(request, 'tracker/landing_page.html')

# Progress Tracking CRUD
def progress_list(request):
    progress = ProgressTracking.objects.all()
    return render(request, 'tracker/progress_list.html', {'progress': progress})

def progress_create(request):
    if request.method == "POST":
        form = ProgressTrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressTrackingForm()
    return render(request, 'tracker/progress_form.html', {'form': form})

def progress_update(request, pk):
    progress = ProgressTracking.objects.get(pk=pk)
    if request.method == "POST":
        form = ProgressTrackingForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressTrackingForm(instance=progress)
    return render(request, 'tracker/progress_form.html', {'form': form})

def progress_delete(request, pk):
    progress = ProgressTracking.objects.get(pk=pk)
    if request.method == "POST":
        progress.delete()
        return redirect('progress_list')
    return render(request, 'tracker/progress_confirm_delete.html', {'progress': progress})

# Sleep Track CRUD
def sleeptrack_list(request):
    sleep_tracks = SleepTrack.objects.all()
    return render(request, 'tracker/sleeptrack_list.html', {'sleep_tracks': sleep_tracks})

def sleeptrack_create(request):
    if request.method == "POST":
        form = SleepTrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sleeptrack_list')
    else:
        form = SleepTrackForm()
    return render(request, 'tracker/sleeptrack_form.html', {'form': form})

def sleeptrack_update(request, pk):
    sleep_track = SleepTrack.objects.get(pk=pk)
    if request.method == "POST":
        form = SleepTrackForm(request.POST, instance=sleep_track)
        if form.is_valid():
            form.save()
            return redirect('sleeptrack_list')
    else:
        form = SleepTrackForm(instance=sleep_track)
    return render(request, 'tracker/sleeptrack_form.html', {'form': form})

def sleeptrack_delete(request, pk):
    sleep_track = SleepTrack.objects.get(pk=pk)
    if request.method == "POST":
        sleep_track.delete()
        return redirect('sleeptrack_list')
    return render(request, 'tracker/sleeptrack_confirm_delete.html', {'sleep_track': sleep_track})


# SleepSync/tracker/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# List all users
def user_list(request):
    users = User.objects.all()
    return render(request, 'tracker/user_list.html', {'users': users})

# Create a new user
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'tracker/user_form.html', {'form': form})

# Update an existing user
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'tracker/user_form.html', {'form': form})

# Delete a user
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'tracker/user_confirm_delete.html', {'user': user})


from .models import RelaxationRoutine
from .forms import RelaxationRoutineForm

# List all routines
def routine_list(request):
    routines = RelaxationRoutine.objects.all()
    return render(request, 'tracker/routine_list.html', {'routines': routines})

# Create a new routine
def routine_create(request):
    if request.method == 'POST':
        form = RelaxationRoutineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RelaxationRoutineForm()
    return render(request, 'tracker/routine_form.html', {'form': form})

# Update an existing routine
def routine_update(request, pk):
    routine = get_object_or_404(RelaxationRoutine, pk=pk)
    if request.method == 'POST':
        form = RelaxationRoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RelaxationRoutineForm(instance=routine)
    return render(request, 'tracker/routine_form.html', {'form': form})

# Delete a routine
def routine_delete(request, pk):
    routine = get_object_or_404(RelaxationRoutine, pk=pk)
    if request.method == 'POST':
        routine.delete()
        return redirect('routine_list')
    return render(request, 'tracker/routine_confirm_delete.html', {'routine': routine})

from .models import SmartAlarm
from .forms import SmartAlarmForm

# List all alarms
def alarm_list(request):
    alarms = SmartAlarm.objects.all()
    return render(request, 'tracker/alarm_list.html', {'alarms': alarms})

# Create a new alarm
def alarm_create(request):
    if request.method == 'POST':
        form = SmartAlarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alarm_list')
    else:
        form = SmartAlarmForm()
    return render(request, 'tracker/alarm_form.html', {'form': form})

# Update an existing alarm
def alarm_update(request, pk):
    alarm = get_object_or_404(SmartAlarm, pk=pk)
    if request.method == 'POST':
        form = SmartAlarmForm(request.POST, instance=alarm)
        if form.is_valid():
            form.save()
            return redirect('alarm_list')
    else:
        form = SmartAlarmForm(instance=alarm)
    return render(request, 'tracker/alarm_form.html', {'form': form})

# Delete an alarm
def alarm_delete(request, pk):
    alarm = get_object_or_404(SmartAlarm, pk=pk)
    if request.method == 'POST':
        alarm.delete()
        return redirect('alarm_list')
    return render(request, 'tracker/alarm_confirm_delete.html', {'alarm': alarm})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash the password manually
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate user by email and password
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('landing_page')  # Redirect to a home page or dashboard
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'tracker/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

def sleep_tips(request):
    return render(request, 'tracker/sleep_tips.html')

from datetime import datetime

def get_sleep_tips(wake_time):
    wake_hour = wake_time.hour

    if 5 <= wake_hour <= 9:
        return (
            "Sleep Schedule: Aim to sleep early, between 9:00 PM and 10:30 PM, to ensure 7-9 hours of rest. "
            "Environment: Use blackout curtains and minimize noise to promote deep sleep. "
            "Wind-down Routine: Avoid bright screens and stimulating activities an hour before bedtime. "
            "Diet: Avoid caffeine after mid-afternoon. "
            "Exercise: Morning exercise can help regulate your circadian rhythm."
        )
    elif 11 <= wake_hour <= 13:
        return (
            "Sleep Schedule: Sleep between midnight and 7:00 AM for consistency. Avoid late-night caffeine. "
            "Environment: Keep the room dark and quiet for optimal rest. "
            "Wind-down Routine: Wind down your day with relaxing activities like reading or meditating."
        )
    elif 14 <= wake_hour <= 17:
        return (
            "Sleep Schedule: Aim for 7-8 hours of sleep, starting from midnight. Avoid naps too late in the day. "
            "Environment: Make sure your room is cool and dark. "
            "Diet: Light meals are best before bedtime, and avoid heavy or spicy foods."
        )
    elif 18 <= wake_hour <= 21:
        return (
            "Sleep Schedule: Sleep between 10:00 PM and 6:00 AM for best results. "
            "Environment: Use blackout curtains and noise reduction techniques. "
            "Diet: Avoid excessive caffeine intake in the evening. "
            "Wind-down Routine: Avoid stimulating activities before bed."
        )
    elif 22 <= wake_hour <= 23:
        return (
            "Sleep Schedule: Consider sleeping before midnight to wake up refreshed. "
            "Environment: Minimize light exposure and make your bedroom relaxing. "
            "Wind-down Routine: Begin relaxing at least an hour before sleep."
        )
    else:
        return "Sleep Schedule: Sleep as per your routine, and ensure you maintain consistent wake-up times."


    
def sleep_tips(request):
    # Get the logged-in user
    user = request.user
    
    # Fetch preferredWakeTime from the logged-in user's profile
    preferredWakeTime = user.preferredWakeTime  # assuming preferredWakeTime is stored as a TimeField
    
    # Get sleep tips based on wake time
    sleep_tips = get_sleep_tips(preferredWakeTime)
    
    # Render to the dashboard template
    return render(request, 'tracker/sleep_tips.html', {'sleep_tips': sleep_tips})