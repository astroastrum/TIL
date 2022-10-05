## ModelForm

* forms.py에서

  ```django
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
  	class Meta:
  		# Article model에 있는 (어떠한 DB의)
  		model = Article
  		# 모든 필드를 내가 가져다가 사용하겠다 (어떠한 필드)
  		fields = '__all__'
  		# fields = ['title', 'content']
  ```



* views.py에서

  ```django
  def create(request):
  		# 사용자의 input 값을 받아서
  		article_form = ArticleForm()
  	context = {
  		'article_form': article_form
  	}
  	return render(request, 'articles/new.html', context=context)
  ```

  

* new.html에서

  ```django
  <h1>글쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {{ article_form.as_p }}
      <input type="submit" value="글쓰기">
  </form>
  ```

  