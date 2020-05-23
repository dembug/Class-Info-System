# Generated by Django 3.0.6 on 2020-05-19 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0006_remove_lecture_classroom_name'),
        ('classroom', '0014_auto_20200519_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='l_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture', verbose_name='Classroom Name'),
        ),
    ]