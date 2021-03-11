# Generated by Django 3.1.5 on 2021-03-11 13:20

import datetime
import detect.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Under Investigation', 'Under Investigation'), ('Solved', 'Solved')], default='Under Investigation', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5)])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=255)),
                ('dob', models.DateField(null='True', validators=[detect.models.validate_dob], verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('NOT WANTED', 'NOT WANTED'), ('WANTED', 'WANTED')], default='NOT WANTED', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='detect.person')),
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.CharField(choices=[('Human Resource', 'Human Resource'), ('Finance', 'Finance'), ('Information Management', 'Information Management'), ('Administration', 'Administration')], max_length=100)),
                ('employee_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Fired', 'Fired')], default='Active', max_length=100)),
            ],
            bases=('detect.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='detect.person')),
                ('student_id', models.IntegerField(primary_key=True, serialize=False, validators=[detect.models.validate_length])),
                ('student_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Graduated', 'Graduated'), ('Suspended', 'Suspended')], default='Active', max_length=100)),
            ],
            bases=('detect.person',),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to=detect.models.get_upload_to)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detect.person')),
            ],
        ),
        migrations.CreateModel(
            name='DetectedCriminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('location', models.CharField(max_length=255)),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='detect.person')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detect.faculty')),
            ],
        ),
    ]
