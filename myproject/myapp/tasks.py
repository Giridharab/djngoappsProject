from celery import shared_task
from .models import Nugget


@shared_task
def create_nugget_task(content):
    nugget = Nugget.objects.create(content=content)
    return nugget.id


@shared_task
def modify_nugget_task(nugget_id, content):
    Nugget.objects.filter(id=nugget_id).update(content=content)
    return True


@shared_task
def delete_nugget_task(nugget_id):
    Nugget.objects.filter(id=nugget_id).delete()
    return True
