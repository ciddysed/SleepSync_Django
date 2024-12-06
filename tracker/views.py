from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from .models import ProgressTracking, SleepTrack, User
from .forms import ProgressTrackingForm, SleepTrackForm, UserRegistrationForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.template.loader import render_to_string


@login_required
def profile_view(request):
    return render(request, 'tracker/profile.html', {'user': request.user})

def admin_dashboard(request):
    """Render the admin dashboard with user list."""
    # Get all users from your custom User model
    users = User.objects.all()
    return render(request, 'tracker/admin_dashboard.html', {'users': users})

def profile(request):
    user = request.user
    return render(request, 'tracker/profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user 

    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        preferred_wake_time = request.POST.get('preferredWakeTime')
        sleep_goals = request.POST.get('sleepGoals')
        profile_picture = request.FILES.get('profile_picture')
        sleep_time = request.POST.get('sleepTime')

        user.first_name = first_name
        user.last_name = last_name
        user.preferredWakeTime = preferred_wake_time
        user.sleepGoals = sleep_goals
        user.sleepTime = sleep_time

        if profile_picture:
            user.profile_picture = profile_picture

        user.save() 

        return redirect('profile')

    else:
        return render(request, 'tracker/edit_profile.html', {'user': user})

def landing_page(request):
    return render(request, 'tracker/landing_page.html')

def about(request):
    return render(request, 'tracker/about.html')

def contacts(request):
    return render(request, 'tracker/contacts.html')

def features(request):
    return render(request, 'tracker/features.html')

def privacy_policy(request):
    return render(request, 'tracker/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'tracker/terms_of_service.html')

def progress_list(request):
    user = request.user
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



from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'tracker/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'tracker/user_form.html', {'form': form})

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

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'tracker/user_confirm_delete.html', {'user': user})


from .models import RelaxationRoutine
from .forms import RelaxationRoutineForm

def routine_list(request):
    routines = RelaxationRoutine.objects.all()
    return render(request, 'tracker/routine_list.html', {'routines': routines})

def routine_create(request):
    if request.method == 'POST':
        form = RelaxationRoutineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RelaxationRoutineForm()
    return render(request, 'tracker/routine_form.html', {'form': form})

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

def routine_delete(request, pk):
    routine = get_object_or_404(RelaxationRoutine, pk=pk)
    if request.method == 'POST':
        routine.delete()
        return redirect('routine_list')
    return render(request, 'tracker/routine_confirm_delete.html', {'routine': routine})

from .models import SmartAlarm
from .forms import SmartAlarmForm

def alarm_list(request):
    alarms = SmartAlarm.objects.all()
    return render(request, 'tracker/alarm_list.html', {'alarms': alarms})

def alarm_create(request):
    if request.method == 'POST':
        form = SmartAlarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alarm_list')
    else:
        form = SmartAlarmForm()
    return render(request, 'tracker/alarm_form.html', {'form': form})

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
            user.password = make_password(form.cleaned_data['password']) 
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})

# Login View
def landing(request):
    return render(request, 'tracker/landing.html')

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

def edit_wake_time(request):
    user = User.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('sleep_tips')  # Redirect to the desired page
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_wake_time.html', {'form': form})

@login_required
def update_wake_time(request):
    if request.method == 'POST':
        wake_time = request.POST.get('wake_time')
        if (wake_time):
            user = request.user
            user.preferredWakeTime = wake_time
            user.save()
            return redirect('sleep_tips')  # Redirect to the sleep tips page or wherever appropriate.
    return redirect('sleep_tips')  # Redirect in case of invalid form submission or GET request.

def progress_bar_view(request):
    return render(request, 'tracker/progress_bar.html')

def record_sleep(request):
    return render(request, 'tracker/RecordSleep.html')

import logging

logger = logging.getLogger(__name__)

