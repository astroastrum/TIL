## Login, Logout

* 어떻게 시작하는가?

  ```python
  python manage.py runserver
  
  localhost/admin
  
  로그인이 이미 되어있음
  = DB에 django_session에 저장 되어있음
  로그아웃 해보면
  django_session이 비어져있다
  
  
  # 확인 참고
  INSTALLED_APPS에
  'django.contrib.sessions'은 세션관리하는 것
  
  MIDDLEWARE에
  'django.contrib.sessions.middleware.SessionMiddleware'도 중간에 세션처리
  'django.middleware.csrf.CsrfViewMiddleware' CSRF 처리
  'django.contrib.auth.middleware.AuthenticationMiddleware' 인증처리
  MIDDLEWARE란?
  요청이 들어오면 MIDDLEWARE 순서대로 어떤 사이에 처리해야 될 것들을 처리해준다
  응답하면 MIDDLEWARE 역순으로 처리한다
  요청과 응답을 처리할 때 
  요청오면 검토해서 처리하고 응답할 때도 검토해서 처리한다
  
  
  #로그인 로직 참고
  - URL: GET/accounts/login/
  - FORM(처리)
  	- (Template) 사용자에게 Form을 제공
  - URL: POST /accounts/login/
  	- (로그인) 로직처리 
      	- 사용자인지 확인하고, django_session 테이블에 저장, 쿠키 제공
      
  - 로그인 행위가 완료되면
  	- 게시글 목록 페이지로 redirect
      
      
  urls.py에
  urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # User 상세보기
    # integer로 pk를 받는다
    path('<int:pk>/', views.detail, name='detail'),
  ]
  
  
  views.py에
  def login(request):
    return render(request, 'accounts/login.html')
  
  
  login.html 생성
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  {% block body %}
    <h1>로그인</h1>
  {% endblock body %}
  
  
  이제 사용자 form을 제공해야 하는데 어떤 form을 제공해야함?
  장고에서 제공하는 로그인 form
  
  views.py에서
  # 로그인 form
  from django.contrib.auth.forms import AuthenticationForm
  
  def login(request):
    form = AuthenticationForm()
    context = {
      'form': form
    }
    return render(request, 'accounts/login.html', context)
  
  
  login.html에서 
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  {% block body %}
    <h1>로그인</h1>
    <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form %}
      <input type="submit" content="OK">
    </form>
  {% endblock body %}
  
  
  아직은 로그인이 되지 않는다
  로그인 되는 로직을 추가해야한다
  
  def login(request):
      # 로그인 로직 추가
      if request.method == 'POST':
          form = AuthenticationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')    
      else:
      # form 처리 한다고 로그인이 되는 것은 아니여서 로작을 추가해야 한다
          form = AuthenticationForm()
      context = {
        'form': form
      }
      return render(request, 'accounts/login.html', context)
  
  
  이렇게 작성하면 유효성 검사 통과가 되지 않아서 오류가 발생한다
  
  # 로그인 세션
  from django.contrib.auth import login as auth_login
  
  def login(request):
      # 로그인 로직 추가
      if request.method == 'POST':
          # AuthenticationForm은 ModelForm이 아님
          # data의 argument로 request에 POST가 들어올 것 같음
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              # ModelForm이 아니라서 save() 없음
              # form.save()
              # 이곳에 들어갈 로직은?
              # 세션에 저장, 로그인 함수가 내장되어 있음
              # User정보를 form으로부터 가져올 수 있음
              # login 함수는 request와 user 객체를 인자로 받음
              # user 객체는 form에서 인증된 user 정보를 받을 수 있음
              auth_login(request, form.get_user())
              return redirect('articles:index')    
      else:
      # form 처리 한다고 로그인이 되는 것은 아니여서 로작을 추가해야 한다
          form = AuthenticationForm()
      context = {
        'form': form
      }
      return render(request, 'accounts/login.html', context)
  
  
  admin 로그아웃하고
  signup에서 회원가입하고
  accounts/login 들어가서
  아이디, 비밀번호 입력하면 목록으로 이동함 
  그리고 세션이 추가됨
  로그인 성공
  
  # 사용자 로그인 정보 표시
  로그인 성공되었는지 모든 페이지에 사용자의 로그인 정보를 표시해보겠다
  base.html에 추가
  <h1>{{ user }}</h1>
  
  # AnonymousUser 정보 표시
  다시 localhost/articles/에 들어가서
  쿠키를 삭제하면 
  모르는 사람 = AnonymousUser로 
  
  로그인 성공
  ```

  

