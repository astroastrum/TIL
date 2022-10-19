## Edit + Update

* before edit + update

  ```python
  articles/views.py
  
  def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
      'article': article,
      'form': form,
    }
    return render(request, 'articles/edit.html', context)
  
  
  
  # ModelForm 활용한 UPDATE
  def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  
    context = {
      'article': article,
      'form': form,
    }
    return render(request, 'articles/edit.html', context)
  
  
  
  ```

  

* after edit + update

  ```python
  def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
  
    else:
      form = ArticleForm(instance=article)
    context = {
      'form': form,
      'article': article,
    }
    return render(request, 'articles/update.html', context)
  
  ```

  