def get_sleep_effects(sleep_duration):
    if sleep_duration < 4:
        return {
            'range': '<4 hours',
            'effects': [
                'Severe fatigue: Persistent exhaustion impacts daily functioning.',
                'Cognitive impairment: Poor decision-making, focus, and memory.',
                'Immune suppression: Higher susceptibility to colds, flu, and infections.',
                'Hormonal imbalance: Increased cortisol (stress hormone) and reduced growth hormone production.'
            ],
            'tasks': [
                'Power Naps: Take short naps (20–30 mins) to temporarily improve alertness.',
                'Stress Reduction: Practice light stretching, meditation, or progressive muscle relaxation.',
                'Limit Stimulants: Avoid caffeine, nicotine, and heavy meals late at night.',
                'Hydration: Stay hydrated but avoid large quantities of water right before bed.'
            ]
        }
    elif 4 <= sleep_duration < 6:
        return {
            'range': '4-6 hours',
            'effects': [
                'Memory issues: Short-term and working memory are significantly impaired.',
                'Mood instability: Increased irritability, anxiety, and depressive symptoms.',
                'Slower reaction times: Greater risk of accidents due to impaired motor coordination.',
                'Physical fatigue: Weakness and reduced stamina during physical activities.'
            ],
            'tasks': [
                'Deep Breathing & Yoga: Engage in calming exercises to manage stress levels.',
                'Daylight Exposure: Spend time in natural light to reset the circadian clock.',
                'Sleep Hygiene: Minimize screen time 1–2 hours before bed; instead, read a book or listen to soothing music.',
                'Time Management: Organize your schedule to prioritize sleep and relaxation.'
            ]
        }
    elif 6 <= sleep_duration < 8:
        return {
            'range': '6-8 hours',
            'effects': [
                'Sleep-deprived state: Considered insufficient for optimal health.',
                'Reduced focus: Decreased productivity and problem-solving abilities.',
                'Higher health risks: Prolonged sleep deprivation can lead to obesity, diabetes, and heart disease.',
                'Weakened immunity: Reduced efficiency of the immune system over time.'
            ],
            'tasks': [
                'Bedtime Routine: Establish a consistent routine with calming activities like journaling or listening to white noise.',
                'Dietary Adjustments: Avoid alcohol, heavy meals, and sugary snacks at least 2–3 hours before sleep.',
                'Exercise: Engage in moderate-intensity workouts earlier in the day to enhance sleep quality.',
                'Blue Light Filters: Use blue light blocking glasses or night mode on devices.'
            ]
        }
    elif 7 <= sleep_duration < 9:
        return {
            'range': '7-8 hours',
            'effects': [
                'Optimal for adults: Promotes mental clarity, emotional stability, and physical recovery.',
                'Cognitive enhancement: Improved memory, creativity, and learning capabilities.',
                'Immune strength: Supports efficient immune response and hormonal balance.',
                'Stress reduction: Lower cortisol levels improve overall mood and resilience.'
            ],
            'tasks': [
                'Sleep Consistency: Stick to a regular sleep schedule, including on weekends, to reinforce your body clock.',
                'Balanced Diet: Include magnesium-rich foods (nuts, seeds, spinach) and avoid overeating at dinner.',
                'Mindfulness Practices: Practice gratitude journaling or mindfulness meditation to foster emotional well-being.',
                'Activity Balance: Alternate work with breaks to avoid mental burnout.'
            ]
        }
    elif 9 <= sleep_duration < 10:
        return {
            'range': '9-10 hours',
            'effects': [
                'Recovery benefits: Helps in healing, growth, and recovery from stress or illness, especially for teens and young adults.',
                'Potential warning sign: In adults, excessive sleep may indicate conditions like depression, sleep apnea, or fatigue disorders.',
                'Energy dips: Too much sleep can make you feel lethargic and groggy due to disrupted sleep stages.'
            ],
            'tasks': [
                'Light Exercise: Go for a walk or do light aerobics to energize the body.',
                'Sleep Tracking: Use apps or wearables to monitor sleep patterns and quality.',
                'Identify Triggers: Pay attention to factors (e.g., stress, diet) that might be extending your sleep duration.',
                'Social Interaction: Spend time with friends or pursue a hobby to stay active.'
            ]
        }
    else:
        return {
            'range': '>10 hours',
            'effects': [
                'Lethargy: Prolonged sleep can lead to daytime tiredness and brain fog.',
                'Health risks: Increased risks of obesity, cardiovascular diseases, diabetes, and stroke.',
                'Circadian disruption: Over-sleeping disrupts the body’s natural rhythm, leading to irregular energy levels.',
                'Underlying issues: May point to conditions like hypothyroidism, chronic fatigue syndrome, or depression.'
            ],
            'tasks': [
                'Balanced Routine: Introduce consistent wake-up times to avoid oversleeping.',
                'Physical Activity: Include moderate exercises like swimming or cycling to boost energy.',
                'Engage in Hobbies: Stimulate your mind with creative or social activities to counter feelings of lethargy.',
                'Medical Consultation: Seek advice if prolonged sleep persists and feels unrefreshing.'
            ]
        }

