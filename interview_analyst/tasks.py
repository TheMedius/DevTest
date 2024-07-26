# tasks.py
from celery import shared_task
from .utils import send_email

@shared_task
def send_email_task(data):
    send_email(data)
