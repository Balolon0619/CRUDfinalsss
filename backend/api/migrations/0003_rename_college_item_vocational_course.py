# Generated by Django 5.0.6 on 2024-07-15 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_studentid_item_college_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='college',
            new_name='vocational_course',
        ),
    ]
