## Django 

* App URL mapping

  * 앱의 개수가 증가하면 어떠한 현상이 발생하는가?

    * view 함수와 path()의 개수도 동시에 증가합니다.

    * 개수가 증가하면 모든 것을 urls.py에서 감당할 수 없습니다.

    * 그래서 urls.py를 앱마다 매칭시켜야 합니다.

      

* Template namespace

  * 장고는 Templates을 분리된 공간이 아닌 하나의 공간이라고 인식합니다. 그래서 같은 파일명이 존재하면 같은 파일로 인식합니다. 파일명이 같을 경우, 장고는 첫번째로 등록된 파일만 인지합니다. 동일한 이름을 가진 파일을 구분하려면 이름 공간을 별도로 만들어 주어야 합니다. 예를 들면, articles의 templates에 articles 폴더를 하나 만들고 이 폴더 안에 index.html 파일을 이동합니다.

    ```django
    articles/
    	templates/
    		articles/
    			index.html
    ```

    

* Django ORM(Object-Relational Mapping)

  * 객체와 관계형 데이터베이스의 데이터를 대응시킵니다. 데이터베이스의 테이블을 객체(Class)와 같이 쓸 수 있습니다. ORM은 장고가 데이터베이스와 연결할 수 있는 통로입니다.

    

* 쿼리셋(QuerySets)
  * 쿼리셋은 데이터베이스에 있는 객체 집합을 뜻하고 데이터베이스의 데이터를 다룰 수 있습니다.

