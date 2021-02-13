import requests, json
from pprint import pprint 
URL = 'https://openapi.naver.com/v1/search/encyc.json'

client_id = # NaverOpenAPI ID
client_secret = # NaverOpenAPI Secret 
dict_data_path = 'dict_data/'

def get_naverOpenAPI_dictionary(query):
    headers = { 'X-Naver-Client-Id' : client_id,
                'X-Naver-Client-Secret' : client_secret}


    params = {  'query' : query,
                'display' : 100,
                'start' :   1000}

    resp = requests.get(URL, headers=headers, params=params)

    #print(resp.request)
    #print(resp.status_code)
    content = resp.content


    filename = f"{dict_data_path}/{query}.data.json"
    with open(filename, 'wb') as f:
        f.write(content)

    return filename

def test(test_query = '가'):
    filename = get_naverOpenAPI_dictionary(test_query)

    with open(filename, encoding='utf-8') as test_json:
        test_results = json.loads(test_json.read())['items']

    for text in test_results:   print(text)

if __name__ == '__main__':
    test(test_query='가')

