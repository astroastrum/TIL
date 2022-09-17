## JavaScript

* 반복문(Loop Statement)

  * 조건식(conditional expression)이 참이면 계속 실행합니다.

  * 종류

    * while
    * for
    * for...in
    * for...of

  * 특징

    * while

      * 언제 종료?

        * 거짓을 만나면

          ```javascript
          while (조건식) {
             // 거짓을 만나면 종료
          }
          ```

          

    * for

      * 언제까지 실행?

        * 거짓을 만날때까지

          ```javascript
          for (초기화식; 조건식; 증감식) {
              //거짓을 만날때까지 반복
          }
          ```

          

    * for...in

      * 실행 구조

        ```javascript
        const browsers = {
            Google: 'Chrome'
            Apple: 'Safari'
            Microsoft: 'Microsoft Edge'
        }
        
        for (let property in browsers) {
            console.log(property); // Google, Apple, Microsoft 
        }
        ```

        

    * for...of

      * 실행 구조

        ```javascript
        const browsers = ['Chrome', 'Safari', 'Microsoft Edge']
        
        for (let browser of browsers) {
            console.log(browser); // Chrome, Safari, Microsoft Edge
        }
        ```

        

* 함수

  * 일급 객체 입니다.

  * 함수 정의 방법

    * 함수 선언식 (function declaration)
    * 함수 표현식(function expression)

  * 함수 구조

    * 이름

    * 매개변수(arguments)

    * body

      ```javascript
      function name(args) {
          // Brendan's code to execute
      }
      ```

  * 함수 표현식(function expression)

    * 함수를 변수에 저장하는 동작이고 (args)의 앞에 있었던 name을 표현식의 name에 자리를 옮긴 느낌입니다.

      ```javascript
      
      const name = function (args) {
          // Brendan's code to execute
      }
      ```

  * 매개변수와 인자의 개수

    * JavaScript에서는 자유롭게 값을 넘길 수 있습니다.

      ```javascript
      const liberty = function () {
          return 0
      }
      
      freedom(7, 8, 9) // 0
      
      const doublelbt = function (lbt1, lbt2) {
          return [lbt1, lbt2]
      }
      
      doublelbt(7, 8, 9) // [7, 8]
      ```

      

  