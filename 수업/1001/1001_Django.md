## Django

* Django ORM 

  * 방명록에 글을 작성하면 영구 저장되는 것이 아니라 바로 사라집니다. 작성한 글을 영구 저장하기 위해서 Django의 ORM을 사용합니다.

    ```django
    index.html 파일에
    
    <div>
        <h1>방명록</h1>
    </div>
    <div>
        <h2>글 작성</h2>
        <form action="/articles/create/" method="GET">
            <input type="text" name="content">
            <input type="submit">
        </form>
    </div>
    
    models.py 파일에 모델을 등록해서 영구 저장합니다.
    
    class Article(models.Model):
    	content = models.TextField()
    ```

    

* Create

  * 방명록에 글을 작성하면 작성한 글을 볼 수 있습니다. 이와 같이 작성된 내용이 화면에 보이게 하려면 index에서 받은 데이터를 request를 통해 꺼내서 사용해야합니다. 

    ```django
    views.py에
    
    def create(request):
    	# index에서 받은 content 데이터를 사용
    	content = request.GET.get('content')
    	guestbook.append(content)
    	# 템플릿에서 content 사용
    	return render(request, 'articles/create.html'), {'content: content'}
    ```

    

* App 등록

  * 앱을 만들면 바로 settings.py에 등록합니다.

    ```django
    python manage.py startapp articles
    
    settings.py에 앱 등록
    'articles'
    ```

    