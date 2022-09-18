## JavaScript

* 함수

  * Rest Parameter

    * 나머지 매개변수는 세개의 점을 ... 매개변수 이름보다 먼저 작성하는 형태입니다. 

      ```javascript
      const dots = function (param1, param2, ...rest) {
          return [param1, param2, rest]
      }
      
      rest(7, 8, 9, 10, 11) // [7, 8, [9, 10, 11]]
      ```

      

  * Spread Operator

    * `Spread`는 일상생활에서 보통 '나는 빵에 잼 발라 먹을 거야'라고 표현하기도 합니다.

      ```javascript
      I'm going to spread jam on bread
      ```

    * `JavaScript`에서도 비슷한 뉘앙스를 가지는데 세개의 점을 사용해서 배열 인자를 폅니다.

      ```javascript
      const unfold = function (param1, param2, param3) {
          return param1 + param2 + param3
      }
      
      const numbers = [7, 8, 9]
      unfold(...numbers) // 24
      ```

       