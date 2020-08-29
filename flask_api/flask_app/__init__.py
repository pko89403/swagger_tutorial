from flask import Flask
from flask import g
from flask import Response, make_response 
from flask import request

from datetime import datetime, date, timedelta

from flask_restplus import Api, Resource, fields

app = Flask(__name__)

api = Api(app) # flask restplus 의 시작 

api_model = api.model('Language', {'language' : fields.String('The language.')})
app.debug = True # 디버그 할때 써래 


@api.route('/language')
class Language(Resource):
    def get(self):
        return languages
    @api.expect(api_model)
    def post(self):
        langauges.append(api.payload)
        return {'result' : "Language added"}, 201

app.config.update(
    SECRET_KEY='X1243yRH!mMwf',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31) # 31 days
)
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

@app.route('/req_param')
def rp():
    p = request.args.get('p')
    return "p= %s" % str(p)

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식 : " + str(datestr)

@app.route('/req_env')
def req_env():
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
            'SERVER_NAME: %(SERVER_NAME) s <br>') % request.environ

@app.route('/w_cookie')
def w_cookie():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123X'

    return make_response(res)

@app.route('/r_cookie')
def r_cookie():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie['" + key + "] = " + val + " , " + session.get('Token')

@app.route('/d_session')
def d_session():
    if( session.get('Token') ):
        del session['Token']
    return "Session이 삭제되었습니다."


@app.route("/")
def start():
    return "start flask!"

    