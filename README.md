# chatproj

For looking app 'alive', follow 
https://chat-room-for-you.herokuapp.com/

Launch this app locally:

Work on Linux. Open teminal.

$ wget https://bootstrap.pypa.io/get-pip.py

$ sudo python get-pip.py

$ sudo pip install virtualenv

$ virtualenv chat --no-site-packages

$ cd chat

$ source bin/activate

(chat)$ pip install Django

(chat)$ mkdir src

(chat)$ cd src

(chat)$ git clone git@github.com:grydinywka/chatproj.git

(chat)$ cd chatproj/

(chat)$ pip install -r requirements.txt

Next stage, we should create database. Open postgresql(if need - install one ):

=# create database chatproj_db;

=# create user chatproj_db_user with password 'chatproj_db_user';

=# grant connect on database chatproj_db to chatproj_db_user;

(chat)$ cd ../../bin

(chat)$ gedit activate

add to end file next two lines:

DJANGO_SETTINGS_MODULE="chatproj.development_settings"

export DJANGO_SETTINGS_MODULE

Save file

(chat)$ deactivate

$ source activate

(chat)$ cd ../src/chatproj/

(chat)$ python manage.py migrate

(chat)$ python manage.py runserver
