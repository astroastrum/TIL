## QuerySet API

* QuerySet란?

  * 맥도날드 버거 세트를 고르고 싶을 때 세트 메뉴를 보고 주문합니다. QuerySet는 세트 메뉴와 같은 목록입니다. 장고(Django) ORM에서 형성된 자료형이기 때문에 파이썬에서 사용하려면 형변환을 해야합니다.   

* API는 기능입니다. 

* gt

  ```python
  # gt는 greater than 입니다.
  
  Entry.objects.filter(id__gt=8)
  
  # 이 문법에 대응되는 sql은?
  # SELECT ... WHERE id > 8;
  ```

  



## Object Relational Mapping (ORM)

* 파이썬으로 데이터베이스를 조작할 수 있습니다.