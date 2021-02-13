
## Nori 형태소 분석기 플러그인
mecab-ko-dict-dictionary를 형태소 분석기로 사용     

ori analyzer는 아래와 같이 구성된다.
- nori_tokenizer
- nori_part_of_speech token filter
- nori_readingfrom token filter
- nori_number token filter

노리 토크나이저는 ```decompound_mode```와 ```user_dictionary```을 지원한다.     
노리 파트 오브 스피치는 ```stoptags```를 지원한다.

> decompound_mode : 복합 명사를 처리하는 방식(none, discard, mixed)

> user_dictionary : 사용자 사전 정의

ES 샘플 CURL

```
curl -X GET "$HOSTNAME:9200/_analyze?pretty" -H 'Content-Type: application/json' -d'
{
  "tokenizer": "nori_tokenizer",
  "text": "뿌리가 깊은 나무는",
  "attributes" : ["posType", "leftPOS", "rightPOS", "morphemes", "reading"],
  "explain": true
}
```

Initialize

```
  django-admin.py startproject server_project
  cd server_project
  python manage.py startapp search_app
```

Sample Request
```
  curl localhost:8000/?search=감동
```



