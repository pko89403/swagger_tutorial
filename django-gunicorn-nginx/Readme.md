도커 시작 시
~~~sh
docker-compose up --build
~~~
도커 종료 시
~~~sh
docker-ccompose down --volume
~~~

### 참고 사항 - Django
- settings.py 에서 ALLOWED_HOSTS = ['web']
- settings.py 에서 DEBUG = True