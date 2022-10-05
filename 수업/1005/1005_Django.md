## Django

* **HTTP 요청**의 기본

  * Method

  * Path

  * Version of the protocol

  * Headers

    

* **Post** Method

  * GET은 조회 용도

    * ex) Article 객체를 조회

  * **Form을 통해서 제출할 때** Post 사용

    ```django
    <form action="{% url 'articles:create' %}" method="POST">
      <!-- POST method 사용시 csrf_token을 반드시 작성 -->
      <!-- create 함수에서 값을 받을 때 request.POST로 값을 받아서 처리 -->
      {% csrf_token %}
      <!-- csrf란? 
      input type="hidden"으로 만들어줌 
      POST 요청은 DB에 전송하기 위해 사용함
      혹시 요청이 들어왔을 때 다른 사이트에서 
      요청이 변조된 것이 아닌지 확인하는 로직 -->
      <label for="title">제목 : </label>
      <input type="text" name="title" id="title">
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글쓰기">
    </form>
    ```

  * GET과 _POST_의 차이점

    * URL 평점 **기록**_(등록)_
      * POST
        * 무언가를 **저장**하고 기록하는 기능
    * URL 평점 조회
      * GET
        * ex) Google 검색



* 서버측의 이중 검증
  * HTML에서 검증을 했더라도 서버측에서 이중 검증이 되어야 완전한 보안을 구현할 수 있습니다.



* ModelForm

  * ModelForm 선언

    * 선언된 모델에 따른 필드 구성
      1. Form 생성
         * 어떤 필드를 구성할 것인가 ('name', 'value') 
         * 어디로 보낼 것인가 ('action', 'method')
      2. 유효성 검사
  
    ```django
    from django import forms
    from .models import Article
    
    
    # ModelForm 선언
    class ArticleForm(forms.ModelForm):
      
      class Meta:
        model = Article
        # 선언된 모델에 따른 필드들
        fields = ['title', 'content']
    ```
  
    
  
  * 대체 기능
  
    ```django
    forms.py에서 
    
    from django import forms
    from .models import Article
    
    # 모델 form에 instance를 넘겨서 new.html의 form을 대체한다
    # template에 무언가를 넘기기 위해 context를 넘긴다 
    class ArticleForm(forms.ModelForm):
    
      class Meta:
        # Article model에 있는
        model = Article
        # 모든 필드를 내가 가져다가 사용하겠다
        fields = '__all__'
    
    
    new.html에서
    
    {{ article_form.as_p }}
    
    ```
  
    
  
  * 필드가 많을 경우 ModelForm에서 관리
  
  * 유효성 검사  
  
    * ex) Google에 로그인할 때
    * 유효성 검사가 실패했을 때 어떤 결과를 보여주기도 합니다.
  
    ```django
    def create(request):
      # 데이터의 개수가 많아지면 많아질수록 request.POST의 개수도 많아진다
      # article_form은 ArticleForm에 request.POST를 넘기고 
      # 만약에 article_form이 유효한지 검사할 수 있다
      # article_form = ArticleForm(request.POST)
    	if article_form.is_valid():
    	article.form.save()
    	# 유효하지 않을 경우 장고는 알림을 자동으로 해줌
    	else:
    		print('유효하지 않습니다')
        return redirect('articles:index')
    ```
  
    

* admin 사이트

  * http://localhost:8000/admin

  * admin.py에서 관리

  * 사용자 이름과 비밀번호 설정

    ```django
    python manage.py createsuperuser
    ```

    

  * admin 등록

    * 모델 **데이터베이스** 관리

      ```django
      # admin 사이트에 Article 등록
      admin.site.register(Article)
      ```

      

* 관리자 폼 커스터마이징

  ```django
  class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'created_at', 'updated_at']
  ```



* Static files

  * **정적 파일**에 대한 기능

  * settings.py의 STATIC_URL에 '/static/' 설정이 이미 존재

  * INSTALLED_APPS에 'django.contrib.staticfiles'는 정적 파일을 관리하는 것

  * articles에 images 파일 만들어서 이미지 삽입 가능

    ```django
    {% load static %}
    <img src="{% static 'images/autumn.jpeg' %}" alt="">
    ```

    

  * CSS 

    ```django
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    ```

    

* 배포

  * Bootstrap5

    * ```django
      {% load django_bootstrap5 %}
      {% bootstrap_css %}
      {% bootstrap_javascript %}
      {% bootstrap_form article_form %}
      ```

      