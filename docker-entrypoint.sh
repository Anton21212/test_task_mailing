#!/bin/bash
echo "from mailing.tasks import mailings_scheduler; mailings_scheduler.delay()" | python manage.py shell
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:80
