# Generated by Django 5.0.3 on 2024-03-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Departments', models.CharField(max_length=100)),
                ('DateOfJoin', models.DateField()),
                ('ProfileFileName', models.CharField(max_length=100)),
            ],
        ),
    ]