def get_tasks_based_on_duration(sleep_duration):
    if sleep_duration < 4:
        return {
            'range': '<4 hours',
            'effects': [
                'Severe fatigue: Persistent exhaustion impacts daily functioning.',
                'Cognitive impairment: Poor decision-making, focus, and memory.',
                'Immune suppression: Higher susceptibility to colds, flu, and infections.',
                'Hormonal imbalance: Increased cortisol (stress hormone) and reduced growth hormone production.'
            ],
            'tasks': [
                'Power Naps: Take short naps (20–30 mins).',
                'Stress Reduction: Practice light stretching or meditation.',
                'Limit Stimulants: Avoid caffeine and nicotine late at night.',
                'Hydration: Stay hydrated but avoid large quantities before bed.'
            ]
        }
    elif 4 <= sleep_duration < 6:
        return {
            'range': '4-6 hours',
            'effects': [
                'Moderate fatigue: Reduced energy levels and productivity.',
                'Mood swings: Increased irritability and emotional instability.',
                'Reduced concentration: Difficulty focusing on tasks.',
                'Weakened immune system: Increased risk of illness.'
            ],
            'tasks': [
                'Low-impact Exercise: Engage in yoga or walking.',
                'Deep Breathing: Practice stress management techniques.',
                'Balanced Diet: Eat meals with protein and complex carbohydrates.',
                'Consistent Bedtime: Establish a regular sleep schedule.'
            ]
        }
    elif 6 <= sleep_duration < 8:
        return {
            'range': '6-8 hours',
            'effects': [
                'Optimal recovery: Enhanced physical and mental restoration.',
                'Improved memory: Better cognitive function and focus.',
                'Stable mood: Balanced emotional state.',
                'Strong immune system: Lower risk of illness.'
            ],
            'tasks': [
                'Regular Sleep Routine: Maintain consistent sleep habits.',
                'Moderate Exercise: Include activities like brisk walking or light cardio.',
                'Sleep Journaling: Reflect on sleep patterns and habits.',
                'Hydration: Ensure adequate water intake throughout the day.'
            ]
        }
    else:
        return {
            'range': '>8 hours',
            'effects': [
                'Possible oversleeping effects: Grogginess and lethargy.',
                'Disrupted sleep cycle: Difficulty falling asleep at night.',
                'Reduced productivity: Lower energy levels during the day.'
            ],
            'tasks': [
                'Avoid Heavy Meals: Limit large meals before bed.',
                'Screen Time: Reduce exposure to screens before sleep.',
                'Sleep Diary: Track sleep patterns and habits.',
                'Balanced Nutrition: Maintain a healthy diet.'
            ]
        }

@csrf_exempt
@login_required
def record_sleep_time(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            try:
                sleep_time = datetime.strptime(data['sleep_time'], '%H:%M').time()
                wake_time = datetime.strptime(data['wake_time'], '%H:%M').time()
            except ValueError as ve:
                return JsonResponse({'status': 'failed', 'error': f"Invalid time format: {ve}"})

            today = datetime.now().date()

            try:
                # Convert sleep_time and wake_time to datetime objects
                sleep_datetime = datetime.combine(today, sleep_time)
                wake_datetime = datetime.combine(today, wake_time)

                # Handle cases where wake time is the next day
                if wake_datetime < sleep_datetime:
                    wake_datetime += timedelta(days=1)

                # Calculate sleep duration in hours as a float
                sleep_duration = (wake_datetime - sleep_datetime).total_seconds() / 3600.0
            except Exception as calc_error:
                return JsonResponse({'status': 'failed', 'error': f"Error calculating sleep duration: {calc_error}"})

            try:
                # Record the sleep tracking data
                SleepTrack.objects.create(
                    user=request.user,
                    date=today,
                    sleep_duration=sleep_duration,
                    sleep_quality='Good',  # Placeholder, can be customized
                    sleep_stages='N/A',  # Placeholder, can be customized
                    schedule_id=1  # Placeholder, can be customized
                )
            except Exception as db_error:
                return JsonResponse({'status': 'failed', 'error': f"Database error: {db_error}"})

            try:
                # Fetch tasks based on sleep duration
                tasks = get_tasks_based_on_duration(sleep_duration)

                # Render the task cards HTML template with the tasks
                task_cards_html = render_to_string('tracker/task_cards.html', {'effects': tasks})
            except Exception as render_error:
                return JsonResponse({'status': 'failed', 'error': f"Error rendering task cards: {render_error}"})

            return JsonResponse({'status': 'success', 'task_cards': task_cards_html})
        except Exception as e:
            logger.error(f"Unexpected error recording sleep time: {e}")
            return JsonResponse({'status': 'failed', 'error': f"Unexpected error: {e}"})

    # Return failed status for non-POST requests
    return JsonResponse({'status': 'failed'})

