## Profile Page

* 어떻게 시작하는가

  ```python
  urls.py에
  
  urlpatterns = [
    path('signup', views.signup, name='signup'),
    # User 상세보기
    # integer로 pk를 받는다
    path('<int:pk>/', views.detail, name='detail'),
  ]
  
  
  detail.html 생성
  {% extends 'base.html' %}
  {% block body %}
    <h1>{{ user.username }}님의 프로필</h1>
  {% endblock body %}
  
  
  views.py에서
  # detail 함수에서 User 참조할 때 from .models import User 사용금지
  # from .models import User 사용금지
  from django.contrib.auth import get_user_model
  
  def detail(request, pk):
    # User 정보를 받아오는 쿼리셋 API 
    # User class 참조할 때 어떻게 작성? from .models import User가 아닌 from django.contrib.auth import get_user_model
    # user = User.objects.get(pk=pk), User가 아닌 get_user_model()
    user = get_user_model().objects.get(pk=pk)
    context = {
      'user': user
    }
    return render(request, 'accounts/detail.html', context)
  ```

  