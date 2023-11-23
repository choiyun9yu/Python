# Flask

## 1. What is Flask?
Flask는 파이썬에서 사용 가능한 웹 어플리케이션 프레임워크이다. Flask는 Werkzeug WSGI와 Jinja2 엔진에 의해 동작한다.

### 1-1. WSGI(Web Server Gateway Interface)
WSGI는 파이썬 웹 어플리케이션과 웹 서버 사이의 표준 인터페이스를 정의한 것이다. WSGI는 파이썬 언어로 작성된 웹 어플리케이션이 웹 서버와 통신하기 위한 규칙을 제공한다. (Django에서도 쓰임)   

WSGI의 목적은 다양한 웹 어플리케이션 프레임워크와 웹 서버 사이의 호환성을 보장하는 것이다. 즉, 웹 어플리케이션은 WSGI 인터페이스를 따르면 어떤 WSGI 호환 웹 서버에서도 동작할 수 있다.  

### 1-2. Werkzeug(워ㅋ즈-우ㄱ)
Werkzeug는 파이썬 웹 어플리케이션을 개발하기 위한 유틸리티 라이브러리이다. Werkzeug는 웹 프레임워크인 Flask의 기본 구성 요소 중 하나로 사용된다. 다시 말해 WSGI가 인터페이스를 설계할 때 지켜야할 규약이라면 Werkzeug는 규약을 지키며 설계하게 도와주는 도구이다. 대표적으로 request, response 같은 명령 실행은 Werkzeug를 통해 이뤄진다.

### 1-3 Jinja2
Jinja2는 파이썬에서 동작하는 templating 엔진이다. 특정 데이터와 template를 연결해서 flask에서 구현이 어려운 동적인 움직임을 지원한다. 
