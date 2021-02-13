FROM elasticsearch:7.10.1
ENV xpack.security.enabled=false 
ENV discovery.type=single-node

WORKDIR /usr/share/elasticsearch

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch analysis-nori

EXPOSE 9200 9201 9300 9301