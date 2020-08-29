# 누가 요새 장고를 쓰나?! 플라스크!!!
1. Global Object : g, Application Context - 모든 요청들이 공유하는 영역
2. Session Context - 사용자가 서버에 붙으면 서버는 세션을 하나 열어준다. 브라우저 하나당 세션하나 열린다. 세션 내 공유하는 공간 
3. request(요청) -> Server -> response(응답)
4. wsgi ( WebServer Gateway Interface)
5. Request Event Handler
    ~~~python

    @app.before_first_request # 사용자가 이 요청을 처음 부를때 실행
    def ... # 예시 ) 웹페이지 인코딩 수정

    @app.before_request # 매번 요청을 보내기 전에, 라우터가 모델에 보내기 전에
    def ... # 예시 ) DB Connection

    @app.after_request # response가 나가기 직전에 실행
    def ...(response) # 예시 ) DB Close

    @app.teardown_request # request에서 response 까지 다 끝나고 destroy.
    def ...(exception)

    @app.teardown_appcontext # application context가 destroy 시에
    def ...(exception)
    ~~~
6. Routing
    ~~~python

    @app.route('/test')
    def ...

    @app.route('/test', methods=['POST', 'PUT' ])

    # 파라미터
    @app.route('/test/<tid>')
    def test3(tid):
        print("tid is", tid)

    # page ... 없으면 index
    @app.route('/test/, defaults={'page': 'index'})
    @app.route('/test/<page>')
    def ...

    @app.route('/test', host='abc.com')
    @app.route('/test', redirect_to='/new_test')
    ~~~
7. sub-domain
    blog.naver.com 에서 blog는 서브 도메인이다.   
    서브 도메인 별 다른 처리가 가능하자나
    ~~~python
    @app.route("/", subdomain="blog")
    def naverblog():
        return "Hello blog.naver.com!!!"
    ~~~

8. Request Parameter
    ...get('<param name>', <default-value>, <type>)
    methods: get, getlist(리스트), clear, etc

    ~~~python
    # GET ,,, args
    request.args.get('q')

    # POST ,,, form
    request.form.get('p', 123)

    # GET or POST ,,, values
    # values를 사용하면 GET이든 POST든 파라미터는 다 받는다.
    request.values.get('v')

    # Parameters
    request.args.getlist('qs')
    ~~~
7. request.environ
8. xhr
9. response
    리스폰스 구조
    - headers
    - status
    - status_code
    - data
    - mimetype
    ~~~python
    res = Response("Test")
    res.headers.add("Program-Name", "Test Response")
    res.set_data("This is Test Program.")
    res.set_cookie("UserToken", "A12Bc9")
    ~~~
10. Cookie, IndexedDB, Storage

    Cookie Argument
    - key
    - value
    - max_age
    - expires
    - domain
    - path

    ~~~python
    res = Response("Test")
    res.set_cookie("UserToken", "A12Bc9")

    # other request
    request.cookies.get("UserToken", "A12Bc9")
    ~~~

11. Session
    서버 메모리에 떠있는 singletone 객체, 서버에다 심어놓는 쿠키와 같음
    시크릿 키를 동반해야한다. 