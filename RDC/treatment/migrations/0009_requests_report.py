# Generated by Django 4.2.4 on 2023-09-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_cabinet', '0003_rename_cooment_report_comment_alter_report_file'),
        ('treatment', '0008_alter_requests_payment_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctor_cabinet.report'),
        ),
    ]