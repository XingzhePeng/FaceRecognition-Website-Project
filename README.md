# [<img src="welcome/static/images/tubiao.png" width="30"> FaceMaster](http://123.207.183.210/)
* [FaceMaster at a glance](#facemaster-at-a-glance)
* [Requirements to deploy FaceMaster](#requirements-to-deploy-facemaster)
* [How to launch FaceMaster](#how-to-launch-facemaster)
* [Contact me](#contact-me)

## FaceMaster at a glance
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FaceMaster is a research project by Frank. To take a glance at FaceMaster, just click [here](http://123.207.183.210/).You can get started by uploading some photos with human faces. What we first do is to extract all the face information in your photos. And with the technology called face recognition, we are able to find out which faces are the same person. Finally we keep an N:N relationship between the photos and people inside them. That is, we not only know all the people inside any particular photo but also know all the photos that contain one particular person. Here's a sample page.
>
>[<img src="sample.png">](http://123.207.183.210/)
## Requirements to deploy FaceMaster
FaceMaster is a django-based website. It uses Mysql as its database. Besides, a celery plus reddis module is required to provide asynchronous task processing capabilities. All the required libraries and some tips will be given as below. Note that all the commands below are tested under Ubuntu 16.04.3 LTS 64 bit system, if you are in other distributions of linux, please change the command to the corresponding pattern.
>>This is a python3 project, so you should first install python3 on your platform.
>>Also, pip is a gorgeous tool for installing Python packages. Install pip3 by running:
>```bash
>$sudo apt-get install python3-pip
>```
>>Then install Django. Type the command below or following the instructions on the [Django official site](https://www.djangoproject.com/).
>```bash
>$sudo pip3 install Django==1.11.4
>```
>>Then install mysql-server, mysql-client and libmysqlclient-dev library by typing the command below. You'll be asked to set a password for the root user when install mysql-server.
>```bash
>$sudo apt-get install mysql-server
>$sudo apt-get install mysql-client
>$sudo apt-get install libmysqlclient-dev
>```
>>It's also recommended to install mysql-workbench to get a friendlier access to the Mysql server. Type this:
>```bash
>$sudo apt-get install mysql-workbench
>```
>>Install mysqlclient to build the bridge between Django and Mysql-server, typing:
>```bash
>$sudo apt-get install python3-dev
>$sudo pip3 install mysqlclient
>```
>>Install celery and reddis, typing this:
>```bash
>$sudo pip3 install celery==4.1.1
>$sudo apt-get install redis-server
>$sudo pip3 install redis
>```
>>I'm using a python library called itsdangerous to help generate a token for account-activation to set a time out, so type the command below to install it:
>```bash
>$sudo pip3 install itsdangerous
>```
>>Also, the face recognition library is from Baidu. Type the command below to install baidu-aip:
>```bash
>$sudo pip3 install baidu-aip==1.5.0.0
>```
## How to launch FaceMaster
Follow the steps below to launch FaceMaster
>>Change the email configuration in this file:
>```bash
>FaceMaster/demo/settings.py
>```
>>Change some configuration in this file:
>```bash
>FaceMaster/main/task.py
>```
>>Create a database by typing:
>```SQL
>CREATE DATABASE demo CHARACTER SET utf8;
>```
>>Makemigrations and migrate in django:
>```bash
>cd FaceMaster/
>```
>```python
>python3 manage.py makemigrations
>python3 manage.py migrate
>```
>>launch Celery first:
>```bash
>cd FaceMaster/
>$celery -A demo worker -l info
>```
>>Launch Django then. Go to base path of the django project and type the command below:
>```bash
>cd FaceMaster/
>$python3 manage.py runserver
>```
>>After all these steps, you can type "127.0.0.1:8000/" in your browser address bar to access the "FaceMaster" web you just deloyed.
>
>>And you were using the default Django server just now. To deploy it on Apache or uwsgi+nginx, there are more steps to go. Have fun.
## Contact me
>I'd be really happy if you have some questions to ask me.
>
>Contact me at frankpeng740@yahoo.com
