import time
import os

from django.conf import settings

from celery.decorators import task
from PIL import Image


@task()
def task_convert_image(image, filename):
    im = Image.open(image)
    im.save(os.path.join(settings.MEDIA_ROOT, filename))

    time.sleep(300)

    return filename