* Logout 어떻게 시작하는가?

  ```python
  base.html
  
  {% load django_bootstrap5 %}
  <!DOCTYPE html>
  <html lang="en">
  
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      {% bootstrap_css %}
      {% block css %}{% endblock css %}
    </head>
  
    <body>
      <p>{{ user }}</p>
      <div class="container my-5">
        {% block body %}{% endblock body %}
      </div>
      {% bootstrap_javascript %}
    </body>
  
  </html>
  
  
  로그인 회원가입 버튼 만들기
  
  base.html에
  
  {% load django_bootstrap5 %}
  <!DOCTYPE html>
  <html lang="en">
  
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      {% bootstrap_css %}
      {% block css %}{% endblock css %}
    </head>
  
    <body>
      <p>{{ user }}</p>
      <!-- 회원가입 링크 -->
      <a href="{% url 'accounts:signup' %}">회원가입</a>
      <!-- 로그인 링크 -->
      <a href="{% url 'accounts:login' %}">로그인</a>
      <div class="container my-5">
        {% block body %}{% endblock body %}
      </div>
      {% bootstrap_javascript %}
    </body>
  
  </html>
  
  
  if문을 사용함
  base.html
  
  {% load django_bootstrap5 %}
  <!DOCTYPE html>
  <html lang="en">
  
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      {% bootstrap_css %}
      {% block css %}{% endblock css %}
    </head>
  
    <body>
      <!-- 로그아웃 -->
      <!-- request.user가 인증이 되었다면 -->
      <!-- 회원가입 들어가서 로그인 인증이 되면 로그아웃 표시 -->
      {% if request.user.is_authenticated %}
        <span>{{ request.user }}</span>
        <a href="">로그아웃</a>
      {% else %}
        <!-- 회원가입 링크 -->
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <!-- 로그인 링크 -->
        <a href="{% url 'accounts:login' %}">로그인</a>
      {% endif %}
  
      <div class="container my-5">
        {% block body %}{% endblock body %}
      </div>
      {% bootstrap_javascript %}
    </body>
  
  </html>
  
  
  request.user는 user객체
  User 객체가 가지고 있는 속성은 is_authenticated
  
  
  
  로그인 한 상태에서 로그인 페이지로 가려면?
  articles/index.html에서
  
  <h1>게시판</h1>
    <!-- 만약에 request.user가 authenticated면 그때만 보여줌 -->
    {% if request.user.is_authenticated %}
      <a href="{% url 'articles:create' %}">글 쓰기</a>
    {% endif %}
  
  
  
  # 접근 제한 막기
  글쓰기(articles/create)으로 이동하는 것을 막으려면?
  views.py의 create함수에서
  def create(request):
      # 로그인이 되면
      if request.user.is_authenticated:
          if request.method == 'POST':
            article_form = ArticleForm(request.POST)
            # article_form이 유효한지 검사
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:index')
          else: # 유효하지 않다면
              article_form = ArticleForm()
          context = {
            'article_form': article_form
          }
        
          return render(request, 'articles/form.html', context=context)
      else:
        # 로그인 안되면 접근 잘못했습니다 페이지를 보여줌
        # return render() 또는 return redirect()
        # 로그인 창으로 보내려면
          return redirect('accounts:login')
  
      
  수정페이지
  views.py에서
  from django.contrib.auth.decorators import login_required
  
  
  @login_required
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          # POST : input 값 가져와서, 검증하고, DB에 저장
          article_form = ArticleForm(request.POST, instance=article)
          if article_form.is_valid():
              # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
              article_form.save()
              return redirect('articles:detail', article.pk)
          # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
      else:
          # GET : Form을 제공
          article_form = ArticleForm(instance=article)
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/form.html', context)
  
  
  URL의 어떤 부분이 다른가?
  로그인 하고나서 뭐가 다른가?
  요청을 보냈을 때 어떤 코드의 순서를 거치는가?
  
  def login(request):
      # 로그인 로직 추가
      if request.method == 'POST':
          # AuthenticationForm은 ModelForm이 아님
          # data의 argument로 request에 POST가 들어올 것 같음
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              # ModelForm이 아니라서 save() 없음
              # form.save()
              # 이곳에 들어갈 로직은?
              # 세션에 저장, 로그인 함수가 내장되어 있음
              # User정보를 form으로부터 가져올 수 있음
              # login 함수는 request와 user 객체를 인자로 받음
              # user 객체는 form에서 인증된 user 정보를 받을 수 있음
              auth_login(request, form.get_user())
              # request.GET.get('next') : /articles/1/update/
              # request.GET.get('next'), 이 값에 따라서 조건문을 만든다
              if request.GET.get('next'):
                  return redirect(request.GET.get('next'))
              else:
                  return redirect('articles:index')   
      else:
      # form 처리 한다고 로그인이 되는 것은 아니여서 로작을 추가해야 한다
          form = AuthenticationForm()
      context = {
        'form': form
      }
      return render(request, 'accounts/login.html', context)
  
  
  
  코드를 줄일 수 있다
  def login(request):
      # 로그인 로직 추가
      if request.method == 'POST':
          # AuthenticationForm은 ModelForm이 아님
          # data의 argument로 request에 POST가 들어올 것 같음
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              # ModelForm이 아니라서 save() 없음
              # form.save()
              # 이곳에 들어갈 로직은?
              # 세션에 저장, 로그인 함수가 내장되어 있음
              # User정보를 form으로부터 가져올 수 있음
              # login 함수는 request와 user 객체를 인자로 받음
              # user 객체는 form에서 인증된 user 정보를 받을 수 있음
              auth_login(request, form.get_user())
              # request.GET.get('next') : /articles/1/update/
              # request.GET.get('next'), 이 값에 따라서 조건문을 만든다
              return redirect(request.GET.get('next')) or 'articles:index') 
      else:
      # form 처리 한다고 로그인이 되는 것은 아니여서 로작을 추가해야 한다
          form = AuthenticationForm()
      context = {
        'form': form
      }
      return render(request, 'accounts/login.html', context)
  
  
  create함수 변화
  
  @login_required
  def create(request):
      if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        # article_form이 유효한지 검사
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
      else: # 유효하지 않다면
          article_form = ArticleForm()
      context = {
        'article_form': article_form
      }
    
      return render(request, 'articles/form.html', context=context)
  ```

  

  