from flask import Flask
from flask import g
from flask import Response, make_response 

app = Flask(__name__)
app.debug = True # 디버그 할때 써래 

# request 요청을 실행하기 전에 한번 해줘
@app.before_request
def before_request(): 
    print("before request!!!")
    g.str = "한글" 


# Route 컨트롤 - URI 지정
@app.route("/gg") # 처음에
def start_with_g():
    return "start flask!" + getattr(g, 'str', '111')
    

@app.route("/res_test1")
def res_test1():
    # response header {'test' : 'ttt'}
    custom_res = Response("Custom Response", 200, {'test':'ttt', 'test2':'ttt2'})
    return make_response(custom_res)

# WebServer Gateway Interface 많이 쓴다.
@app.route('/test_wsgi')
def wsgi_test():
    # environ : 플라스크의 환경 변수, start_response : 콜백 함수 
    def application(environ, start_response): # inner function
        body = 'The Request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Context-Type', 'text/plain'),
                    ('Context-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]
    return make_response(application)

@app.route("/")
def start():
    return "start flask!"

    