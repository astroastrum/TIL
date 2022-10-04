## Django

* 시작하기(기본 흐름) 

```
- 가상환경 및 Django 설치

1. 가상환경 설치
python -m venv venv

2. 가상환경 실행
source venv/Scripts/activate
* 가상환경 폴더를 .gitignore로 설정

3. 장고 설치
pip install django==3.2.13

4. 가상환경에서 '이것을 설치했다' 또는 '내가 활용하는 패키지기 이런것이다'에 관한 기록지 남기기
pip freeze > requirements.txt



- Django 프로젝트 생성

5. 장고 프로젝트 생성 
django-admin startproject pjt .

6. 서버 실행
python manage.py runserver

- 서버 로그
서버에 접속하는 모든 로그들이 기록된다
URL에 요청을 보내면 서버에 기록된다

```

* 앱 만들기

```
1. articles 앱 생성
python manage.py startapp articles

2. 앱 등록
INSTALLED_APPS에 등록

3. urls.py 설정
URL로 요청을 받아서 처리하고 응답한다
URL 설정을 App 단위로 하기 위해서 
프로젝트 폴더의 urls.py에 'URL관리는 articles 앱에서 하겠다'를 작성한다
articles 폴더에 urls.py를 추가한다

```

* Articles 앱의 Index

```
- 기본 흐름
url을 등록하고
view 함수 생성하며
template을 만든다

1. articles의 urls.py에서 '로컬호스트의 articles로 들어오면 어떠한 페이지를 처리하겠다'는 계획을 세운다

2. views.py로 이동해서 index 함수를 정의한다
요청 정보를 받아서 원하는 페이지를 render한다

3. articles 앱에 templates 폴더를 만들고 articles 폴더도 만들어서 이 폴더 안에 index.html을 만든다.

```

* 사용자의 요청

```
1. URL 요청을 보냄
2. 서버에 요청이 들어옴
3. URL 목록이 urlpatterns에 나옴
4. 목록 속에서 찾음
5. views의 index함수에 그 URL의 처리 정보가 있고 views에 있는 함수를 실행시킨다. 함수를 실행하면 articles의 index.html을 render해서 사용자에게 보여짐

```

* CRUD 기능 만들기

```
- CRUD = 데이터베이스에 생성, 조회, 수정, 삭제 기능

1. Article Model 생성(모델 정의)

  1-1) 기능 기획
  UI(User Interface)와 DB는 밀접한 관계
  어떠한 서비스를 제공할 것인가
  ex) 
  게시판 기능
  - 제목
  - 내용
  - 글 작성시간/수정시간


  1-2) class Article 정의 (DB 설계)
  models.py에 class Article 정의
  class Article은 models에 있는 Model을 상속받아서 만들겠다
  왜 상속을 받는가? 
  설계는 하지만 기능은 상속받기 위해서
  class Article(models.Model):


  1-3) Database에 반영
  Migration 파일 생성
  - python manage.py makemigrations
  DB 반영(migrate)
  - python manage.py migrate


  1-4) 실제 DB에 반영되었는지 확인
  - python manage.py showmigrations
  또는
  - db.sqlite3 확인


2. CRUD 기능 구현

2-1) Create(생성)이란?
- 2가지 기능 (사용자에게 HTML Form 제공하는 기능과 View함수로 DB에 저장하는(입력한 데이터를 처리하는) 기능)
- 사용자가 게시판에 글을 작성
- form으로 데이터를 입력 받아서 추가
- URL에 매핑되는 VIEW 함수는 반드시 1개, 기능을 새로 추가할 경우 URL을 추가하고 이 URL에 대응되는 View 함수를 새로 만들어야함

    2-1-1)
    urls.py에 설계
    http://127.0.0.1:8000/articles/new/


    2-1-2)
    views.py에서 new함수 정의


    2-1-3)
    new.html 생성
    - 사용자에게 <form> 제공 >>> 이곳에서 (http://127.0.0.1:8000/articles/new/)
    - 입력받은 데이터 처리 >>> 이곳에서 (http://127.0.0.1:8000/articles/create/) 
      create 경로를 new.html의 form action에 작성 ("/articles/create/") 또는 {% url 'articles:create' %}
      "/articles/create/"보다 'articles:create'을 사용하는 이유는 변수명으로 바꾸어서 편리하게 HTML에 적용하기 위함
      전자를 선택했을 경우 url의 이름이 변경되었을때 모든 파일에 적용된 해당 url의 이름을 변경해야함

    
    2-1-4)
    url.py에 경로 작성하고 views.py에 create함수 정의
    * path('create/', views.create, name='create'),
      - 참고
          요청 정보는 Request information, URL, views.py의 request 인자에서 확인 가능함
    * create 함수 정의 (GET에서 정보를 가져와서 DB에 저장)
    title = request.GET.get('title') > GET에서 'title' 요청 정보를 가져옴
    # DB에 저장
    Article.objects.create(title=title, content=content)


2-2) 게시글 목록 기능(작성한 글을 보여주는 기능)
DB에 있는 값을 꺼내서 Toss해야함. (게시글에 있는 것을 꺼낸다)
    -DB에서 값을 가져온다 
     articles = Article.objects.all()
    -Template에 context로 전달한다
     context = {'articles': articles}

```

