from elasticsearch import Elasticsearch
import json

dict_data_path = '/Users/seokwoo/Personal/From_Nginx_To_API/es-engine/dict_data/가.data.json'
es = Elasticsearch([{'host' : 'localhost', 'port' : '9200'}])
es.indices.delete(index='dictionary')
es.indices.create(
    index = 'dictionary',
    body = {
        "settings": {
            "index" : {
                "analysis" : {
                    "analyzer" : {
                        "my_analyzer" : {
                            "type" : "custom",
                            "tokenizer" : "nori_tokenizer"
                        }
                    }
                }
            }
        },
        "mappings" : {
            #"dictionary_datas" : {
                "properties" : {
                    "title" : {
                        "type" : "text",
                        "analyzer" : "my_analyzer"  # title을 분석할 수 있도록 설정한다.
                    },
                    "link" : {
                        "type" : "text"
                    },
                    "description" : {
                        "type" : "text",
                        "analyzer" : "my_analyzer" # description을 분석할 수 있도록 설정한다.
                    },
                    "thumbnail" : {
                        "type" : "text"
                    }
                }
            #}
        }
    }
)

with open(dict_data_path, encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

    body = ""

    for idx, item in enumerate(json_data['items']):
        body = body + json.dumps({  "index" : { "_index" : "dictionary", "_id"  : idx}}) + '\n'
        body = body + json.dumps(item, ensure_ascii=False) + '\n'

    es.bulk(body)