from __future__ import absolute_import
import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_telegram_bot.settings")

CELERY_TASK_AUTO_DISCOVERY = True

redis = "redis://localhost:6379/"
app = Celery("django_telegram_bot", broker=redis, backend=redis,)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.task_create_missing_queues = True
# app.conf.task_serializer = "json"
# app.conf.result_serializer = "pickle"
# app.conf.accept_content = ["json", "pickle"]
# app.conf.result_expires = timedelta(days=1)
# app.conf.task_always_eager = False


if __name__ == "__main__":
    app.start()