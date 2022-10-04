## Django

* **HTTP 요청**의 기본

  * Method

  * Path

  * Version of the protocol

  * Headers

    

* **Post** Method

  * GET은 조회 용도

    * ex) Article 객체를 조회

  * **Form을 통해서 제출할 때** Post 사용

    ```django
    <form action="{% url 'articles:create' %}" method="POST">
      <!-- POST method 사용시 csrf_token을 반드시 작성 -->
      <!-- create 함수에서 값을 받을 때 request.POST로 값을 받아서 처리 -->
      {% csrf_token %}
      <!-- csrf란? 
      input type="hidden"으로 만들어줌 
      POST 요청은 DB에 전송하기 위해 사용함
      혹시 요청이 들어왔을 때 다른 사이트에서 
      요청이 변조된 것이 아닌지 확인하는 로직 -->
      <label for="title">제목 : </label>
      <input type="text" name="title" id="title">
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글쓰기">
    </form>
    ```

  * GET과 _POST_의 차이점

    * URL 평점 **기록**_(등록)_
      * POST
        * 무언가를 **저장**하고 기록하는 기능
    * URL 평점 조회
      * GET
        * ex) Google 검색



* 서버측의 이중 검증
  * HTML에서 검증을 했더라도 서버측에서 이중 검증이 되어야 완전한 보안을 구현할 수 있습니다.



* ModelForm

  * 대체 기능

    ```django
    forms.py에서 
    
    from django import forms
    from .models import Article
    
    # 모델 form에 instance를 넘겨서 new.html의 form을 대체한다
    # template에 무언가를 넘기기 위해 context를 넘긴다 
    class ArticleForm(forms.ModelForm):
    
      class Meta:
        # Article model에 있는
        model = Article
        # 모든 필드를 내가 가져다가 사용하겠다
        fields = '__all__'
    
    
    new.html에서
    
    {{ article_form.as_p }}
    
    ```

    

  * 필드가 많을 경우 ModelForm에서 관리

  * 유효성 검사  

    * ex) Google에 로그인할 때
    * 유효성 검사가 실패했을 때 어떤 결과를 보여주기도 합니다.

    ```django
    def create(request):
      # 데이터의 개수가 많아지면 많아질수록 request.POST의 개수도 많아진다
      # article_form은 ArticleForm에 request.POST를 넘기고 
      # 만약에 article_form이 유효한지 검사할 수 있다
      # article_form = ArticleForm(request.POST)
    	if article_form.is_valid():
    	article.form.save()
    	# 유효하지 않을 경우 장고는 알림을 자동으로 해줌
    	else:
    		print('유효하지 않습니다')
        return redirect('articles:index')
    ```

    