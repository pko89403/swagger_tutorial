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
