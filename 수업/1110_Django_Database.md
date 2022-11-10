## 데이터베이스

* 블로그 글

  * 블로그 글은 작성자, 작성일, 제목, 본문 등의 정보가 있습니다. 블로그 글을 작성한 사람이 있다면 작성한 사람의 id, 비밀번호, 이메일 등의 정보도 필요합니다. 이와 같은 정보를 저장하고 관리하려면 데이터베이스를 사용해야 합니다.

* 테이블

  * 가로 방향(행): 레코드
  * 세로 방향(열): 필드

* id

  * 고유한 필드 = primary key

* 외래키 foreign key 

  * User 테이블의 id가 2번인 작성자가 Post 테이블의 작성자 필드에 2번으로 저장되어 있을 경우

* 테이블 종류

  * User 
    * 작성자 또는 운영자
      * 필드 종류
        * id, username, password, email
  * Post
    * 블로그 글
      * 필드 종류
        * id, title, content, author, create_at(작성일)
  * Comment
    * 댓글
      * 필드 종류
        * id, post, author, create_at

* models.py

  ```python
  from django.db import models
  
  # Post 모델은 models 모듈의 Model 클래스를 확장해서 만든 파이썬 클래스
  class Post(models.Model):
      title = models.CharField(max_length=30)
      content = models.TextField()
  ```

* models.py

  ```python
  class Post(models.Model):
      title = models.CharField(max_length=30)
      content = models.TextField()
  
      def __str__(self):
          return f'[{self.pk}]{self.title}'
  
  모델이 만들어지면 자동으로 pk필드도 생성됩니다. pk는 각 레코드에 대한 고유값이며 블로그 글이 처음 작성되면 첫번째 pk가 자동으로 주어집니다. pk값을 통해서 블로그 글의 번호와 제목을 문자열로 나타냅니다.
  self.pk는 해당 포스트의 pk값(포스트 번호)이고 self.title은 포스트 제목입니다.
  
  ```

* views.py

  ```python
  from .models import Post
  # models.py에 작성한 Post 모델을 import합니다.
  
  
  def index(request):
      # Post 레코드 전부를 불러와서 posts에 저장하고 딕셔너리 타입으로 보냅니다.
      # 데이터베이스에 쿼리를 이런 방식으로 보내서 필요한 레코드를 불러올 수 있습니다.
      posts = Post.objects.all()
      return render(request, 'articles/index.html', {'post': posts,})
  
  
  
  ```

* html에 for문 사용해서 Post 레코드 뿌리기

  ```html
  {% for p in posts %}
  	<h3>{{ p }}</h3>
  {% endfor %}
  
  Post 레코드들을 뿌립니다
  ```

* html에 for문 사용해서 Post 필드 뿌리기

  ```html
  {% for p in posts %}
  	<h3>{{ p.title }}</h3>
  	<h4>{{ p.content }}</h4>
  {% endfor %}
  ```

* views.py

  ```python
  def detail(request, pk):
      # pk를 매개변수로 받습니다.
      # Post 모델의 pk 필드 값이 update함수의 매개변수로 받은 pk와 같은 레코드를 가져오세요
      post = Post.objects.get(pk=pk)
      return render(request, 'articles/detail.html', {'post': post})
  ```

* detail.html

  ```html
  def detail(request, pk):
  	post = Post.objects.get(pk=pk) 했을 경우
  
  <h1>{{ post.title }}</h1>
  <h2>{{ post.content }}</h2>
  포스트의 title, content 필드
  ```

  