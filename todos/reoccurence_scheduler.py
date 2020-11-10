from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from .models import Todo
from django.utils import timezone
from datetime import timedelta
import calendar


def update_deadline():
    for todo in Todo.objects.all():
        if todo.deadline < timezone.now():
            if todo.recurring == "d":
                todo.deadline = todo.deadline + timedelta(days=1)
                todo.save()
            elif todo.recurring == "w":
                todo.deadline = todo.deadline + timedelta(days=7)
                todo.save()
            elif todo.recurring == "m":
                days_in_month = calendar.monthrange(todo.deadline.year, todo.deadline.month)[1]
                todo.deadline = todo.deadline + timedelta(days=days_in_month)
                todo.save()
            elif todo.recurring == "y":
                if calendar.isleap(todo.deadline.year):
                    todo.deadline = todo.deadline + timedelta(days=366)
                    todo.save()
                else:
                    todo.deadline = todo.deadline + timedelta(days=365)
                    todo.save()


def start():
    scheduler = BackgroundScheduler()
    """Updating the deadline every day at 1am"""
    scheduler.add_job(update_deadline, 'cron', hour=1)
    scheduler.start()
