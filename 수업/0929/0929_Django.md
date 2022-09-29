## Django

* 핵심 명령어

  ```django
  mkdir [폴더 이름]
  폴더 생성
  
  cd [폴더 이름]/
  만든 폴더로 들어감
  
  pip list
  장고에 뭐가 설치되어 있는지 확인
  
  python -m venv [가상환경 이름]
  사용할 수 있는 가상환경 만듬
  작동된 상태는 아님
  venv 모듈을 활용하고 venv 옆에 가상환경 이름을 붙임
  
  
  source [가상환경 이름]/Scripts/activate
  가상환경 작동
  
  가상환경이란?
  개발자의 세계에서 sandboxing이라고 불리우는데 글로벌 환경에 영향을 주거나 영향을 받지 않는 나만의 가상공간
  
  
  pip install django==3.2.13
  장고 설치 
  가상환경이어서 글로벌 환경에는 설치 불가
  
  
  django-admin startproject [프로젝트 이름][시작경로]
  예) startproject testpjt01 .
  프로젝트 생성과 시작 경로 지정
  
  code .
  
  python manage.py runserver
  장고 서버 실행
  
  ```

  

* 앱 만들기 위한 명령어

  ```django
  python manage.py startapp [앱 이름]
  ex) python manage.py startapp articles
  글을 게시할 수 있는 게시글 앱 생성
  
  settings.py에서 앱 등록
  예) INSTALLED_APPS = [
  	'articles'
  ]
  
  
  앱을 삭제할 경우
  1. INSTALLED_APPS에서 삭제한 후 저장
  2. articles 폴더를 삭제하고 저장
  ```

  