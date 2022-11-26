## 단계적 이해

* urlpatterns

  ```django
  pjt/urls.py
  
  # 주문 들어오면 articles의 index로 보내자
  urlpatterns = [
  	path('index/', views.index)
  ]
  ```

  

* Index, Welcome 함수 로직 정의

  ```django
  from django.shortcuts import render
  
  # 무조건 첫번째 인자로 request를 받음
  # request로 요청한 사람의 정보(요청에 관련된 정보)가 들어옴, 하나의 객체화되서 들어옴
  # 장고가 요청정보를 부름
  def index():
  	# view에서 처리한 데이터를 index.html에 보냄.
  	# context의 딕셔너리 데이터를 index.html에 보내겠다, 넘기겠다.
  	context = {
  	'name': 'vanilla',
  	'img': 'https://cdn.jpg',
  	}
  	
  	# 환영하는 페이지 렌더
  	return render(request, 'index.html', context)
  ```

  ```django
  articles/templates/index.html
  
  <body>
      <h1>{{ 변수명 작성 }} 님, Welcome</h1>
      <h1>{{ name }}님, Welcome</h1>
      <img src="http://cdn.jpg">
      또는
      <img src={{ img }}">
  </body>
  ```

  ```python
  import random 
  
  def index():
  	names = ['vanilla', 'strawberry', 'delight']
      
      name = random.choice(names)
      
      # view에서 처리한 데이터를 index.html에 보냄.
  	# context의 딕셔너리 데이터를 index.html에 보내겠다, 넘기겠다.
  	context = {
  	'name': name,
  	'img': 'https://cdn.jpg',
  	}
  	
  	# 환영하는 페이지 렌더
  	return render(request, 'index.html', context)
  
  
  
  # welcome함수는 name이라고 하는 사용자들의 입력값을 사용할 것이다 
  def welcome(request, name):
      # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 렌더
      # name을 print해본다
      print(name)
      # 사람들이 입력한 값
      context = {
          'name': name,
      }
      return render(request, 'welcome.html', context)
  	# context로 넘어온 데이터를 template에서 활용해야함
  ```

  ```django
  articles/templates/welcome.html
  
  <body>
      <h1>{{ 변수명 작성 }} 님, Welcome</h1>
      <h1>{{ name }}님, Welcome</h1>
  </body>
  ```

  ```django
  def welcome(request, name):
      # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 렌더
      # name을 print해본다
      print(name)
      # 사람들이 입력한 값
      context = {
          'name': name,
  		'greetings': [
  			'안녕', 'hello', 'hi',
  		]
  		'img1': [
  		'https://.jpg'
  		'https://.jpg'
  		]
      }
      return render(request, 'welcome.html', context)
  	# context로 넘어온 데이터를 template에서 활용해야함
  ```

  ```django
  articles/templates/welcome.html
  
  <body>
      <h1>{{ 변수명 작성 }} 님, Welcome</h1>
      <h1>{{ name }}님, Welcome</h1>
      <p>{{ greetings }}</p>
      {% for greeting in greetings %}
      <p>{{ greeting }}</p>
      {% endfor %}
  </body>
  ```

  

  

* Ping, Pong 로직 (Retrieving the Data)

  ```django
  ping.html
  
  #ping에서 데이터를 입력해서 pong에서 데이터를 받아야함
  # 입력하면 pong 페이진로 데이터 보냄
  # 데이터를 어떠한 방식으로 보낼것인가? GET or POST
  <form action="/pong">
      이름을 입력해주세요: <input type="text" name="ball"> # 텍스트 입력창
      <input type="submit">  # 제출 버튼
  </form>
  ```

  /pong: /ping으로부터 전달받은 데이터를 활용하여 '000 님 환영합니다'를 작성하고 사용자의 이름을 사용

  ```django
  urls.py
  pong이라고 하는 url을 사용할 것이다. views.pong
  path('pong/', views.pong),
  
  
  views.py
  def pong(request):
  	# ping에서 보내온 데이터를 부름
  	# request로부터 가져옴
  	# request라고하는 객체 안에 GET이라고 하는 property에 접근하면 어떤 데이터의 딕셔너리가 나옴. ex) {'ball': ['john']}
  	# (사용자가 입력한 데이터) = 넘겨받은 사람들의 이름 'ball'
  	ball = request.GET.get('ball')
  	context = {
  		'name': ball,
  	}
  	return render(request, 'pong.html', context)
  ```

  ```django
  pong.html
  
  <body>
      <h1>{{ 변수명 작성 }} 님, Welcome</h1>
      <h1>{{ name }}님, Welcome</h1> 
  </body>
  ```

  

* Article 모델 선언하기 전의 index.html과 create.html

  ```django
  index.html
  
  {% extends 'base.html' %}
  {% block content %}
  <h1>
      방명록
  </h1>
  <h2>글 목록</h2>
  {% for content in 방명록 %}
  <p>{{ content }}</p>
  {% endfor %}
  
  <h1>글 작성</h1>
  <form action="/articles/create/" method="GET">
      <input type="text" name="content">
      <input type="submit">
  </form>
  {% endblock %}
  ```

  ```django
  create.html
  
  <h1>작성 완료</h1>
  <p>작성 내용: {{ content }}</p>
  <a href="/articles">방명록으로 돌아가기</a>
  ```

  

* models.py

  ```django
  class Article(models.Model):
  	content = models.TextField()
  ```

  ```django
  from .models import Article
  
  def index(request):
  	# DB에서 가져오기
  	방명록 = Article.objects.all()
  	# SELECT * FROM articles;
  
  	return render(request, 'articles/index.html', {'방명록': 방명록})
  
  
  def create(request):
  	# 내가 작성한 내용
  	# content가 날라오는데 ('content')는 url로 날아온 파라미터 컨텐트, content = 는 내가 작성한 내용
  	# 오른쪽부터 천천히 읽는다
  	# request.GET에서 content 파라미터로 날라온 데이터를 잡아서 content에 넣으려고함. 이것을 template에 content라는 이름으로 사용하려고함 
  	content = request.GET.get('content')
  	# 사용자가 글 작성하고 나면 무조건 하드디스크에 영구 저장해야함/담아두어야 휘발성이 없음
  	# DB에 저장
  	# Article아 만들어줘. 레코드 하나만 만들게. 인자 하나를 넣는다. content의 content.
  	Article.objects.create(content=content)
  
  	return render(request, 'articles/create.html', {'content': content})
  ```

  ```django
  index.html
  
  {% extends 'base.html' %}
  {% block content %}
  <h1>
      방명록
  </h1>
  <h2>글 목록</h2>
  {% for content in 방명록 %}
  # 사용자가 작성한 모든 content를 렌더
  <p>{{ content.content }}</p>
  {% endfor %}
  
  <h1>글 작성</h1>
  <form action="/articles/create/" method="GET">
      <input type="text" name="content">
      <input type="submit">
  </form>
  {% endblock %}
  ```

  ```django
  create.html
  
  <h1>작성 완료</h1>
  <p>작성 내용: {{ content }}</p>
  <a href="/articles">방명록으로 돌아가기</a>
  ```

  

* 9월 27일 참조