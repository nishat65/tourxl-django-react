# Generated by Django 5.0.7 on 2024-07-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='difficulty_level',
            field=models.CharField(choices=[('easy', 'easy'), ('moderate', 'moderate'), ('challenging', 'challenging'), ('extreme', 'extreme')], max_length=100),
        ),
    ]
