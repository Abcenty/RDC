# Generated by Django 4.2.4 on 2023-09-28 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('doctor_cabinet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='services',
            field=models.ManyToManyField(to='user.services'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
