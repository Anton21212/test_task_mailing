# Generated by Django 4.1.2 on 2022-10-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_client_sex_alter_mailing_client_sex_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='tag',
            field=models.TextField(blank=True, verbose_name='Тег'),
        ),
    ]
