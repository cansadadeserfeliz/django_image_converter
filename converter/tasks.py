import time
import os
import random
import uuid

from django.conf import settings

from celery.decorators import task
from PIL import Image


@task()
def task_convert_image(image):
    random_fail = random.randint(7, 13)
    if random_fail == 13:
        raise Exception('Random fail.')

    filename = '{0}.jpg'.format(uuid.uuid4())
    im = Image.open(image)
    im.save(os.path.join(settings.MEDIA_ROOT, filename))

    time.sleep(300)

    return filename