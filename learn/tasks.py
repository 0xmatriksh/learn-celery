from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    sleep(20)
    return x + y