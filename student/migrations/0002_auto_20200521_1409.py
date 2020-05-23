# Generated by Django 3.0.6 on 2020-05-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_auto_20200419_2156'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department_name',
        ),
        migrations.AddField(
            model_name='student',
            name='department_name',
            field=models.ManyToManyField(to='department.Department'),
        ),
    ]