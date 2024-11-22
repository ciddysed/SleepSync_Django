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

    # Early Morning (5 AM - 9 AM)
    if 5 <= wake_hour <= 9:
        return {
            'schedule': {
                'title': 'Optimal Sleep Schedule',
                'icon': 'clock',
                'tips': ['Aim to sleep early, between 9:00 PM and 10:30 PM', 'Ensure 7-9 hours of quality rest']
            },
            'environment': {
                'title': 'Sleep Environment',
                'icon': 'moon',
                'tips': ['Use blackout curtains', 'Minimize ambient noise', 'Keep room temperature cool']
            },
            'routine': {
                'title': 'Evening Routine',
                'icon': 'book',
                'tips': ['Avoid bright screens an hour before bed', 'Limit stimulating activities']
            },
            'diet': {
                'title': 'Dietary Guidelines',
                'icon': 'coffee',
                'tips': ['Avoid caffeine after mid-afternoon', 'Light dinner 2-3 hours before bed']
            },
            'exercise': {
                'title': 'Exercise Recommendations',
                'icon': 'activity',
                'tips': ['Morning exercise helps regulate circadian rhythm', 'Complete workouts at least 3 hours before bed']
            }
        }

    # Late Morning (11 AM - 1 PM)
    elif 11 <= wake_hour <= 13:
        return {
            'schedule': {
                'title': 'Sleep Schedule',
                'icon': 'clock',
                'tips': ['Sleep between midnight and 7:00 AM', 'Maintain consistent sleep times']
            },
            'environment': {
                'title': 'Room Setup',
                'icon': 'moon',
                'tips': ['Keep the room dark and quiet', 'Use white noise if needed']
            },
            'routine': {
                'title': 'Relaxation Routine',
                'icon': 'book',
                'tips': ['Read before bed', 'Practice meditation or deep breathing']
            }
        }

    # Afternoon (2 PM - 5 PM)
    elif 14 <= wake_hour <= 17:
        return {
            'schedule': {
                'title': 'Sleep Duration',
                'icon': 'clock',
                'tips': ['Aim for 7-8 hours of sleep', 'Start bedtime routine from midnight', 'Avoid late afternoon naps']
            },
            'environment': {
                'title': 'Room Conditions',
                'icon': 'moon',
                'tips': ['Maintain cool room temperature', 'Ensure complete darkness']
            },
            'diet': {
                'title': 'Evening Diet',
                'icon': 'coffee',
                'tips': ['Choose light meals before bed', 'Avoid spicy and heavy foods']
            }
        }

    # Evening (6 PM - 9 PM)
    elif 18 <= wake_hour <= 21:
        return {
            'schedule': {
                'title': 'Sleep Timing',
                'icon': 'clock',
                'tips': ['Sleep between 10:00 PM and 6:00 AM', 'Follow a consistent schedule']
            },
            'environment': {
                'title': 'Sleep Environment',
                'icon': 'moon',
                'tips': ['Use blackout curtains', 'Implement noise reduction']
            },
            'diet': {
                'title': 'Evening Habits',
                'icon': 'coffee',
                'tips': ['Avoid evening caffeine', 'Stay hydrated during the day']
            },
            'routine': {
                'title': 'Night Routine',
                'icon': 'book',
                'tips': ['Avoid stimulating activities', 'Practice calming exercises']
            }
        }

    # Night (10 PM - 11 PM)
    elif 22 <= wake_hour <= 23:
        return {
            'schedule': {
                'title': 'Night Schedule',
                'icon': 'clock',
                'tips': ['Sleep before midnight', 'Plan for complete sleep cycles']
            },
            'environment': {
                'title': 'Bedroom Setup',
                'icon': 'moon',
                'tips': ['Minimize light exposure', 'Create a relaxing atmosphere']
            },
            'routine': {
                'title': 'Pre-sleep Routine',
                'icon': 'book',
                'tips': ['Begin relaxing an hour before sleep', 'Practice gentle stretching']
            }
        }

    # Default/Other Hours
    else:
        return {
            'schedule': {
                'title': 'General Guidelines',
                'icon': 'clock',
                'tips': ['Maintain consistent wake-up times', 'Adjust sleep schedule gradually']
            }
        }


    
def sleep_tips(request):
    # Get the logged-in user
    user = request.user
    
    # Fetch preferredWakeTime from the logged-in user's profile
    preferredWakeTime = user.preferredWakeTime
    
    # Get structured sleep tips based on wake time
    tips = get_sleep_tips(preferredWakeTime)
    
    # Create context with user info and structured tips
    context = {
        'user': user,
        'preferredWakeTime': preferredWakeTime,
        'tips': tips,  # This now contains the structured dictionary of tips
        'categories': {
            'schedule': {
                'name': 'Sleep Schedule',
                'icon': '''<svg viewBox="0 0 24 24">
                    <path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm.5-13H11v6l5.2 3.2.8-1.3-4.5-2.7V7z"/>
                </svg>'''
            },
            'environment': {
                'name': 'Sleep Environment',
                'icon': '''<svg viewBox="0 0 24 24">
                    <path d="M20 4v16H4V4h16m2-2H2v20h20V2zm-8 9h-2V9h2v2z"/>
                </svg>'''
            },
            'routine': {
                'name': 'Evening Routine',
                'icon': '''<svg viewBox="0 0 24 24">
                    <path d="M17.66 8L12 2.35 6.34 8A8.02 8.02 0 004 13.64c0 2 .78 4.11 2.34 5.67a7.99 7.99 0 0011.32 0c1.56-1.56 2.34-3.67 2.34-5.67A8.02 8.02 0 0017.66 8zM6 14c.01-2 .62-3.27 1.76-4.4L12 5.27l4.24 4.38C17.38 10.77 17.99 12 18 14H6z"/>
                </svg>'''
            },
            'diet': {
                'name': 'Diet Guidelines',
                'icon': '''<svg viewBox="0 0 24 24">
                    <path d="M20 3H4v10c0 2.21 1.79 4 4 4h6c2.21 0 4-1.79 4-4v-3h2c1.11 0 2-.89 2-2V5c0-1.11-.89-2-2-2zm0 5h-2V5h2v3zM4 19h16v2H4z"/>
                </svg>'''
            },
            'exercise': {
                'name': 'Exercise Tips',
                'icon': '''<svg viewBox="0 0 24 24">
                    <path d="M13.49 5.48c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm-3.6 13.9l1-4.4 2.1 2v6h2v-7.5l-2.1-2 .6-3c1.3 1.5 3.3 2.5 5.5 2.5v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1l-5.2 2.2v4.7h2v-3.4l1.8-.7-1.6 8.1-4.9-1-.4 2 7 1.4z"/>
                </svg>'''
            }
        }
    }
    
    # Render the template with the structured context
    return render(request, 'tracker/sleep_tips.html', context)