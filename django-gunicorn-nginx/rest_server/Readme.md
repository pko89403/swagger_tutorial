# Django를 이용한 Rest API 서버 구축
## Django 세팅
~~~sh
django-admin startproject rest_server
~~~
rest_server/settings.py 파일을 열어서 다음과 같이 내용을 추가해준다
~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_swagger'
]
~~~
~~~sh
python manage.py startapp item2item
~~~
그리고 rest_server/settings.py 파일에 Installed App에 방금 생성한 앱을 추가해준다
~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'item2item'
]
~~~
## DB세팅
API를 이용해 접근할 수 있는 DB를 만들어준다. member/models.py 파일을 수정해준다.

~~~python
from django.db import models

class item2item(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
~~~
모델을 수정한 경우 Django에서는 makemigration과 migrate를 해줘야한다.
~~~sh
python manage.py makemigrations item2item
python manage.py migrate item2item
~~~
~~~
python manage.py shell
>>> from item2item.models import item2item
>>> item2item.objects.create(name='seokwoo', mail='pko954@amorepacific.com', age=29)
~~~
## API 뷰 만들기
API 요청에 따라 응답을 해주는 뷰를 작성해야 한다.     
item2item 폴더 하단에 api.py를 만들어주고 코드를 작성함    
     
Serializer는 API를 통한 요청에 대한 응답의 형태들을 결정해주는 클래스이다.    
ViewSet은 요청을 처리하여 응답을 해주는 클래스이다.    
추후에 get, post. put, patch. delete에 대한 액션을 지정해주면 된다.

## 결과 확인
~~~python
python manage.py runserver 0.0.0.0:8000
~~~
## 마지막 
http://localhost:8000/api/v1/item2item/

~~~sh
gunicorn --bind 0.0.0.0:8000 rest_server.wsgi:application
~~~
~~~sh
gunicorn -c gunicorn.py.ini rest_server.wsgi:application
~~~