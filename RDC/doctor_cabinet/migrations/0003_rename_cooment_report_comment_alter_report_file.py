# Generated by Django 4.2.4 on 2023-09-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_cabinet', '0002_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='cooment',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]