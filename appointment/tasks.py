import time
import datetime
from .models import Appointment_hour



def add_appointment():

    appointments_1 = Appointment_hour.objects.filter(week = 1)
    appointments_2 = Appointment_hour.objects.filter(week = 2)

    for appointment_1 in appointments_1:
        appointment_1.week = 0
        appointment_1.save()
    
    for appointment_2 in appointments_2:
        appointment_2.week = 1
        appointment_2.save()

    """date_time = datetime.datetime(2021, 10, 17)
    a_timedelta = date_time - datetime.datetime(1970, 1, 1)
    reference_seconds = a_timedelta.total_seconds()
    week_seconds = 604800
    day_seconds = 86400
    recent_time = time.time()
    recent_time += 10800        #utc farkı
    week_counter = (recent_time - reference_seconds) / week_seconds
    week_counter = round(week_counter)

    for week in args:
        if week_counter == week:
            true_week_seconds = week_seconds * week
            total_seconds = reference_seconds + true_week_seconds
            break
    print(week_counter)"""
    
    recent_time = time.time()
    recent_time += 10800  #utc
    total_seconds = recent_time + 604800  #haftalık
    day_seconds = 86400

    for i in range(1,7):
        total_seconds += day_seconds
        for j in range(1,13):
            appointment_hour = Appointment_hour(hour = j , day = i , time_day = total_seconds , week = 2)
            appointment_hour.save()
