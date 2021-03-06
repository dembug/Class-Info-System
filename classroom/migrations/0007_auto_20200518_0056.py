# Generated by Django 3.0.5 on 2020-05-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20200419_2156'),
        ('department', '0006_auto_20200419_2156'),
        ('classroom', '0006_auto_20200518_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classroom_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Classroom Name'),
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='department_name',
        ),
        migrations.AddField(
            model_name='classroom',
            name='department_name',
            field=models.ManyToManyField(to='department.Department', verbose_name='Department Name'),
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='lecture_name',
        ),
        migrations.AddField(
            model_name='classroom',
            name='lecture_name',
            field=models.ManyToManyField(to='lecture.Lecture', verbose_name='Lecture Name'),
        ),
    ]
