from django.shortcuts import render, redirect
from .models import ProgressTracking, SleepTrack
from .forms import ProgressTrackingForm, SleepTrackForm

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