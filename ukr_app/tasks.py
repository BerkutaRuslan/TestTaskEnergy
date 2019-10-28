from time import sleep
import requests

from ukr_project.celery import shared_task
from ukr_app.models import Links


@shared_task
def test(id):
    print(id, 'Status checked and updated')
    link = Links.objects.get(pk=id)
    response = requests.get(link.url)
    if response.status_code == 200:
        Links.objects.filter(pk=id).update(
            status=True)
    else:
        Links.objects.filter(pk=id).update(
            status=False)


