## 회원가입

* Django Auth [인증과 권한을 총괄]

  * 인증[Authentication]
    * 웹사이트에 인증된 사람인가? [ex) 로그인]
    * INSTALLED_APPS > 'django.contrib.auth'
      * 유저/인증과 관련된 내용
  * 권한[Authorization]
    * 같이 인증을 받은 사람인데 각자의 권한이 다름
    * 일반회원/관리자
  * Admin
    * createsuperuser
    * 기본 내장된 어떠한 기능이 있고 auth app이 있음
      * 'django.contrib.admin'
  * 암호화
    * user에 관한 정보[비밀번호]
      * DB에 그대로 저장하면 문제 발생

  

* accounts app 생성 및 등록

  * python manage.py startapp accounts
  * INSTALLED_APPS = ['accounts']
  * pjt/urls.py/urlpatterns = [path('accounts/', include('accounts.urls')]
  * accounts/urls.py/
    * app_name = 'accounts'
    * urlpatterns = []

  

* DB 조작 (**커스텀 유저 모델**: 맞춤 설정)

  * accounts/models.py

    ```django
    # class User 정의
    # User에 들어가는 필드들
    # 이미 User 모델이 존재했음 > (SQLITE EXPLORER)auth_user에 id, password, email이 이미 존재함. 내장되어 있는 uesr모델을 사용할 수 있음.
    # auth_user = 앱이름_모델이름
    # auth_user을 사용하려면 클래스 상속받아서 활용.
    # 이렇게 하기 위해서 기본 설정이 필요 [공식문서에는 (User 모델) import]
    # 객체를 보면 객체로 무엇을 할 수 있는지 판단해야함. 다양한 속성과 메소드가 있음.
    # User 모델 활용할 때 Custom  User Model로 대체해서 활용할 것임.
    # User Model과 관련된 설정을 settings.py에 작성
    # accounts 앱에 있는 User가 이제부터 내가 사용할 사용자 정보
    AUTH_USER_MODEL = 'accounts.User'
    
    
    # 내부에 있는 모델을 가져옴
    # AbstractUser상속받기
    # 프로젝트 시작할 때 설정하기
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    class User(AbstractUser):
    	pass
    	
    ```

    

* Superuser
  * python manage.py createsuperuser
    * DB에 admin 저장됨



* AbstractUser란?
  * User에 대한 다양한 필드 설정이 가능
    * 장고 공식문서에 class AbstractUser 클릭해서 다양한 필드 설정 확인 가능
    * AbstractBaseUser를 상속받고 있음
      * AbstractBaseUser는 models.Model을 상속받고 있음
        * 상속 구조 (내림 상속)
          * models.Model 
          * class AbstractBaseUser
            * 비밀번호/인증
            * 비밀번호만 상속받고 싶으면 AbstractBaseUser만 사용 가능
          * class AbstractUser **커스텀**
            * username, email
          * class User



* Shell_Plus 사용하기 **(User 객체 활용)**
  * pip install ipython
    * pip freeze > requirements.txt
      * python manage.py shell_plus
        * 모델을 자동으로 불러옴
        * articles에서 게시글을 작성하기 위한 코드
          * Article.objects.create(title='제목1', content='내용1')
        * User는 objects.create할 때 어떤 정보가 있어야하나?
          * User.objects.create(username='sun', password='1q2w3e5t')
          * 이렇게 작성하면 비밀번호가 그대로 저장되어서 User는 create를 사용할 때 password는 암호화하는 로직 자체가 들어가야하기 때문에 장고가 **추가적인 설정**을 지원함.
            * PBKDF2 알고리즘
              * 역산 불가능





* 회원가입 기능 구현

  * url 생성

    ```django
    accounts/urls.py
    import django.urls import path
    from . import views
    
    urlpatterns = [
    	path('signup/', views.signup, name='signup'),
    ]
    ```

    ```django
    accounts/views.py
    from django.shortcuts import render
    
    def signup(request):
    	return render(request, 'accounts/signup.html')
    ```

    ```django
    templates/accounts 폴더 생성
    signup.html 생성
    
    {% extends 'base.html' %}
    
    # 회원가입에 필요한 form을 제공해주어야함. 회원가입 Form은 User와 연결된 모델 Form이 필요함. 
    {% block body %}
    {% endblock body %}
    
    
    # 회원가입에 필요한 form을 제공해주어야함. 회원가입 Form은 User와 연결된 모델 Form이 필요함. 그래서
    
    accounts/views.py
    from django.contrib.auth.forms import UserCreationForm
    def signup(request):
    	form = UserCreationForm()
    	# context에 form을 넘김
    	context = {
    		'form': form
    	}
    	return render(request, 'accounts.signup.html', context)
    
    ```

    ```django
    accounts/signup.html
    
    {% extends 'base.html' %}
    {% load django_bootstrap5 %}
    
    # 회원가입에 필요한 form을 제공해주어야함. 회원가입 Form은 User와 연결된 모델 Form이 필요함. 
    {% block body %}
    {{ form.as_p }}
    # 사용자 이름, 비밀번호, 비밀번호 확인 렌더
    {% endblock body %}
    ```

    또는 부트스트랩으로 장식된 form 렌더 가능

    ```django
    accounts/signup.html
    
    {% extends 'base.html' %}
    {% load django_bootstrap5 %}
    
    # 회원가입에 필요한 form을 제공해주어야함. 회원가입 Form은 User와 연결된 모델 Form이 필요함. 
    {% block body %}
    <form action="" method="POST">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="OK" %}    
    </form>
    # 사용자 이름, 비밀번호, 비밀번호 확인 렌더
    {% endblock body %}
    ```

    ```django
    포스트 요청처리/유효성 검사
    포스트 요청처리/유효성 검사
    포스트 요청처리/유효성 검사
    accounts/views.py [포스트 요청 처리][나중에 UserCreationForm에서 CustomUserCreationForm으로 변경]
    
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm
    
    def signup(request):
    	# POST 요청 처리
    	# if request의 method가 POST라면, 그때는 회원가입 처리를 해주어야함. 
    	# 나머지 GET요청일때는 form을 넣어서 처리함.
    	if request.method == 'POST'
    		# 사용자가 입력한 값(request.POST)을 받아서 form에 입력을 넣어주고 
    		from = UserCreationForm(request.POST)
    		# 만약에 form이 is valid 유효한가?
    		if form.is_valid():
    		# 유효하면 form save
    			form.save()
    			# articles의 index로 보냄
    			return redirect('articles:index')
    	else: # GET 요청일때는 
    		form = UserCreationForm()
    	# context에 form을 넘김
    	context = {
    		'form': form
    	}
    	return render(request, 'accounts.signup.html', context)
    ```

    ```python
    accounts/forms.py
    
    # form을 상속 받음
    # UserCreationForm은 (forms.ModelForm) 모델폼을 상속받고 있음
    # 모델 폼은 class Meta:
            		model = User이기 때문에
    # 다시 form을 상속받아야함
    
    from django.contrib.auth.forms import UserCreationFrom
    from .models import User
    
    def CustomUserCreationForm(UserCreationForm):
        
        class Meta:
            model = User
            fields = '__all__' 
            
    
    또는
    def CustomUserCreationForm(UserCreationForm):
        
        class Meta:
            model = User
            fields = ('username',) 
            
    ```

    ```python
    accounts/views.py [form을 CustomUserCreationForm으로 변경]
    
    from django.shortcuts import render, redirect
    # from django.contrib.auth.forms import UserCreationForm
    from .forms import CustomUserCreationForm
    
    def signup(request):
    	# POST 요청 처리
    	# if request의 method가 POST라면, 그때는 회원가입 처리를 해주어야함. 
    	# 나머지 GET요청일때는 form을 넣어서 처리함.
    	if request.method == 'POST'
    		# 사용자가 입력한 값(request.POST)을 받아서 form에 입력을 넣어주고 
    		from = CustomUserCreationForm(request.POST)
    		# 만약에 form이 is valid 유효한가?
    		if form.is_valid():
    		# 유효하면 form save
    			form.save()
    			# articles의 index로 보냄
    			return redirect('articles:index')
    	else: # GET 요청일때는 
    		form = CustomUserCreationForm()
    	# context에 form을 넘김
    	context = {
    		'form': form
    	}
    	return render(request, 'accounts.signup.html', context)
    
    ```

    admin에서 회원가입에 관한 정보를 보고 싶을 경우

    ```python
    from django.contrib import admin
    from .models import User
    
    # admin에서 사용자를 등록하여 사용자를 볼 수 있음
    admin.site.register(User)
    ```





* ArticleForm과 CustomUserCreationForm의 **차이점**

  ```django
  articles/forms.py
  * ArticleForm(forms.ModelForm):
    * 원래는 내가 직접 forms.ModelForm을 상속해서 만들었다면
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  	
  	class Meta:
  		model = Article
  		fields = ['title', 'content']
  
  
  accounts/forms.py
  * CustomUserCreationForm(UserCreationForm)
    * 이미 만들어진 UserCreationForm을 바탕으로 상속받아서 내가 커스텀해서 만들음
  
  
  from django.contrib.auth.forms import UserCreationForm
  from .models import User
  
  class CustomUserCreationForm(UserCreationForm):
  	class Meta:
  		model = User
  		fields = ('username',)
  ```

  

  

* Article(models.Model)과 User(AbstractUser)의 **차이점**

  ```django
  articles/models.py
  from django.db import models
  
  class Article(models.Model):
  	title = models.CharField(max_length=20)
  	content = models.TextField()
  	created_at = models.DateTimeField(auto_now_add=True)
  	updated_at = models.DateTimeField(auto_now=True)
  
  
  accounts/models.py
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
  	pass
  ```

  



* django.contrib.auth.get_user_model() 사용하기

  * 직접 참조하지 않도록 model에서 User를 사용할 때 get_user_model을 호출하면 리턴값이 settings.py의 AUTH_USER_MODEL = 'accounts.User'를 의미함.

  ```django
  accounts/admin.py
  
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from django.contrib.auth import get_user_model
  
  # get_user_model 호출
  admin.site.register(get_user_model, UserAdmin)
  ```

  ```django
  accounts/forms.py
  
  from django.contrib.auth.forms import UserCreationForm
  # from .models import User
  from django.contrib.auth import get_user_model
  
  # get_user_model 호출
  class CustomUserCreationForm(UserCreationForm):
  	class Meta:
  		model = get_user_model()
  		fields = ('username',)
  ```

  



* 프로필(회원정보) 페이지 구현하기

  * 기능을 만들려면 URL을 먼저 정의함

    * URL: /accounts/1/ 1번 사용자

      ```django
      accounts/urls.py
      
      urlpatterns = [
      	path('signup/', views.signup, name='signup'),
      	path('<int:pk>/', views.detail, name='detail'),
      ]
      
      ```

      

  * view 이름을 detail

    ```django
    # from .models import User
    from django.contrib.auth import get_user_model
    
    
    # pk받아옴
    def detail(request, pk):
    	# 유저 정보를 받아오는 쿼리문, 쿼리셋 API
    	# User 클래스를 사용할 때 상속을 받고 있으니 get_user_model을 사용
    	user = get_user_model().objects.get(pk=pk)
    	# user = User.objects.get(pk=pk)
    	context = {
    		'user': user
    	}
    	
    	# 유저정보를 불러와서 return render
    	return render(request, 'accounts/detail.html')
    ```

    

  * template 반환: 사용자 정보(username) 노출

    ```django
    {% extends 'base.html' %}
    {% block body %}
    <h1>
        {{ user.name }}님의 프로필
    </h1>
    ```

    



* articles/views.py와 accounts/views.py 비교하기

  * User class 참조하는 방법만 다르고 다 같음

    ```django
    accounts/views.py
    
    def detail(request, pk):
    	user = get_user_model().objects.get(pk=pk)
    	context = {
    		'user': user
    	}
    	return render(request, 'accounts/detail.html', context)
    
    ```

    ```django
    articles/views.py
    
    def detail(request, pk):
    	article = Article.objects.get(pk=pk)
    	context = {
    		'article': article
    	}
    	return render(request, 'articles/detail.html', context)
    ```

    

* 수업 1011 참조