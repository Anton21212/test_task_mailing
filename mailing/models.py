from django.db import models


class ClientSexFilterChoices(models.TextChoices):
    MAN = ('M', 'Man')
    WOMAN = ('W', 'Woman')


class Mailing(models.Model):
    message = models.TextField(verbose_name='Текст сообщения для доставки клиенту')
    start_datetime = models.DateTimeField(verbose_name='Дата и время запуска')
    end_datetime = models.DateTimeField(verbose_name='Дата и время окончании')
    client_sex_filter = models.CharField(max_length=1, choices=ClientSexFilterChoices.choices)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    phone_number = models.BigIntegerField(verbose_name='Номер телефона')
    mobile_operator_code = models.IntegerField(verbose_name='Код мобильного оператора')
    sex = models.CharField(max_length=1, choices=ClientSexFilterChoices.choices)
    tag = models.TextField(verbose_name='Тег', blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    sending_at = models.DateTimeField(verbose_name='Дата и время отправки', null=True, blank=True, default=None)
    mailing = models.ForeignKey(Mailing, verbose_name='id рассылки', on_delete=models.CASCADE,
                                related_name='created_messages')
    client = models.ForeignKey(Client, verbose_name='id клиента', on_delete=models.CASCADE,
                               related_name='created_messages')
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
