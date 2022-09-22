## Django

* Django

  * Request and Response

    * Django의 구조는 요청과 응답입니다.

      

* Three Django Steps
  1. 주문서를 만듭니다.
     * URL
       * index page의 실제 경로 page를 요청합니다.
       * 첫번째 인자와 두번째 인자(어떤 view 파일에서 주문을 핸들링 할 것인가)를 지정합니다.
  2. 로직을 구현합니다.
     * View
       * 함수 정의
         * 요청한 사람의 정보(하나의 객체가 되어)가 들어옵니다.
  3. 클라이언트에게 HTML 문서를 보여줍니다.
     * Templates
       * Django 규칙
         * articles 내에 폴더를 생성합니다.