## docker-compose.yml
내부에 도커로 3개의 컨테이너를 올린다.(docker-compose up)    
- Nginx( reverse proxy )
- Nginx( server )
- php-fpm 컨테이너

>reverse proxy 서버는 80번 포트를 open하고
>뒷 단의 Nginx 서버는 8080 포트를 오픈한다.
>크롬에서 localhost를 입력하면 Reverse Proxy 서버가 뒷단의 Nginx의 phpinfo() 결과를 보여준다.

### upstream이 뭘까?
nginx에 내장된 모듈로 부하분산, 속도 개선과 같은 역할을 한다.    
http://nginxisnotproblem.blogspot.com/2014/11/05-upstream.html
~~~sh
upstream 이름 {
    [ip_hash;]
    server host 주소:포트 [옵션];
    .....
}
~~~
**listen의 의미는 뭘까?** 클라이언트로 연결 요청이 수신 되는지 listen(주시)