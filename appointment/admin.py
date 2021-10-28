from django.contrib import admin

from .models import Appointment_hour
# Register your models here.

@admin.register(Appointment_hour)
class AppointmentAdmin(admin.ModelAdmin):
    
    list_display = ["whom","hour","day","created_date","time_day","week"]
    list_display_links = ["whom"]
    search_fields = ["whom"]
    list_filter = ["hour" , "day" , "week"]
    class Meta:
        model = Appointment_hour
