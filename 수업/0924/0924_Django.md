## Django

* Project
  * 여러개의 앱이 모여있는 곳입니다.
* Application
  * 사용자의 요청이 들어오면 이 요청에 대한 응답을 보냅니다.
  * 기능 단위로 만들어가야 합니다.



* Views

  * 함수를 왜 정의하는가?

    * 사용자는 요청하고 서버는 응답합니다.

      * 즉, 함수는 HTTP로 요청을 받고 HTTP로 응답하기 위한 것입니다. Views는 Templates에게 응답을 작성하는 문서의 형식을 부탁합니다.

        ```django
        def index(request):
        	return render(request, 'index.html')
        ```

      * render()

        * 결국 응답은 어떠한 결합으로 이루어지는가?

          * 템플릿 + 컨텍스트 + 사용자에게 보여지는 텍스트

            ```django
            render(request, template_name, context)
            ```

            * request
              * 요청 객체
            * template_name
              * 경로
            * context
              * 데이터



* Templates
  * 사용자에게 보여줄 HTML 파일



* Django에서 코드는 어떤 순서로 구현하는가?

  * URL 

    * URL의 다음은 Views

      ```django
      path('index/', views.index)
      ```

  * View

    * Views의 다음은 Template

      ```django
      def index(request):
      return render(request, 'index.html')
      ```

  * Templates

    * 사용자에게 보여줄 HTML 파일

      ```django
      articles/templates/index.html
      ```

      

* 추가 설정
  * LANGUAGE_CODE
    * 전세계의 개발자가 사용하는 장고는 영어를 기본으로 제공하지만 국가별 언어를 제공합니다
  * TIME_ZONE
    * 전세계의 개발자는 서로 다른 시간대의 공간에서 개발합니다. USE_TZ를 True로 설정하면 자동으로 국가별 시간에 맞추어 변경 가능합니다.