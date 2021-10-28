# Generated by Django 3.2.7 on 2021-10-19 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(choices=[('1', '09.00-10.00'), ('2', '10.00-11.00'), ('3', '11.00-12.00'), ('4', '12.00-13.00'), ('5', '13.00-14.00'), ('6', '14.00-15.00'), ('7', '15.00-16.00'), ('8', '16.00-17.00'), ('9', '17.00-18.00'), ('10', '18.00-19.00'), ('11', '19.00-20.00'), ('12', '20.00-21.00')], max_length=2, verbose_name='Saat')),
                ('day', models.CharField(choices=[('1', 'Pazartesi'), ('2', 'Salı'), ('3', 'Çarşamba'), ('4', 'Perşembe'), ('5', 'Cuma'), ('6', 'Cumartesi')], max_length=1, verbose_name='Gün')),
                ('time_day', models.CharField(max_length=20, verbose_name='Günün zamanı')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('whom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kimin')),
            ],
        ),
    ]
