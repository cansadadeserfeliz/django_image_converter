# Django Image Converter (test project)

## Installation

(tested on Ubuntu 14.04)

    sudo apt-get install redis-server
    sudo service redis-server restart

    pip install -r requirements.txt

Run celery worker:

    ./manage.py celery worker --loglevel=info