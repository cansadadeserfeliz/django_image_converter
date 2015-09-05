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

![](https://habrastorage.org/files/716/486/b39/716486b395da4273bf38515b5edb995a.png)
