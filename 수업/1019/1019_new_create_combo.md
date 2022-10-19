## New + Create 

* New + Create 이전 

  ```python
  articles/views.py
  
  # ModelForm 활용
  def new(request):
    form = ArticleForm()
    context = {
      'form': form,
    }
    return render(request, 'articles/new.html', context)
  
  
  
  
  '''
  ModelForm 활용전 create 함수
  
  def create(request):
    # DB에 저장
    # 1. parameter로 날라온 데이터를 받아서
    # request GET에서 content 파라키터로 날라온 데이터를 잡아서 content에 넣으려고 한다
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    # 2. 데이터가 저장됨
    article = Article.objects.create(title=title, content=content)
    
    return redirect('articles:detail', article.pk)
    
    # article.pk 오류
    # return redirect('articles:detail', article.pk)
  '''
  
  
  
  
  # ModelForm 활용 후 create 함수의 변화
  def create(request):
    # 유효성 검사
    form = ArticleForm(request.POST)
    if form.is_valid():
      # DB에 저장
      article = form.save()
      return redirect('articles:detail', article.pk)
    return redirect('articles:new')
  ```

  

* New + Create 이후

  ```python
  # after new + create
  def create(request):
    if request.method == 'POST':
      form = ArticleForm(request.POST)
      if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
  
    else:
      form = ArticleForm()
    context = {
      'form': form,
    }
    return render(request, 'articles/create.html', context)
  ```

  