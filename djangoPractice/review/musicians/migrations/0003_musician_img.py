# Generated by Django 3.0.7 on 2020-06-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0002_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='img',
            field=models.CharField(default='', max_length=150),
        ),
    ]