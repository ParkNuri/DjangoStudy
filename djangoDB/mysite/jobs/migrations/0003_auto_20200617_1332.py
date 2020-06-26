# Generated by Django 2.1.15 on 2020-06-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_person_past_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='person',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='person',
            name='past_job',
            field=models.TextField(default=''),
        ),
    ]
