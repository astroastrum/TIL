* UD (posts 앱)

  ```django
  class Post(models.Model):
  	title = models.CharField(max_length=50)
  	content = models.TextField
  ```

  ```django
  posts/views.py
  
  def index(request):
  	# 모든 글 목록을 보여준다
  	# 1. DB에서 모든 글을 불러온다.
  	posts = Post.objects.all()
  	# 2. Template에 보내준다.
  	context = {
  		'posts': posts,
  	}
  	return render(request, 'posts/index.html', context)
  ```

  ```django
  index.html
  
  <h1>게시판</h1>
  <ul>
      {{ for post in posts }}
      <li>제목: {{ post.title }} | 내용: {{ post.content }}
     	<a href="">
         [수정]
      </a>/
      <a href="">
      	[삭제]
      </a>
      </li>
      {% endfor %}
  </ul>
  
  <a href="{% url 'posts:new' %}">새글쓰기</a>
  
  ```

  ```django
  posts/views.py
  from .models import Post
  
  def create(request):
  	# 1. parameter로 날라온 데이터를 받아서
  	title = request.GET.get('title')
  	content = request.GET.get('content')
  	
  	# 2. DB에 저장
  	# title='날라온 데이터'
  	Post.objects.create(title=title, content=content)
  	
  	context = {
  		'title': title,
  		'content': content,	
  	}
   	return render(request, 'posts/create.html', context)
  ```

  ```django
  posts/create.html
  
  <h1>작성 완료</h1>
  <p>제목: {{ title }}</p>
  <p>내용: {{ content }}</p>
  <a href="{% url 'posts:index' %}">목록으로</a>
  ```

  몇번째 글을 수정하고 지울것인지 URL 구성이 달라집니다. URL 구성 느낌: posts/update/ 1 

  ```django
  posts/urls.py
  
  urlpatterns = [
  	# id보다는 pk를 사용, pk는 자료형이 int
  	# id가 같이 넘어옴. views안의 delete라는 함수 안에서 삭제 핸들링하겠음.
  	path('delete/<int:pk>', views.delete, name='delete'),
  ]
  ```

  ```django
  posts/views.py
  
  def delete(request, pk):
  	# pk에 해당하는 글 삭제만 하면됨
  	# pk를 id에 넣어서 가져오고 삭제
  	Post.objects.get(id=pk).delete()
  	return redirect('posts:index')
  
  	
  ```

  * 9월 28일 참조

  ```django
  articles/index.html
  
  <ul>
      {% for post in posts %}
      <li>ID: {{ post.id }} |
          <a href="{% url 'posts:detail'% post.pk %}">
          제목: {{ post.title }}
          </a>
          <a href="">
            [수정]
          </a>
          <a href="{% url 'posts:delete' post.pk %}">
            [삭제]
          </a>   
      </li>
      {% endfor %}
  </ul>
  ```

  ```django
  articles/urls.py
  path('detail/<int:pk>, views.detail, name='detail')
  
  
  articles/views.py
  
      
  # 두번째 read
  # 하나의 데이터에 대한 정보를 출력
  def detail(request, pk):
      # 하나의 데이터에 대한 정보를 출력
  	# get() 메소드를 사용해서 특정 pk의 데이터를 불러온다
  	post = Post.objects.get(pk=pk)
      context = {
      	'post': post,
      }
  	return render(request, 'posts/detail.html', context)
  
  	
  ```

  ```django
  articles/urls.py
  
  path('edit/<int:pk>', view.edit, name='edit'),
  # 응답할 update함수
  path('update/<int:pk>', views.update, name='update'),
  
  
  
      
      
  articles/views.py
  
  # pk를 받고
  def edit(requeset, pk):
      	# get 메소드 사용해서 특정 pk 데이터를 받아옴
      	post = Post.objects.get(pk=pk)
      	context = {
      		'post': post,
      }
  	return render(request, 'posts/edit.html', context)
  
  
      
      
  # read + create + 알파
  def update(request, pk) :
      # update할 특정 데이터를 불러옴 -> pk 사용해서
      post = Post.objects.get(pk=pk)
      
      title = request.GET.get('title')
      content = request.GET.get('content')
      
      # 데이터를 수정
      # 내가 불러온 post의 title를 내가 받아온 title로 바꿈 
      post.title = title
      post.content = content
      
      # 데이터를 수정한 것을 반영
      post.save()
      
      #내가 불러온 post의 pk값 입력 가능
      return redirect('posts:detail', post.pk)
      
      
      
      
     
  
  articles/edit.html
  <h1>글 수정</h1>
  # 글을 수정하는 것은 특정 pk값을 가진 데이터를 수정하기 때문에 post.pk 필요 
  # 특정 pk를 가진 데이터를 불러오기 위해 pk를 동적인자로 전달
  <form action="{% url 'posts:update' post.pk %}">
      제목: <input type="text" name="title" value="{{ post.title }}"><br>
      내용: <textarea>{{ post.content }}</textarea>
      내용: <input type="text" name="content" value="{{ post.content }}">
      <input type="submit">  
  </form>
  
  
  
  	
  ```

  * 9월 29일 참조
  * POST 메소드 이후

  ```django
  urls.py
  
  path('<int:pk>/update/', views.update, name='update'),
      
      
  articles/views.py
  def update(request, pk):
     	article_form = ArticleForm()
      context = {
      	'article_form': article_form
      }
      return render(request, 'articles/update.html', context)
      
      
  
  Form에서 중요한 2가지 요소
      1. input (input의 name, value)
      2. action 메소드
      왜? 사용자가 입력한 값을 name으로 이름을 붙여서 어디로 보낼지(action) 어떠한 방식으로 보낼지(method)
      
     
      
  articles/update.html
  
      
  # 주의해야 할 점은 수정페이지에서 수정할 때 기존에 작성했던 글이 없기 때문에 def update에서 article = Article.objects.get(pk=pk)와 article_form=ArticleForm(instance=article)을 추가해야함
      
  <form action="{% url 'articles:update' %}" method="POST">
      {{ article_form.as_p }}
      <input type="submit" value="수정">
  </form>
      
      
      
  articles/views.py
  
  # 기존에 작성했던 글과 함께 수정가능
  def update(request, pk):
      article = Article.objects.get(pk=pk)
     	article_form = ArticleForm(instance=article)
      context = {
      	'article_form': article_form
      }
      return render(request, 'articles/update.html', context)
  
      
      
      
   # 유효성 검사를 추가하면
  def update(request, pk):
      if request.method == 'POST':
      	article_form = ArticleForm(request.POST)
      	if article_form.is_valid():
      		redirect('articles:detail', article.pk)
      else: #유효성 검사 통과하지 않으면, # GET : Form을 제공
     		article_form = ArticleForm(instance=article)
      context = {
      	'article_form': article_form
      }
      return render(request, 'articles/update.html', context)
  ```

  ```django
  Create 생성
  	1. UI 제공 new
  	2. DB 저장 create
  	
  Read(detail) 조회 (특정한 글을 본다)
  	1. DB에서 특정 가져와서 조회
  
  Delete
  	1. DB에서 특정 가져와서 삭제
  
  Update
  	1. UI 제공 edit
  	2. DB 저장 update
  
  
  ****************************근데 ModelForm이 장고에서 등장함*****************************
  
  Model에 정의된 필드에 맞춰서 
  	- UI를 그려주고 
  	- 유효성 검사하며 
  	- DB에 저장가능
  
  
  그래서
  Create 생성 (GET, POST 요청에 따라서 바꾸고)
  	1. UI 제공 new        > GET
  	2. DB 저장 create 	> POST 
  
  
  Update (GET, POST 요청에 따라서 바꿔서 같은 view 함수에서 처리)
  	1. UI 제공 edit		> GET
  	2. DB 저장 update		> POST
  
  
  예시)
  
  1. GET 요청일 때 처리 흐름
  2. POST 요청일 때 처리 흐름
  	2-1. valid할때
  	2-2. invalid할때
  
  def create(request):
  	if request.method == 'POST':
  		article_form = ArticleForm(request.POST)
  		if article_form.is_valid():
  			article_form.save()
  			return redirect('articles:index')
  	else:
  		article_form = ArticleForm()
  	context = {
  		'article_form': article_form
  	}
  	return render(request, 'articles/new.html', context=context)
  
  
  
  ```

  ```django
  articles/new.html
  
  <h1>글쓰기</h1>
  
  <!-- form : 사용자에게 양식을 제공하고
  	값을 받아서(input: name, value)
  	서버에 전송(form: action) -->
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">제목: </label>
      <input type="text" name="title" id="title">
      <label for="content">내용: </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글쓰기">
  </form>
  
  
  articles/views.py
  
  def new(request):
  	return render(request, 'articles/new.html')
  ```

  ```django
  articles/views.py
  
  def index(request):
  	articles = Article.objects.order_by('-pk')
  	context = {
  		'articles': articles
  	}
  	return redirect(request, 'articles/index.html', context)
  
  
  
  articles/index.html
  <h1>
      게시판
  </h1>
  <a href="{% url 'articles:new' %}">글 쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title }}</h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr>
  {% endfor %}
  ```

  ```django
  articles/views.py
  
  # 수정이라고 하는 행위는 기존에 있는 instance를 수정하는 것
  def update(request, pk):
  	# 기존의 글을 수정하는 것
  	# 특정한 글을 수정하려는 것이니까 반드시 instance정보를 같이 넘겨주어야함.
  	article = Article.obejcts.get(pk=pk)
  	if request.method == 'POST':
  		# POST: input값 가져와서, 검증하고, DB에 저장
  		# 사용자로부터 값을 가지고와서
  		article_form = ArticleForm(request.POST, instance=article)
  		if article_form.is_valid():
  			# 유효성 검사 통과하면 상세보기 페이지로 전환
  			redirect('articles:detail', article.pk)
  	# 분기
  	else:
  		article_form = ArticleForm(instance=article)
  	context = {
  		'article_form': article_form
  	}
  	return render(request, 'articles/update.html', context)
  
  ```

  ```django
  정리
  
  
  Create 생성
  	1. UI 제공 new
  	2. DB 저장 create
  	그래서 해당하는 url과 view가 2개 있었음
  
  Read 조회(detail, 상세보기)
  	1. DB에 특정 가져와서 조회
  	
  Delete
  	1. DB에서 특정 가져와서 삭제
  
  Update 
  	1. UI 제공 edit
  	2. DB 저장 update
  
  
  근데 ModelForm이 장고에서 등장 ~
  
  
  ModelForm은 Model에 정의된 필드에 맞춰서 
  	- UI를 그려주고
  	- 유효성 검사하고
  	- DB에 저장도됨
  
  
  코드단순화
  유효성 검사할때 같이 처리하게 만들음. GET, POST 요청에 따라서 바꾸고 같은 함수에서 처리. 
  
  Create 생성
  	1. UI 제공 new		> GET
  	2. DB 저장 create		> POST
  
  
  Update 
  	1. UI 제공 edit		> GET
  	2. DB 저장 update		> POST
  ```

  