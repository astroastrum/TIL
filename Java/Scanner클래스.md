## Scanner클래스

* 먼저 한 문장을 입력합니다.

  ```java
  import java.util.*;
  ```

* Scanner클래스의 객체를 생성합니다.

  ```java
  Scanner scanner = new Scanner(System.in);
  ```

* nextLine() 메서드를 불러옵니다. 내용을 입력하면 문자열로 반환되는데 Integer.parseInt() 메서드를 호출하여 int타입으로 바꿉니다.

  ```java
  String input = scanner.nextLine();
  int num = Integer.parseInt(input);
  ```

  