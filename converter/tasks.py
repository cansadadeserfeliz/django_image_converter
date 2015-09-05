import time
import os

from celery.decorators import task
from PIL import Image

from app.settings import MEDIA_ROOT


@task()
def task_convert_image(image, filename):
    im = Image.open(image)
    im.save(os.path.join(MEDIA_ROOT, filename))

    time.sleep(300)

    return filename