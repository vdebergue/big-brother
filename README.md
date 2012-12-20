big-brother
===========

install basic package
---------------------
```
sudo apt-get install python-virtualenv
cd
virtualenv --distribute --no-site-packages bb-dev
source bb-dev/bin/activate
cd /path/to/big/brother/folder
sudo pip install -r requirements.txt
```

install mongo
-------------
```
sudo apt-get install mongodb-server
```

install db for django
---------------------
```
cd big_brother
python manage.py syncdb
```

launch the server
-----------------
```
python manage.py testserver
```
