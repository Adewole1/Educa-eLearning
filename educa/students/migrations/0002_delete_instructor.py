# Generated by Django 3.1.7 on 2021-11-25 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('courses', '0004_course_students'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]
