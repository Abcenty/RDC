# Generated by Django 4.2.4 on 2023-09-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_cabinet', '0003_rename_cooment_report_comment_alter_report_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
