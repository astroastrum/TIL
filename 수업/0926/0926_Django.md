## Django

* Template inheritance

  * HTML 파일의 개수가 많을 경우 부트스트랩의 CDN을 가져올 때 어떻게 해야 시간을 단축할 수 있을까요? 템플릿 상속으로 시간을 단축할 수 있습니다. 템플릿 상속은 템플릿의 가장 윗부분에 위치해 있어야 합니다.

    ```django
    {% extends '' %}
    
    {% block content %}
    {% endblock content %}
    ```

    

* URLs
  * Trailing slash
    * 사용자는 URL을 통해 요청합니다.
    * Django는 /(Trailing slash)를 URL의 마지막에 항상 붙여줍니다.



* Sending form data

  * action

    * 응답(데이터)을 어떤 URL로 할 것인가에 대한 속성입니다.

      ```django
      <form action="">
      </form>
      ```

  * method

    * 데이터를 어떠한 방법으로 전송할 것인가에 대한 속성입니다.

      ```django
      <form action="" method="">
      </form>
      ```

      

    

  