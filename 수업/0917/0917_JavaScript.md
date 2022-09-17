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

        