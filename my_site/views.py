from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from appointment.models import Appointment_hour


# Create your views here.

def index(request):
    """import datetime
    import time

    date_time = datetime.datetime(2021,10, 24)
    a_timedelta = date_time - datetime.datetime(1970, 1, 1)
    reference_seconds = a_timedelta.total_seconds()
    week_seconds = 604800
    day_seconds = 86400
    total_seconds = reference_seconds + week_seconds


    for i in range(1,7):
        total_seconds += day_seconds
        for j in range(1,13):
            appointment_hour = Appointment_hour(hour = j , day = i , time_day = total_seconds , week = 2)
            appointment_hour.save()"""

    return render(request,"index.html")

def communication(request):
    return render(request,"communication.html")


def about(request):
    return render(request,"about.html")



