from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Animal
from .utils import age_math
from datetime import datetime, timedelta, date


logger = get_task_logger(__name__)


@shared_task
def add(x,y):
    # logger.info("sent, done, finished with your task even though i haven't started")
    return (x + y)


@shared_task
def update_dead(animal_type, age_week, age_day, user):
    age_in_days = age_math(age_week, age_day)
    red = datetime.strptime(str(date.today()), '%Y-%m-%d') - timedelta(days=age_in_days)
    print(red.strftime('%d-%m-%Y'))
    dead_query = Animal.objects.filter(owner_id = user,created_at=red, alive=True, animal=animal_type).first()
    # print(dead_query.alive)
    if dead_query:
        dead_query.alive = False
        print("done")
        dead_query.save()
    else:
        return "Animal Not Found"