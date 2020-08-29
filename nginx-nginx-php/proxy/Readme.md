리버스 프록시 서버 역할을 할 Nginx 컨테이너다. 80 포트를 호스트와 공유하고 있다.    
볼륨 에서는 호스트 pc의 proxy/nginx.conf 파일을 container의 /etc/nginx/nginx.conf로 공유하고 있다