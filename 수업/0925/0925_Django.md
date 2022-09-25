## Django

* 추가 설정
  * USE_L10N
    * locale의 형식을 통해 날짜와 숫자를 설정합니다.
  * USE_I18N
    * 번역을 사용하고 싶을 경우 설정합니다.
    * I18N
      * 국제화하기 위한 함수



* Django Template
  * Django Template Language Syntax
    * Variable
    
      ```django
      {{ variable }}
      
      변수명은 영어, 밑줄, 숫자를 섞어서 사용할 수 있습니다. 하지만 밑줄을 첫번째 자리에 지정할 수 없습니다.
      ```
    
      
    
    * Filters
    
      ```django
      {{ variable|filter }}
      
      변수를 변경하거나 고칠 경우에 사용합니다.
      ```
    
      
    
    * Tags
    
      ```django
      {% tag %}
      ```
    
      
    
    * Comments
    
      ```django
      {# #}
      
      Django template에서 주석을 작성할 경우에 사용합니다.
      ```
    
      