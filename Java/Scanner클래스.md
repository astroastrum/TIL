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

  

* 알고리즘

  ```java
  import java.util.Scanner; // java.util 패키지에 있는 Scanner 클래스를 import함
  public class Main { // Main.java 파일명과 클래스 이름이 같아야만 하는 JAVA의 규칙
      public static void main(String[] args) {
          Scanner sc = new Scanner(System.in); 
          // Scanner클래스는 객체를 생성해야만 사용가능
          // System.in은 화면에서 입력을 받는다는 뜻
          int N = sc.nextInt();
          // 입력받은 정수를 변수 N에 저장
          
          String sNum = sc.next(); // 입력값을 sNum에 저장
          char[] cNum = sNum.toCharArray(); // char[]형 변수로 변환
          int sum = 0;
          for (int i = 0;, i < cNum.length; i++) {
              sum += cNum[i] - '0';
          }
          System.out.print(sum);
      }
  }
  ```

  