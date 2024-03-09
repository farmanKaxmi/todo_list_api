from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task
import logging

@shared_task
def my_periodic_task():
    print("My periodic task is running!")


logger = logging.getLogger(__name__)

@shared_task
def send_reminder_emails():

    logger.info("send_reminder_emails task is running!")
    upcoming_tasks = Task.objects.filter(
        deadline__gt=timezone.now(),
        deadline__lte=timezone.now() + timezone.timedelta(days=1),
        completed=False
    )
    print(upcoming_tasks)

    for task in upcoming_tasks:
        subject = f'Reminder: {task.title}'
        message = f'You have a task "{task.title}" with the deadline {task.deadline}'
        send_mail(
            subject,
            message,
            'farmankaxmi@gmail.com',
            [task.user.email],
            fail_silently=False,
        )