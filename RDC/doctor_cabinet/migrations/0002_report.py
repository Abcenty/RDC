# Generated by Django 4.2.4 on 2023-09-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_cabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('cooment', models.TextField()),
            ],
        ),
    ]