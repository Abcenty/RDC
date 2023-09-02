# Generated by Django 4.2.4 on 2023-09-01 14:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_birthdate_patients_birth_date_and_more'),
        ('treatment', '0003_requests_doctor_alter_requests_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='request_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requests',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.patients'),
        ),
    ]
