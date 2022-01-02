# Generated by Django 4.0 on 2022-01-02 12:42

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Applicant_name', models.CharField(max_length=32)),
                ('Mobile_No', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('Gender', models.CharField(max_length=32)),
                ('Address', models.CharField(max_length=32)),
                ('Aadhar_No', models.IntegerField()),
                ('Picture', models.ImageField(default='', upload_to='')),
                ('document', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
