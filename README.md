# Fitme

한양대학교 ERICA 오픈소스 소프트웨어 개발 Hola 팀<br/>

2019077183 이혜선 Project Manager, Backend-engineer
2018042660 노지영 Backend-engineer
2019044802 윤진난 Frontend-engineer
2018042533 고유미 Frontend-engineer
2017061044 유지건 Frontend-engineer


## Getting Started

### ✅ Prerequisites

Required | Description
--|--
[Ubuntu](https://ubuntu.com/) | 18.04 LTS
[Python](https://www.python.org/downloads/) | 3.6.8 or above 
[Django](https://www.djangoproject.com/) | 2.2.7 or above

### ✅ Installation
#### 0. Clone this git repository
```
https://github.com/HyeseonLee/OSS_Hola.git
```
#### 1. Install python3, virtualenv
```
$ sudo apt install python3
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenvwrapper
```
#### 2. Create virtualenv
```
$ virtualenv venv
$ source venv/bin/activate
```
If all went well then your command line prompt should now start with (venv).
<!-- Django is installed in virtualenv. So you have to make python virtaul environment. Then activate it. -->

#### 3. Install Django
```
(venv)$ pip3 install django
```
#### 4. Migrate
```
(venv)$ cd django-project
(venv)$ python manage.py migrate
```
#### 5. Start the server
```
(venv)$ python manage.py runserver
```
This will start the webserver on http://127.0.0.1:8000/


## Service Introduction -> See Wiki
https://github.com/HyeseonLee/OSS_Hola/wiki/%EB%AC%B8%EC%84%9C%ED%99%94

#### You can apply for this program if you want.
contact : hyesun1999@gmail.com
