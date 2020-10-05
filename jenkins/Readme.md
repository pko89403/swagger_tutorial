# Jenkins
Continuous Integration & Delivery Server   
- workspace - /var/jenkins_home
- port50000 - connect a slave agent
## 설치하기
~~~sh
mkdir -p app/jenkins
chmod 777 app/jenkins
docker run -d -p 8080:8080 -p 50000:50000 -v /Users/kangseokwoo/From_Nginx_To_API/jenkins/app/jenkins:/var/jenkins_home --name jenkins -u root jenkins/jenkins:lts
~~~

## Jenkins 브라우저로 접속하기
패스워드를 입력하라고 나온다.
app/jenkins/secrets/initialAdminPassword 가서 볼 수 도 있곡
~~~sh
docker logs jenkins 
~~~
로도 확인 할 수 있다.

## Jenkins 와 Github 연동하기
1. Github 계정의 setting->developer setting->private access token
2. Jenkins의 setting에 들어가서 configuration -> GitHub Servers
3. Add Credential -> Secret text( tab ) -> Secret에 token 입력한다
4. Add NewItem -> Github project에 git repo url 추가

## ssh key setting
1. ssh-keygen으로 key를 생성한다. ( var/root/.ssh/* )
2. private repository -> setting -> deploy keys에 pubkey를 입력한다.
3. Webhook을 세팅해준다.