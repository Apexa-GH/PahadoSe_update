# Generated by Django 5.0.7 on 2024-08-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_experience_enddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Non', models.CharField(blank=True, default='0', max_length=255, null=True)),
                ('View', models.CharField(blank=True, default='0', max_length=255, null=True)),
                ('Image', models.FileField(blank=True, null=True, upload_to='Reviews')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.TextField(blank=True, default='')),
                ('SmallDescription', models.TextField(blank=True, default='')),
            ],
        ),
    ]
