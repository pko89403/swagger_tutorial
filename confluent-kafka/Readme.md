# Confluent Kafka OSS
Confluent, founded by the creators of Kafka, provides an open-source software(OSS) distribution of Kafka.    
Kafka requires Java run-time environment, and the setup of many config options    
Confluent provided Docker containers, all necessary dependencies    
all configuration options can also be centralized in a single     
[Reference1-confluent-kafka-docker](https://medium.com/@robcowart/deploying-confluent-platform-kafka-oss-using-docker-39b65fa6809b)
     
[Reference2-confluent-kafka-docker](https://medium.com/better-programming/your-local-event-driven-environment-using-dockerised-kafka-cluster-6e84af09cd95)

[Reference-schema-registry-to-kafka](https://medium.com/better-programming/adding-schema-registry-to-kafka-in-your-local-docker-environment-49ada28c8a9b)
## docker-compose.yaml
분산 시스템은 다양한 동물들이 살고 있는 동물원이다. 
컴포즈 파일은 세가지 서비스들을 가지는데 zookeeper, broker 그리고 kafka-tools다.    
- confluentinc/cp-zookeeper:5.4.0 : 야후 연구 개발팀에서 개발된 서비스로 분산 시스템이 안전하게 작동할 수 있는 간편한 API를 제공한다.  
- confluentinc/cp-server:5.4.0  
- confluentinc/cp-kafka:5.4.0
세 이미지를 사용한다. broker는 Apache Kafka고 Apache Zookeeper에 의존적 이어야 하기 때문에 compose file에서 dependency 를 건다.
## Start the Containers
~~~sh
docker-compose up -d 
~~~

## Create a Kafka Topic
get into the kafka container
~~~sh
docker exec -it kafka /bin/bash
~~~
create topic to-do-list.
- --bootstrap-server : connect to broker
- --replication-factor 1 : Replcation for Fault-Tolerant
- --partitions 2 : partition for topic
- --topic to-do-list : name of topic 
~~~sh
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic to-do-list 
~~~
check whether the topic was actually created or not
~~~sh
kafka-topics --list --bootstrap-server localhost:9092
# __confluent.support.metrics
# _confluent-license
# _confluent-metrics
# to-do-list

~~~
For more detailed information about topic
~~~sh
kafka-topics --describe --bootstrap-server localhost:9092 --topic to-do-list
~~~

## Send Messages to the topic 
kafka-console-producer 를 사용한다. key-value 메시지를 보낼 수 있다.
~~~sh
kafka-console-producer --topic to-do-list --bootstrap-ser localhost:9092 --property "parse.key=true" --property "key.separator=:"
~~~
~~~sh
>key1:val1
>key2:val2
>key3:val3
~~~
## Consume Message from the Topic
~~~sh
kafka-console-consumer --topic to-do-list --bootstrap-server localhost:9092 --from-beginning --property "print.key=true"
~~~
~~~sh
null	my second event
key2	val2
key3	val3
null	my first event
null	my third event
key1	val1
~~~
## Schema Registry
There is an implicit 'contract' that producers write data with a schema that can be read by consumers, even as producers and consumers evolve their schema. Schema Registry helps ensure that this contract is met with compatibility checks.     
It is useful to think about schemas as APIs. It provides centralized schema management and compatibility checks as schemas evolve. using avro.    
~~~sh
curl localhost:8081 # test
~~~
## Confluent Control Center로 Topic 생성
유료라는데...그래서 안되는 거닝...hlebalbau/kafka-manager:stable(It's yahoo's)를 사용함     
cp-kafa5.4.0 버전의 Kafka 버전은 2.4.0 이다.
[Reference3]('https://megazonedsg.github.io/kafka-prod-env/')

## Schema Registry UI 
[Reference4](https://lenses.io/blog/2016/08/schema-registry-ui/)
- Exploring and searching schemas
- Avro evaluation compatibility checks
- New schema registration
- Avro + Table Schema views
- Displaying CURL commands 
- A 15Mbytes Docker image (???)

## Mac OS X Install maven
~~~sh
brew install maven # 설치 명령어
mvn -version # 버전 확인 명령어
which mvn # 명령어 위치 확인하기
export M2_HOME=/usr/local/Cellar/maven/3.6.3_1/libexec
export M2=$M2_HOME/bin
export PATH=$PATH:$M2_HOME/bin
~~~
## Maven 프로젝트 생성하기
~~~sh
 mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-simple -DarchetypeVersion=1.4 \
-DgroupId=com.example.chapter4 -DartifactId=firstapp -Dversion=1.0-SNAPSHOT -DinteractiveMode=false
~~~

pom.xml에 컨플루언트 리포지토리를 추가한다. 
pom.xml에 kafka dependency도 함께 추가한다.
~~~xml
    <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-assembly-plugin</artifactId>
    <version>3.1.0</version>
    <configuration>
        <descriptorRefs>
            <!-- 이걸 지정해야 사용하는 lib을 포함하는 fat-jar가 만들어진다. -->
            <descriptorRef>jar-with-dependencies</descriptorRef>
        </descriptorRefs>
    </configuration>
    <executions>
        <execution>
        <phase>package</phase>
        <goals>
            <goal>single</goal>
        </goals>
        </execution>
    </executions>
    </plugin>
~~~
fat-jar 빌드 할 수 있어! 쏠 수 있어~!
~~~sh
mvn clean
mvn package -DskipTests # 제대로 빌드 되면 target 디렉토리 아래에 2개의 jar 파일이 생성된다.
~~~
실행 할 수 있어! 나 쏠 수 있어~!
~~~sh
java -cp ./firstapp-1.0-SNAPSHOT-jar-with-dependencies.jar com.example.chapter4.FirstAppProducer
~~~
