import time
from django.db.models import Q
from config.celeryapp import app
from .models import Mailing, Client, Message
import pytz
from django.utils import timezone


@app.task()
def send_message(
        message_id: int,
        message_text: str,
        phone_number: str,
        mobile_operator_code: str,  # noqa нужен для определения конкретного сервиса по отправке.
):
    message_obj = Message.objects.get(id=message_id)
    print(f"Сообщение клиенту с номер {phone_number} было отправлено. Текст сообщения: {message_text}")
    current_utc_datetime = timezone.datetime.now().astimezone(tz=pytz.UTC)
    message_obj.sending_at = current_utc_datetime
    message_obj.save()


@app.task()
def mailings_scheduler():
    while True:
        current_utc_datetime = timezone.now()

        mailing_objs = Mailing.objects.filter(
            start_datetime__lte=current_utc_datetime,
            end_datetime__gt=current_utc_datetime
        )
        for mailing_obj in mailing_objs:
            client_objs = Client.objects.filter(sex=mailing_obj.client_sex_filter).filter(
                ~Q(created_messages__mailing_id=mailing_obj.id) | Q(created_messages__isnull=True))

            for clint_obj in client_objs:
                message_obj = Message.objects.create(client=clint_obj, mailing=mailing_obj)

                send_message.apply_async(
                    (
                        message_obj.id,
                        mailing_obj.message,
                        clint_obj.phone_number,
                        clint_obj.mobile_operator_code
                    ),
                    expires=mailing_obj.end_datetime
                )
        time.sleep(3)
