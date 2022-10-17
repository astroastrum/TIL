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
  
  ```

  

* 이미지 업로드

  * 이미지를 DB에 저장하는 것
    * HTML Form(enctype)
    * VIEW(request FILES)
  * 이미지를 보여주는 것
    * static(정적파일)
      * ROOT/URL 설정