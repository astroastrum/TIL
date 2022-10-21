## 댓글 Comment

* 어떻게 시작하는가?

  ```html
  # articles/models.py
  
  class Comment(models.Model):
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  
  # 참고
  models.CASCADE
  아이디에 연결되어 있는 댓글까지 삭제가능하게 만든다
  
  
  
  # admin.py
  from .models import Article, Comment
  
  class CommentAdmin(admin.ModelAdmin):
      list_display  = ('content', 'created_at', 'article')
  
  admin.site.register(Comment)
  
  
  # admin django 관리
  댓글 추가 해보기
  
  
  
  python manage.py shell_plus
  # 참조: DB 조작하는 모든 파이썬 코드가 View에 있다
  
  Article.objects.all()
  # article 생성
  article = Article.objects.create(title='제목1', content='내용1')
  article 
  
  그렇다면 댓글(생성)은 어떻게 작성?
  1 이라는 내용을 게시글 13번에 작성하는 코드
  comment = Comment.objects.create(content='111', article=article)
  comment
  comment.article # 결과가 어떠함? Article: Article object (13)
  comment.article_id # 결과 13
  
  # comment 저장할 때 둘다됨, 필드 값을 기억해야함 (article_id)
  1. comment = Comment.objects.create(content='111', article=article)
  2. comment = Comment.objects.create(content='111', article_id=13)
  
  comment.article_id #결과? 13
  
  comment.article #결과 Article:Article object(13) 객체
  
  # 13번 게시글의 모든 댓글을 알고자 한다면 어떻게? (결과는 동일)
  Comment.objects.filter(article_id=13)
  # article 객체의 모든 댓글들 그래서 Foreign Key를 사용하는 것임
  article.comment_set.all()
  
  
  참조
  comment.article
  역참조
  article.comment_set
  
  
  --------------------------------------------------------------------------------------
  # 댓글 목록 
  article/detail.html
  
   <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  {% for comment in article.comment_set.all %}
      <p>{{ comment.content }}</p>
  {% endfor %}
  {% endblock %}
  
  
  ```

  
