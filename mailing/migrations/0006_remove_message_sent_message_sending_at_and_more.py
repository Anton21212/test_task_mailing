# Generated by Django 4.1.2 on 2022-10-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_message_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sent',
        ),
        migrations.AddField(
            model_name='message',
            name='sending_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата и время отправки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
    ]
