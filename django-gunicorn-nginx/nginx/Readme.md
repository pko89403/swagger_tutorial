# Nginx란?
아아아 ... Velog님 쩔어!!! https://velog.io/@minholee_93/Nginx-Load-Balancer       
썰에 따르면 apache 서버 성능에 좌절한 개발자가...동시에 10000건의 concurrent connection까지 처리할 수 있도록 개발한 차세대 웹 서버다    
Nginx 는 reverse proxy server로도 사용 가능 하다   
Nginx는 각각의 request를 하나의 Nginx 머신이 asynchronously 하게 처리한다        
Static Response는 Nginx 머신에서 즉시 전달    
server 쪽에서 처리해아되는 response가 요청된 경우에는, 해당 요청은 완전히 독립된 server process에서 처리된 뒤 Nginx의 Reverse Proxy를 사용해 결과 값을 전달한다      

## Virtual Host
- virtual host는 server block 안에 작성한다.
- virtual host의 server_name은 ip 혹은 domain으로 입력한다.

## Location  Blocks
- location은 specific url에 대한 behavior를 정의하며 server 내부에 작성한다
- match 에는 prefix match, exact match, regex match, preferential prefix match가 있다.

## Variables 
- nginx.conf에서 사용할 수 있는 변수를 의미한다
- configuratble variable : 사용자가 직접 정의해서 사용함
- module variable : nginx 의 내장 변수 $host $uri $args

## Redirect 
- static 한 값이 아닌 또다른 uri를 return 하는 경우에 state code는 307이며 redirect 라고 한다

## Rewrite
- 내부적으로 요청을 처리하고 uri는 기존에 호출했던 uri를 유지 한다

## try_files
- 모든 request에 순서대로 앞에서 부터 path를 확인한 후 만약 해당 path가 root에 존재한다면 해당 path로 rewrite 한다
    
## Logging
- Nginx는 access & error log를 기본으로 제공한다
- nginx default log path는 /var/log/nginx 다

## Worker Process
- nginx 에서 실제로 수행하고 response를 return하는 process는 master가 아닌 worker 다.
- default로 1개의 master process와 1개의 worker process를 사용하고 있다
- 단순히 worker process 의 숫자를 늘리는 것은 성능향상에 도움이 되지 않는다. 하나로도 이미 hardware 성능을 최대로 사용함
- 모든 server는 각 core 별로 동일한 file을 한번에 open 할 수 있는 number의 limit이 정해져 있다 ( 서버 마다 달라서 알아봐야함 )
- worker_processes X worker_connections = max_connections 만큼 request를 동시에 처리할 수 있다 

## Buffer 와 Timeout
- 위 둘을 적절히 사용하면 nginx의 performance를 증가 시킬 수 있다
- Buffer : nginx와 같은 프로세스가 RAM으로 부터 데이터를 읽거나 쓰는 것
    1. nginx는 http로 들어온 Request를 먼저 Buffer에 저장하고 처리한다.... Buffer에 여유 공간이 없으면 hdd 같은 곳에 저장함
    2. Response 값도 Client에게 Return하기 전에 먼저 Buffer에 저장된 후, Nginx는 Buffer에서 데이터를 읽어 Client에게 전달함
    3. process에서 데이터를 read / write 할때는 중간에 Buffer를 둔다. ... 처리 과정은 조금 복잡해지지만 성능 상 효율이 올라간다
    > Buffer의 크기를 잘 조정할 필요가 있는게 너무 크면 낭비고 너무 작으면 hdd에 접근을 자주 해야한다.
- Timeout : 들어오는 request의 처리 시간
## Dynamic Module
## Header & Expire
## Compressed Resonse with gzip
## FastCGI Cache
## HTTP/2
## HTTPS
## Rate Limiting
## Basic Auth
## Hadrdening Nginx
## SSL 인증서
## Reverse Proxy
Nginx가 클라이언트로 전달 받은 요청을 어플리케이션 서버에 전달한 뒤,     
어플리케이션 서버가 반환한 결과값을 다시 클라이언트에게 전달하는 방법     
    > 클라이언트는 모든 request 요청과 응답을 어플리케이션 서버가 아닌 Nginx를 통해 수행하게 된다

## Load Balancer
mutliple clientdml request를 multiple server에 distribute 해서 서버 별 load를 분산시킨다
- Redundancy : 만약 로드 밸런서에 연결된 서버 중 특정 서버가 다운 되는 경우, 해당 서버로의 트래픽을 가용한 서버로 redirect 한다
- reverse proxy 와 함께 사용된다