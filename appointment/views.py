from datetime import date
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

import appointment
from .forms import RegisterForm,LoginForm
from .models import Appointment_hour





from django.contrib import messages
# Create your views here.



def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("firts_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")

        if User.objects.filter(username = username):
            messages.info(request,"Bu kullanıcı adı zaten sistemde kayıtlı!")
            context = {
            "form" : form
                        }
            return render(request,"register.html",context)

        else:
            newUser = User(username =username)
            newUser.set_password(password)
            newUser.save()
        
            login(request,newUser)
            messages.success(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("index")
    
    context = {
            "form" : form
        }

    return render(request,"register.html",context)
    
def loginUser(request):
    if request.user.is_authenticated:
        appointments = Appointment_hour.objects.all()
        hour_list = [

        ('1' , "09.00-10.00"),
        ('2' , "10.00-11.00"),
        ('3' , "11.00-12.00"),
        ('4' , "12.00-13.00"),
        ('5' , "13.00-14.00"),
        ('6' , "14.00-15.00"),
        ('7' , "15.00-16.00"),
        ('8' , "16.00-17.00"),
        ('9' , "17.00-18.00"),
        ('10', "18.00-19.00"),
        ('11', "19.00-20.00"),
        ('12', "20.00-21.00"),

        ]    
        import datetime
        import time

        date_time = datetime.datetime(2021,10, 17)
        a_timedelta = date_time - datetime.datetime(1970, 1, 1)
        reference_seconds = a_timedelta.total_seconds()      
        recent_time = time.time()
        recent_time += 10800
        week_seconds = 604800
        day_seconds = 86400

        appointments_1_monday = Appointment_hour.objects.filter(week = 1, day = 1 , hour = 1)

        from datetime import datetime
        import locale
        locale.setlocale(locale.LC_ALL,"tr_TR")

        week_name_seconds_1_1 = appointments_1_monday.first().time_day
        week_name_seconds_1_1_len = len(week_name_seconds_1_1)
        week_name_seconds_1_1 = int((appointments_1_monday.first().time_day)[0:week_name_seconds_1_1_len-2])
        week_name_seconds_1_2 = week_name_seconds_1_1 + week_seconds - day_seconds
        week_name_day_1_1 = datetime.fromtimestamp(week_name_seconds_1_1).strftime("%d")
        week_name_month_1_1 = datetime.fromtimestamp(week_name_seconds_1_1).strftime("%B")
        week_name_day_1_2 = datetime.fromtimestamp(week_name_seconds_1_2).strftime("%d")
        week_name_1 = week_name_day_1_1 + "-" + week_name_day_1_2 +" " + week_name_month_1_1

        week_name_seconds_2_1 = week_name_seconds_1_1 + week_seconds
        week_name_seconds_2_2 = week_name_seconds_1_2 + week_seconds
        week_name_day_2_1 = datetime.fromtimestamp(week_name_seconds_2_1).strftime("%d")
        week_name_month_2_1 = datetime.fromtimestamp(week_name_seconds_2_1).strftime("%B")
        week_name_day_2_2 = datetime.fromtimestamp(week_name_seconds_2_2).strftime("%d")
        week_name_2 = week_name_day_2_1 + "-" + week_name_day_2_2 +" " + week_name_month_2_1


        return render(request,"take_appointment.html", {"appointments" : appointments, "hour_list" : hour_list,
                                                        "reference" : reference_seconds ,"recent_time" : recent_time, 
                                                        "week_name_1" : week_name_1, "week_name_2" : week_name_2})   

    else:
        form = LoginForm(request.POST or None)

        context = {
            "form":form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username,password = password)

            if user is None:
                messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
                return render(request,"login.html",context)

            messages.success(request,"Başarıyla Giriş Yaptınız")
            login(request,user)
            return redirect('appointment:login')
        return render(request,"login.html",context)


@login_required(login_url="appointment:login")
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

@login_required(login_url="appointment:login")
def appointment_success(request,id):
    from datetime import datetime
    import locale
    locale.setlocale(locale.LC_ALL,"tr_TR")
    appointment = get_object_or_404(Appointment_hour,id = id)
    appointment.whom = request.user
    appointment.save()
    date_seconds = round(float(appointment.time_day))
    date = datetime.fromtimestamp(date_seconds).strftime("%d %B %Y")
    messages.success(request, "Randevunuz Başarıyla Alındı")
    return render(request, "appointment_success.html", {"appointment" : appointment, "date" : date})

@login_required(login_url="appointment:login")
def my_appointment(request):
    appointments = Appointment_hour.objects.filter(whom = request.user)
    list= []
    for appointment in appointments:
        from datetime import datetime
        import locale
        locale.setlocale(locale.LC_ALL,"tr_TR")
        date_seconds = round(float(appointment.time_day))
        date = datetime.fromtimestamp(date_seconds).strftime("%d %B %Y")
        list.append(date)
    
    appo_date = zip(appointments,list)
    return render(request, "my_appointment.html", {"appointments" : appointments , "appo_date" : appo_date})

@login_required(login_url="appointment:login")
def delete_appointment(request,id):

    appointment = get_object_or_404(Appointment_hour, id = id)
    appointment.whom = None
    appointment.save()
    messages.success(request, "Randevunuz Başarıyla Silindi")
    return redirect('/appointment/my_appointment')





