# [<img src="welcome/static/images/tubiao.png" width="30"> FaceMaster](http://123.206.213.40/)
* [FaceMaster at a glance](#facemaster-at-a-glance)
* [Requirements to deploy FaceMaster](#requirements-to-deploy-facemaster)
* [How to launch FaceMaster](#how-to-launch-facemaster)
* [Contact me](#contact-me)

## FaceMaster at a glance
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FaceMaster is such a website that can classify your photos using face recognition technology. To take a glance at FaceMaster, just click [here](http://123.206.213.40/). An email is required to sign up for the website. You can upload your photos to website and it'll automatically recognize all the people in your photos. And then, it classifies all the photos by which people is in the photo. The sample page of the website is as follow.
>
>[<img src="sample.png">](http://123.206.213.40/)
## Requirements to deploy FaceMaster
FaceMaster is a django-based website. It uses Mysql as its database. Besides, a celery plus reddis module is required to provide asynchronous task processing capabilities. All the required libraries and some tips will be given as below. Note that all the commands below are tested under Ubuntu 16.04.3 LTS 64 bit system, if you are in other distributions of linux, please change the command to the corresponding pattern.
>>This is a python3 project, so you should first install python3 on your platform. Python3 is pre-installed on ubuntu but the default python version of the conmmand line is python2. If you're in ubuntu system, I recommend you to change the default python version to python3 in a safe way with the commands:
>```bash
>$echo alias python="/usr/bin/python3" >> ~/.bashrc
>$source ~/.bashrc
>```
>>Also, pip is a gorgeous tool for installing Python packages. Install pip3 by running:
>```bash
>$sudo apt-get install python3-pip
>```
>>Then time to install Django-the framework of FaceMaster. Simply type the command below or following the instructions on the [Django official site](https://www.djangoproject.com/).
>```bash
>$sudo pip3 install Django
>```
>>Then comes the database. Install mysql-server, mysql-client and libmysqlclient-dev library by typing the command below. You'll be asked to set a password for the root user when install mysql-server.
>```bash
>$sudo apt-get install mysql-server
>$sudo apt-get install mysql-client
>$sudo apt-get install libmysqlclient-dev
>```
>>It's also recommended to install mysql-workbench to get a friendlier access to the Mysql server if you're in Ubuntu with a GUI. Type this:
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
>$sudo pip3 install celery
>$sudo apt-get install redis-server
>$sudo pip3 install redis
>```
>>I'm using a python library called itsdangerous to help generate a token for account-activation to set a time out, so type the command below to install it:
>```bash
>$sudo pip3 install itsdangerous
>```
>>Also, the face recognition library is from Baidu. Type the command below to install baidu-aip:
>```bash
>$sudo pip3 install baidu-aip
>```
>>Finally, Install Apache to deploy FaceMaster on it. Install the necessary library mod-wsgi to make connection between Django and Apache. Type:
>```bash
>$sudo apt-get install apache2
>$sudo apt-get install libapache2-mod-wsgi-py3
>```
## How to launch FaceMaster
Follow the steps below to launch FaceMaster
>>Create a database by typing:
>```SQL
>CREATE DATABASE demo CHARACTER SET utf8;
>```
>>launch Celery first. Go to base path of the django project and type the command below:
>```bash
>$celery -A demo worker -l info
>```
>>Launch Django then. Go to base path of the django project and type the command below:
>```bash
>$python3 manage.py runserver
>```
>>After all these steps, you can type "127.0.0.1:8000/" in your browser address bar to access the "FaceMaster" web you just deloyed.
>
>>And hey, you were using the default Django server just now. To deploy it on Apache, there are way more steps to operate. (Can I just runaway?)
## Contact me
>The website is far from finished. 
>
>I'd be really happy if you want to communicate with me and share your opinions.
>
>My email address is frankpeng740@yahoo.com
