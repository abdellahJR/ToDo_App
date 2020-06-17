from django.apps import AppConfig
from datetime import datetime


class TasksConfig(AppConfig):
    name = 'tasks'


def inject_now():
    return dict(now=datetime.now())
