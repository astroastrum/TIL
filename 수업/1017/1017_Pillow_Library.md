## Image Upload

* 어떻게 시작하는가?

  ```python
  # Pillow Library 설치
  # 왜? 이미지 관리 위해서
  pip install Pillow
  
  pip freeze > requirements.txt
  
  # ImageField 지정
  # 사용자가 업로드한 이미지를 어디로 업로드하게 할것인가?
  models.py에
  image = models.ImageField(upload_to='images/', blank=True)
  
  
  python manage.py makemigrations
  python manage.py migrate
  
  
  
  # form에 반영
  # forms.py에 'image' 추가
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = ['title', 'content', 'image']
          
          
  
  # 게시글 저장은 되지만 image는 받지 못하는 상황
  # DB에 image 저장이 되지 않는 상태
  # 저장이라는 행위
  # article_form을 제대로 받았는지 확인
  # enctype
  # 파일 데이터는 multipart/form-data 값지정 필요
  form.html에 enctype="multipart/form-data" 추가
  
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {% bootstrap_form article_form %}
      <input type="submit">
  </form>
  
  
  
  # 요청 정보에서 변한 부분이 있다
  # FILES가 생겼다
  # FILES는 어떻게 받나?
  views.py에 request.FILES 추가
  
  def create(request):
      if request.method == 'POST':
          article_form = ArticleForm(request.POST, request.FILES)
          # images 폴더에 이미지가 들어옴
          # 이미지를 서버에 받을 수 있게됨
          print(request.FILES)
          if article_form.is_valid():
              article_form.save()
              return redirect('articles:index')
      else:
            article_form = ArticleForm()
      context = {
          'article_form':article_form
      }
        
      return render(request, 'articles/form.html', context=context)
  
  
  
  
  # detail.html에 <img src="{{ article.image.url }}" alt="{{ article.image }}"> 추가
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>{{ article.pk }}번 게시글</h1>
    <p>{{ article.content }}</p>
    <!-- 이미지 추가하면 보이지 않고 받아갈 수 없음 -->
    <!-- 장고 서버에는 이미지가 저장되어 있는데 서버에서 서빙을 해 줄 설정이 되지 않았음 -->
    <!-- 그래서 MEDIA_ROOT와 MEDIA_URL 설정 필요 -->
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
    <a href="{% url '' article.pk %}">수정하기</a>
  {% endblock %}
  
  
  
  
  settings.py에서 MEDIA_ROOT와 MEDIA_URL 설정
  # Media files (user uploaded files)
  # MEDIA_ROOT라고 하는것은 경로를 BASE_DIR에 images라고 적고 
  # MEDIA_URL은 /media/
  MEDIA_ROOT = BASE_DIR / 'images'
  MEDIA_URL = '/media/'
  
  
  
  
  pjt/urls.py에 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 추가
  
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  
  
  # 이미지 업로드 완료
  
  
  
  # articles/models.py에 image = ProcessedImageField로 변경
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      image = ProcessedImageField(upload_to='images/', blank=True,
                                  processors=[ResizeToFill(1200, 960)],
                                  format='JPEG',
                                  options={'quality': 80})
      
      
  # imagekit installation
  pip install django-imagekit
  
  
  # URL 설정
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
  ```

  

* articles/models.py

  ```python
  articles/models.py
  
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  from django.db import models
  
  # Create your models here.
  # 1. 모델 설계 (DB 스키마 설계)
  from django.conf import settings
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      image = ProcessedImageField(upload_to='images/', blank=True,
                                  processors=[ResizeToFill(1200, 960)],
                                  format='JPEG',
                                  options={'quality': 80})
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
                              
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

  

* articles/forms.py

  ```python
  from django import forms
  from .models import Article, Comment
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = ['title', 'content', 'image']
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment 
          fields = ['content',]
  ```

  

* articles/views.py

  ```python
  from xml.etree.ElementTree import Comment
  from django.shortcuts import render, redirect
  from django.contrib import messages
  from django.contrib.auth.decorators import login_required
  from .models import Article
  from .forms import ArticleForm, CommentForm
  
  # Create your views here.
  
  # 요청 정보를 받는다
  def index(request):
      # 게시글을 가져온다
      articles = Article.objects.order_by('-pk')
      # Template에 전달한다. 
      context = {
          'articles': articles
      }
      return render(request, 'articles/index.html', context)
  
  # def new(request):
  #     article_form = ArticleForm()
  #     context = {
  #         'article_form': article_form
  #     }
  #     return render(request, 'articles/new.html', context=context)
  
  @login_required
  def create(request):
      if request.method == 'POST':
          article_form = ArticleForm(request.POST, request.FILES)
          if article_form.is_valid():
              article = article_form.save(commit=False)
              # 로그인한 유저는 작성자
              article.user = request.user 
              article.save()
              messages.success(request, '글 작성이 완료되었습니다.')
              return redirect('articles:index')
      else: 
          article_form = ArticleForm()
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/form.html', context=context)
  
  def detail(request, pk):
      # 특정 글을 가져온다.
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      # template에 객체 전달
      context = {
          'article': article,
          'comments': article.comment_set.all(),
          'comment_form': comment_form,
      }
      return render(request, 'articles/detail.html', context)
  
  @login_required
  def update(request, pk):
      article = Article.objects.get(pk=pk)
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
          # (2) flash message 활용
          messages.warning(request, '작성자만 수정 가능.')
          return redirect('articles:detail', article.pk)
  
  @login_required
  def comment_create(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.user = request.user
          comment.save()
      return redirect('articles:detail', article.pk)
  ```

  

* articles/detail.html

  ```python
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block body %} 
  <h1>{{ article.title }}</h1>
  <p>{{ article.pk }}번 게시글</p>
  <h3><a href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}</a></h3>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }} | {{ article.updated_at|date:"y-m-d D" }}</p>
  <p>{{ article.content }} </p>
  
  {% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
  {% endif %}
  
  
  {% if request.user == article.user %}
  <p>
      <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  </p>
  {% endif %}
  <h4 class="my-3">댓글</h4>
  {% if request.user.is_authenticated %}
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
      {% csrf_token %}
      {% bootstrap_form comment_form layout='inline'%}
      {% bootstrap_button button_type="submit" content="OK" %}
  </form>
  {% endif %}
  <hr>
  {% for comment in comments %}
      <p> {{ comment.user.username }} | {{ comment.content }}</p>
      <hr>    
  {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
  {% endfor %}
  {% endblock %}
  ```

  

* 이미지 업로드

  * 이미지를 DB에 저장하는 것
    * HTML Form(enctype)
    * VIEW(request FILES)
  * 이미지를 보여주는 것
    * static(정적파일)
      * ROOT/URL 설정