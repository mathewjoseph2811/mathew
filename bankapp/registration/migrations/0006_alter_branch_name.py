# Generated by Django 3.2.15 on 2022-08-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20220814_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(blank=True, default='Kovalam', max_length=100),
        ),
    ]