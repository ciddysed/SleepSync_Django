from django.shortcuts import render, redirect, get_object_or_404
from .models import SleepSchedule
from .forms import SleepScheduleForm

def sleep_schedule_list(request):
    schedules = SleepSchedule.objects.all()
    return render(request, 'SleepSchedule/list.html', {'schedules': schedules})

def sleep_schedule_create(request):
    from .forms import SleepScheduleForm  # Import here if necessary
    form = SleepScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('schedule_list')
    return render(request, 'sleepschedule/form.html', {'form': form})

def sleep_schedule_update(request, id):
    schedule = get_object_or_404(SleepSchedule, id=id)
    form = SleepScheduleForm(request.POST or None, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('schedule_list')
    return render(request, 'sleepschedule/form.html', {'form': form})

def sleep_schedule_delete(request, id):
    schedule = get_object_or_404(SleepSchedule, id=id)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'sleepschedule/delete.html', {'schedule': schedule})
