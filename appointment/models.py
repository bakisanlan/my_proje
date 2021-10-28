from django.db import models

# Create your models here.

class Appointment_hour(models.Model):
    whom = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name= "Kimin",blank= True,null=True)
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
    day_list = [
        
        ('1' , "Pazartesi"),
        ('2' , "Salı"),
        ('3' , "Çarşamba"),
        ('4' , "Perşembe"),
        ('5' , "Cuma"),
        ('6' , "Cumartesi"),

    ]

    week_list = [

        ('0' , 'Geçmiş Hafta'),
        ('1' , 'Bu Hafta'),
        ('2' , 'Gelecek Hafta'),
    
    ]

    hour = models.CharField(max_length= 2,choices= hour_list,verbose_name ="Saat")
    day = models.CharField(max_length=1,choices= day_list,verbose_name = "Gün")
    time_day = models.CharField(max_length = 20,verbose_name = "Günün zamanı")
    created_date = models.DateTimeField(auto_now= True,verbose_name="Oluşturulma Tarihi")
    week = models.CharField(max_length= 1, choices= week_list, verbose_name= "Hafta" ,blank= True,null=True)


    def get_absolute_url(self):
        return "/appointment/{}".format(self.id)

    def __str__(self):
        return "{} günü {} saat aralığı".format(self.get_day_display(),self.get_hour_display())




