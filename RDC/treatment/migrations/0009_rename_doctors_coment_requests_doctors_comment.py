# Generated by Django 4.2.4 on 2023-09-13 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0008_requests_doctors_coment_alter_requests_payment_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='doctors_coment',
            new_name='doctors_comment',
        ),
    ]
