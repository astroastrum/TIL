## Django Logic

* 반드시 설계 먼저

* **로그인** 기능 로직
  * URL을 하고: /accounts/login/ 
  * 처리
    * (템플릿) 사용자에게 Form을 제공
  * URL: POST /accounts/login/ 요청이 들어오면 
    * 처리
      * (로그인) 로직을 처리 
        * 사용자인지 확인하고, django_session 테이블에 저장, 쿠키 주기
      * 로그인 한 행위가 완료되면 
        * (성공) 게시글 목록 페이지로 redirect
        * (실패) 로그인 Form



* 로그인 로직 코드

  ```django
  path('login/', views.login, name='login'),
  
  
  views.py
  def login(request):
  	return render(request, 'accounts/login.html')
  
  
  template
  login.html
  사용자 Form을 줘야 하는데 어떤 Form? Django가 제공하는 로그인 Form. 
  
  
  views.py
  from django.contrib.auth.forms import AuthenticationForm
  
  def login(request):
  	form = AuthenticationForm()
  	context = {
  		'form': form,
  	}
  	return render(request, 'accounts/login.html', context)
  
  
  
  login.html
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form %}
      {% bootstrap_button button_type="submit" content="OK" %}
  </form>
  
  
  아직 **로그인이 되는 로직**이 존재하지 않음. POST 요청을 했을 때, POST 요청을 처리할 수 있도록 해야함. (로그인이 되는 로직, POST 요청을 처리하는 로직)
  
  
  views.py
  
  def login(request):
  	# 만약에 request.method가
  	if request.method == 'POST':
  		# AuthenticationForm은 ModelForm이 아님
  		form = AuthenticationForm(request.POST)
  		# 유효성 검사
  		if form.is_valid():
  			# 세션에 저장, 
  			# login 함수는 request와 user객체를 인자로 받음
  			# user객체는 form에서 인증된 유저 정보를 받을 수 있음
  			# request의 사용자정보를 form으로부터 가지고 올 수 있음
  			# 첫번째: request, 두번째: 유저 정보
  			auth_login(request, form.get_user())
  			return redirect('articles:index')
  	else:
  		form = AuthenticationForm()
  	context = {
  		'form': form,
  	}
  	return render(request, 'accounts/login.html', context)
  
  
  
  유효성 검사 통과가 되지 않으면 login.html을 render. form = AuthenticationForm에 문제 있음. AuthenticationForm은 모델 form이 아님. 모델과 관련된 내용을 한 적이 없음. AuthenticationForm은 forms.form을 상속받고 있음.
  
  
  views.py
  from django.contrib.auth import login 추가.
  
  
  완벽하게 로그인 성공
  로그인 된 것이 맞는지 확인하기 위해 로그인된 사용자의 정보를 출력하기
  base.html
  
  <h1>{{ user }}</h1>
  
  
  ```

  * 로그인 할 때 중요한 것은 세션과 쿠키. http 요청에 대한 정보를 바탕으로 무엇인가를 판단해야함. 정보를 조작할 필요가 있는데 **request**가 제일 중요(먼저 들어옴)하고 그 다음에 **데이터(유저정보)**가 들어옴. 로그인을 하기 위해서 **로그인 함수**는 (쿠키가 있는)요청정보와 ,유저정보가 같이 있어야만 무엇인가를 해서 세션에 저장하고 쿠키에 관리할 수 있는 모습.  

* 로그아웃

  ```django
  로그인 버튼 만들기
  base.html
  # 로그인을 하지 않은 상태에서만 보여주기 위해 분기처리함. if문을 어떻게 해야하나?
  <a href="{% url 'accounts:login' %}">로그인</a>
  
  
  # 템플릿에서 사용할 수 있는 변수 값은 무엇인가? context.
  # 그 context에 포함되어 있는 친구들? 
  # 인증과 관련된 context를 처리해줌
  'context_processors': [
  	'django.contrib.auth.context_processors.auth'
  ]
  
  
  base.html
  # request.user는 어떤 객체? user객체가 가지고 있는 속성: is_authenticated 속성이 있음.
  {{ user }}도 되고 {{ request.user }}도 가능
  
  # if request.user가 인증이 되었다면, 
  {% if request.user.is_authenticated %}
  <span>{{ request.user }}</span>
  <a href="">로그아웃</a>
  {% else %}
  <a href="{% url 'accounts:login' %}">로그인</a>
  <a href="{% url 'accounts:signup' %}">회원가입</a>
  {% endif %}
  
  
  
  # 회원만 글 쓰기를 할 수 있게 하려면(보여주려면)
  {% if request.user.is_authenticated %}
  	<a href="{% url 'accounts:create' %}">글쓰기</a>
  {% endif %}
  {% for article in articles %}
  <h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr>
  {% endfor %}
  {% endblock %}
  
  
  
  articles/views.py
  
  # 글쓰기
  def create(request):
  	# '요청한 유저가 authenticated이면' 추가
  	if request.user.is_authenticated:
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
  		return render(request, 'articles/form.html', context=context)
  	else: #로그인 안되면 어떤 해결책?
  		# 다양한 해결책이 있음
  		# 접근 잘못했습니다 페이지를 보여줄 수도 있고
  		# return render(...)
  		# '또는 로그인하러 다시 가세요'도 가능
  		return redirect('accounts:login')
  
  
  
  
  
  articles/views.py
  # 수정페이지에서 작업을 해봄
  from django.contrib.auth.decorators import login_required
  
  #로그인이 필요함
  @login_required
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.user == article.user: 
          if request.method == 'POST':
              # POST : input 값 가져와서, 검증하고, DB에 저장
              article_form = ArticleForm(request.POST, request.FILES, instance=article)
              if article_form.is_valid():
                  # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                  article_form.save()
                  messages.success(request, '글이 수정되었습니다.')
                  return redirect('articles:detail', article.pk)
              # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
          else:
              # GET : Form을 제공
              article_form = ArticleForm(instance=article)
          context = {
              'article_form': article_form
          }
          return render(request, 'articles/form.html', context)
      else:
          # 작성자가 아닐 때
          # (1) 403 에러메시지를 던져버린다. 
          # from django.http import HttpResponseForbidden
          # return HttpResponseForbidden()
          # (2) flash message 활용!
          messages.warning(request, '작성자만 수정할 수 있습니다.')
          return redirect('articles:detail', article.pk)
  
  
  
  def login(request):
      if request.method == 'POST':
          # AuthenticationForm은 ModelForm이 아님!
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              # 세션에 저장
              # login 함수는 request, user 객체를 인자로 받음 
              # user 객체는 어디있어요? 바로 form에서 인증된 유저 정보를 받을 수 있음
              auth_login(request, form.get_user())
              # http://127.0.0.1:8000/accounts/login/?next=/articles/1/update/
              # request.GET.get('next') : /articles/1/update/
              return redirect(request.GET.get('next') or 'articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/login.html', context)
  
  def logout(request):
      auth_logout(request)
      messages.warning(request, '로그아웃 하였습니다.')
      return redirect('articles:index')
  
  ```

  * request.GET.get('next') : /articles/1/update/