from celery import Celery

from mysite.celery import app

@app.task
def add(x, y):
    return x + y