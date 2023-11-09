# Generated by Django 4.2.7 on 2023-11-09 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0002_concept_description_concept_parents_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('template', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='universalentity',
            name='concepts',
        ),
        migrations.AddField(
            model_name='universalentity',
            name='concept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entities', to='ontology.concept'),
        ),
        migrations.AddField(
            model_name='concept',
            name='json_structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concepts', to='ontology.jsonstructure'),
        ),
    ]