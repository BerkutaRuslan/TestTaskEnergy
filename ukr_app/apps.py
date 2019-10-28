from django.apps import AppConfig
from .tasks import *


class UkrAppConfig(AppConfig):
    name = 'ukr_app'
