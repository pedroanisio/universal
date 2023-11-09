# Generated by Django 4.2.7 on 2023-11-09 15:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion

from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        CreateExtension('postgis'),        
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('ground_zero', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAccount',
            fields=[
                ('email_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email_address', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileAccount',
            fields=[
                ('mobile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('prefix_title', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary'), ('NotInformed', 'NotInformed')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('social_media_id', models.IntegerField(primary_key=True, serialize=False)),
                ('platform_name', models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram')], max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.IntegerField(primary_key=True, serialize=False)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.address')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDocument',
            fields=[
                ('document_id', models.IntegerField(primary_key=True, serialize=False)),
                ('document_type', models.CharField(choices=[('Passport', 'Passport'), ('CPF', 'CPF'), ('RG', 'RG'), ('DriverLicense', 'DriverLicense'), ('RNE', 'RNE'), ('SocialSec', 'SocialSec')], max_length=255)),
                ('document_number', models.CharField(max_length=255)),
                ('issuer_authority', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person')),
            ],
        ),
        migrations.CreateModel(
            name='MobileHistory',
            fields=[
                ('mobile_history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('mobile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.mobileaccount')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person')),
            ],
        ),
        migrations.AddField(
            model_name='mobileaccount',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person'),
        ),
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('email_history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('email_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.emailaccount')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person')),
            ],
        ),
        migrations.AddField(
            model_name='emailaccount',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person'),
        ),
        migrations.CreateModel(
            name='AddressHistory',
            fields=[
                ('address_history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.address')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.person'),
        ),
    ]
