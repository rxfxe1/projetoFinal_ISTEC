# Generated by Django 5.0 on 2023-12-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('orders', '0001_initial'),
        ('reservations', '0001_initial'),
        ('users', '0002_customuser_delete_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='UserProfile',
        ),
    ]
