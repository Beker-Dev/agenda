# Generated by Django 4.0.6 on 2022-07-10 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
