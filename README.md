# Django Image Converter (test project)

## Installation

(tested on Ubuntu 14.04)

    sudo apt-get install redis-server
    sudo service redis-server restart

    pip install -r requirements.txt

Run celery worker:

    ./manage.py celery worker --loglevel=info
    ./manage.py celerycam
    
## Screenshots

![](https://habrastorage.org/files/e80/8e6/7df/e808e67df6a64802bb7643916be9fbae.png)
