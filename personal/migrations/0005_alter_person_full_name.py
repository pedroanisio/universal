# Generated by Django 4.2.7 on 2023-11-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_alter_address_id_alter_addresshistory_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
