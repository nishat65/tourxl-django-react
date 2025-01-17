# Generated by Django 5.0.7 on 2024-07-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('office_address', models.TextField(blank=True, null=True)),
                ('total_tours_done', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Guides',
                'db_table': 'guides',
                'ordering': ['-total_tours_done'],
                'indexes': [models.Index(fields=['phone'], name='phone_idx'), models.Index(fields=['email'], name='email_idx')],
            },
        ),
    ]
