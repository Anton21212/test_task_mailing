# Generated by Django 4.1.2 on 2022-10-30 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RenameField(
            model_name='mailing',
            old_name='client_filter',
            new_name='client_sex_filter',
        ),
        migrations.AlterField(
            model_name='message',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to='mailing.client', verbose_name='id клиента'),
        ),
    ]
