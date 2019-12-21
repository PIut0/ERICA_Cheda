# ERICA_Cheda
체험을 찾다.<br/>
체다

한양대학교 ERICA 소프트웨어학부 오픈소스 소프트웨어 팀과제<br/>
2019084984_임기성 #1PIut0<br/>
2019077183_이혜선 #2HyeseonLee<br/>


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
https://github.com/PIut0/ERICA_Cheda.git
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
<!-- Django is installed in virtualenv. So you have to make python virtaul environment. Then activate it. -->

#### 3. Install Django
```
(venv)$ pip3 install django
```

#### 4. Migrate
```
(venv)$ cd Cheda
(venv)$ cd django_project
(venv)$ python manage.py migrate
```