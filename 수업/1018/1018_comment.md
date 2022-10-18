## 댓글 Comment

* 관계형 *데이터베이스*

  * 표

    * 데이터는 행으로 쌓인다

    * column에 어떠한 모습들이 있다

      

* 테이블 간 관계 예시

  | 주문 id | 제품명     | 주문일     | 배송일     | 주문상태    |
  | ------- | ---------- | ---------- | ---------- | ----------- |
  | 1       | 립톤복숭아 | 2022-10-18 | 2022-10-19 | 상품 준비중 |
  | 2       | 민트초코   | 2022-10-18 | 2022-10-19 | 배송중      |

  * 동일한 이름을 가진 고객이 있을 경우, 고객 정보(id)를 저장합니다.



* RDB

  * 1:1

    * One-to-one relationships

  * 1:N

    * one-to-many relationships

  * M:N

    * Many-to-many relationships

      

* 어떻게 시작하는가?

  ```python
  articles앱의 models.py에
  
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      
      
  python manage.py makemigrations
  python manage.py migrate
  
  python manage.py runserver
  articles/admin에 등록
  
  from .models import Article, Comment
  
  admin.site.register(Comment)
  
  
  python manage.py shell_plus
  Article.objects.all()
  Article.objects.create(title='제목1', content='내용1')
  article = Article.objects.create(title='제목1', content='내용1')
  article
  
  comment = Comment.objects.create(content='111', article=article)
  comment
  comment.article
  comment.article_id
  comment = Comment.objects.create(content='111', article_id=13)
  
  Comment.objects.filter(article_id=13)
  article.comment_set.all()
  exit()
  
  
  articles/detail.html에서
  <h4 class="my-3">댓글</h4>
    <hr>
    {% for comment in article.comment_set.all %}
      <p>{{ comment.content }}</p>
      <hr>
    {% endfor %}
  
  
  또는
  views.py에서 def detail에
  def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
      'articles': article,
      'comments': article.comment_set.all(),
      'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
  
  
  
  또는
  <h4 class="my-3">댓글</h4>
    <hr>
    {% for comment in comments %}
      <p>{{ comment.content }}</p>
      <hr>
    {% endfor %}
  
  
  
  
  articles/forms.py에
  from .models import Article, Comment
  
  class CommentForm(forms.ModelForm):
  
    class Meta:
      model = Comment
      fields = ['content',]
      
      
  def detail에 comment_form = CommentForm()추가
  
  def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
      'article': article,
      'comments': article.comment_set.all(),
      'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
  
  
  
  
  detail.html에 <form action=""></form>추가
  
  <form action="">
      {% bootstrap_form comment_form %}
      <input type="submit">
    </form>
  
  
  
  articles의 urls.py에
  path('<int:pk>/comments/', views.comment_create, name='comment_create') 추가
  
  
  views.py에
  def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit-False)
      comment.article = article
      comment.save()
    return redirect('articles:detail', article.pk)
  ```

  