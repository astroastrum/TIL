## String 클래스

* 문자열 처리 담당

* 객체지향개념 이후, 데이터와 기능(함수)을 함께 클래스에 묶어서 사용

* 내용 변경할 수 없음 (Immutable class)

  ```java
  String str = "Class";
  ```


* 자바는 문자열을 위한 `클래스`를 별도로 공급
  * 클래스
    * `String클래스`
      * 문자열 저장
      * 메서드 공급 

* 문자열(String)은 문자가 나란히 정렬되어 있다는 의미이며 char타입의 변수에는 오직 하나의 문자만 넣을 수 있습니다.

  ```java
  char name = 'J'
  String id = "Java"
  ```

* 덧셈 연산자를 사용하여 문자열을 결합할 때 피연산자의 타입과 상관없이 문자열로 출력합니다.

  ```java
  String add = "Java" + 7 // add는 "Java7"
  ```

* StringBuffer클래스
  * 문자열을 많이 사용해야 할 경우 활용