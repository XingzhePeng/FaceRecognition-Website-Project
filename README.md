# [<img src="welcome/static/images/tubiao.png" width="30"> FaceMaster](http://123.207.183.210/)
* [FaceMaster at a glance](#facemaster-at-a-glance)
* [Requirements to deploy FaceMaster](#requirements-to-deploy-facemaster)
* [How to launch FaceMaster](#how-to-launch-facemaster)
* [Contact me](#contact-me)

## FaceMaster at a glance
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FaceMaster is a research project by Peng Xingzhe. To take a glance at FaceMaster, just click [here](http://123.207.183.210/).You can get started by uploading some photos with human faces inside. What we do first is to extract all the faces in your photos. And with the technology face recognition, we are able to find out which faces are of the same person. Finally we keep an N:N relationship between the photos and people. That is we are aware not only of all the people inside any particular photo but also of all the photos that contain one particular person. Here's a sample page of FaceMaster.
>
>[<img src="sample.png">](http://123.207.183.210/)
## Requirements to deploy FaceMaster
FaceMaster uses django as its back-end, mysql as its database. Besides, a celery plus reddis module is required to provide asynchronous processing capabilitiy. All the required libraries and some tips will be given as below. Note that all the commands below had been tested well on Ubuntu 16.04 LTS 64 bit system, if you were in other distribution of linux, we suggest changing the commands to the corresponding pattern.
>>This is a python3 project, so you should first install python3 on your platform.Also, pip is a gorgeous tool for installing Python packages. Install pip3 by running:
>```bash
>$ sudo apt-get install python3-pip
>```
>>Then install django. Type the command below or following the instructions on the [django official site](https://www.djangoproject.com/).
>```bash
>$ sudo pip3 install Django==1.11.4
>```
>>Then install mysql-server, mysql-client and libmysqlclient-dev by typing the command below. You'll be asked to set a password for the root user of mysql when install mysql-server.
>```bash
>$ sudo apt-get install mysql-server
>$ sudo apt-get install mysql-client
>$ sudo apt-get install libmysqlclient-dev
>```
>>We also recommend you to install mysql-workbench to get a friendly interaction to mysql database, typing:
>```bash
>$ sudo apt-get install mysql-workbench
>```
>>Install mysqlclient to build the connection between django and Mysql-server, typing:
>```bash
>$ sudo apt-get install python3-dev
>$ sudo pip3 install mysqlclient
>```
>>Install celery and reddis, typing:
>```bash
>$ sudo pip3 install celery==4.1.1
>$ sudo apt-get install redis-server
>$ sudo pip3 install redis
>```
>>We use a python library, itsdangerous to generate a token to set a time-out for account activation. Type the command below to install it:
>```bash
>$ sudo pip3 install itsdangerous
>```
>>Also, the face recognition library, baidu-aip is from Baidu. Type the command below to install baidu-aip:
>```bash
>$ sudo pip3 install baidu-aip==1.5.0.0
>```
## How to launch FaceMaster
Follow the steps below to launch FaceMaster
>>Change the database configuration and email configuration in this file:
>```bash
>FaceMaster/demo/settings.py
>```
>>Change some configuration in this file:
>```bash
>FaceMaster/main/task.py
>```
>>Create a mysql database by typing:
>```bash
>mysql -uroot -p
>```
>```SQL
>CREATE DATABASE demo CHARACTER SET utf8;
>```
>>Makemigrations and migrate in django:
>```python
>cd FaceMaster/
>python3 manage.py makemigrations
>python3 manage.py migrate
>```
>>launch celery first:
>```bash
>cd FaceMaster/
>$celery -A demo worker -l info
>```
>>Launch django then. Type the command below:
>```bash
>cd FaceMaster/
>$python3 manage.py runserver
>```
>>After all the steps, you can type the following address in your browser to access the "FaceMaster" website you just deloyed.
>```bash
>127.0.0.1:8000/
>```
>>Note that following the steps above you are just using the built-in server of django. To deploy it on Apache or uwsgi+nginx, there are more steps to go.
## Contact me
>Any question on this project is warmly welcomed.
>
>My email address is: frankpeng740@yahoo.com
