# Generated by Django 4.0.1 on 2024-01-30 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_message_date_message_timestamp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='date',
        ),
    ]