import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_dev.settings")

celery_app = Celery("server_dev")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks() # tasks.py 파일을 자동으로 찾아줌