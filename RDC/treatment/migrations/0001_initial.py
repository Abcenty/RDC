# Generated by Django 4.2.4 on 2023-08-17 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('request_data', models.DateTimeField(auto_now_add=True)),
                ('payment_data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Researches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_file', models.FileField(upload_to='')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.requests')),
            ],
        ),
    ]
