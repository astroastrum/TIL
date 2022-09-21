## Django

* Django 어떻게 시작하는가?

  ```django
  Git Bash
  
  pwd
  ~의 절대경로를 확인합니다.(print working directory)
  
  mkdir [폴더명]
  원하는 폴더를 만듭니다.
  ex) mkdir principio
  
  cd [폴더명]/
  principio 폴더에 작업영역 이동합니다.
  
  python --version
  파이썬이 설치되어 있는지 확인합니다.
  
  python -m venv [가상환경 이름]
  가상환경 venv 모듈을 사용합니다.
  가상환경이 만들어진 상황
  예) python -m venv principio-venv
  
  source principio-venv/Scripts/activate
  가상환경 실행
  
  cd principio/
  
  pip install django==3.2.13
  django 설치합니다.
  
  pip list
  django 설치 확인합니다.
  
  django-admin startproject principiopjt .
  새로운 웹서비스를 만들기 위해서 [프로젝트이름][시작경로]를 작성합니다.
  
  code .
  VScode를 엽니다.
  
  python manage.py runserver
  웹 서버가 돌아가는 파일을 실행합니다.
  
  localhost:8000
  브라우저에 내컴퓨터 주소와 8000을 입력합니다.
  
  Git bash 종료는 Cnt+C
  ```



* Framework

  * 서비스 개발을 발전시키기 위해서 전세계 개발자들이 엄청난 노력을 해왔습니다. 즉, 개발자들이 편리하게 사용할 수 있는 좋은 구조의 코드가 이미 만들어져서 이와 같은 서비스 개발에 필요한 기본 틀을 가지고 원하는 웹 서비스 개발을 할 수 있게 되었습니다. 

    

* Django

  * Django는 **서버를 실현하는 웹 프레임워크**입니다.

  

* 클라이언트

  * Request

    * 클라이언트는 원하는 것을 요청하는 고객입니다. 인터넷과 연결이 되어있는 폰과 컴퓨터, 그리고 다양한 브라우저도 클라이언트 입니다.

      

* 서버

  * Response

    * 클라이언트의 요청에 응답하는 서비스 제공자입니다. 앱과 웹 페이지를 보관하는 컴퓨터도 서버인데 클라이언트가 요청하면 클라이언트의 웹 브라우저에서 서버의 웹페이지 사본을 응답받는 형태입니다. 

    