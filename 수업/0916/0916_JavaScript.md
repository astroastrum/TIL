## JavaScript

* Legacy Code

  * 개선이 어렵고 지속할 수 없는 오래된 코드

    

* ECMA Script

  * 코딩 스타일은 원칙과 일관성이 중요한데 원칙은 유연하게 대처해야하며 일관성을 유지하며 참고하는 것이 좋습니다. 

    

* 변수와 식별자

  * 식별자

    * 변수명
    * 달러($), 문자 그리고 밑줄(_)만이 첫글자로 사용됩니다.
    * 소문자를 첫글자로 작성해야하고 클래스명은 대문자 사용 가능합니다.

  * 변수

    * 변경 될 수 있고 이름이 주어진 값

  * 변수 JavaScript에서 사용하기

    1. 선언(Declaration)

       ```html
       let netscape
       console.log(netscape)
       ```

    2. 할당(Assignment)

       ```html
       netscape = 2
       console.log(netscape)
       ```

    3. 선언과 할당(초기화 Initialization)

       ```html
       let bar = 9
       console.log(bar)
       ```



* 변수 선언 방법
  * 키워드 사용
    * 키워드는 원하는 동작을 정한 것입니다.
    * JavaScript는 키워드를 사용해서 변수를 선언합니다.
      * 키워드 종류
        * var
        * let
        * const
  * undefined
    * 변수는 초기 값을 주지 않으면 태생적으로 `undefined` 값을 가지게 됩니다. 
    * 변수의 값이 없는 것을 설명해주는 데이터 타입입니다.



* let, const

  * let은 재할당이 가능합니다.

    ```html
    let netscape = 2
    netscape = 2 // 재할당
    
    console.log(number)
    ```

  * let은 재선언 되지 않습니다.

    ```html
    let netscape = 2
    let netscape = 9
    ```

  * const는 재할당이 되지 않습니다.

    * 재선언도 가능하지 않습니다.

  * 블록 스코프* (block scope)

    * 함수, for, if 등의 중괄호 안의 영역을 의미합니다.

    * 중괄호 안의 영역에 자리잡고 있는 변수는 영역을 벗어난 범위에 영향을 받지 않습니다.

      ```html
      let netscape = 2
      
      if (netscape === 2) {
        let netscape = 9
        console.log(netscape)
      }
      
      console.log(netscape)
      ```

      

* var

  * 재할당과 재선언 기능이 있습니다.

  * 호이스팅*이 특징이며 비정상적으로 작동할 수 있습니다.

    * 호이스팅이란?
      * 일반적으로 변수가 선언이 되어야 변수에 다가갈 수 있습니다. 그런데 JavaScript에서는 변수가 선언되기 전에도 변수에 접근을 할 수 있는데 다가가면 undefined값을 줍니다. 이렇게 선언되지 않은 변수에 다가갈 수 있는 현상을 `호이스팅`이라고 합니다.

  * 함수 스코프* (function scope)

    * 함수 스코프를 벗어난 범위의 영향을 받지 않습니다.

      ```html
      function netscape() {
        var mocha = 2
        console.log(mocha)
      }
      
      console.log(mocha) // 함수 스코프를 벗어난 범위에 있기 때문에 모카는 정의되지 않았습니다
      ```

      

* 데이터 타입(Data Type)

  * JavaScript에서는 모든 값에 데이터 타입이 주어집니다.
  * 데이터 타입 종류
    * 원시 타입(Primitive Type)
      * 재할당 했을 경우 원래 본인 타입의 값을 출력
    * 참조 타입(Reference Type)
      * 재할당 했을 경우 재할당한 값을 출력



* 연산자

  * 할당 연산자

    * Increment & Decrement

      ```html
      let netscape = 2
      
      netscape += 7
      console.log(netscape) // 9
      
      netscape++
      console.log(netscape) // 10
      
      netscape--
      console.log(netscape) // 9
      ```

      

  * 비교 연산자

    * 결과값을 True와 False로 줍니다.

      ```html
      const mocha = 2
      const live = 9
      console.log(mocha < live) // true
      ```

      

  * 논리 연산자

    * and

    * or

    * not

      ```html
      // and 
      
      console.log(true && true) // true
      
      // or
      
      console.log(true or true) // true
      
      // not
      
      console.log(!'Hello') //false
      ```

      

  * 삼항 연산자

    * 세 개의 피연산자를 통해 값을 출력합니다.



* 조건문

  * 특징

    * 'if' statement

      ```html
      const owner = 'Brendan'
      
      if (owner === 'BrendanEich') {
        console.log('JavaScript')
      } else if (owner === 'JamesGosling') {
        console.log('Java')
      } else {
        console.log('WhosNext')
      }
      ```

      

    * 'switch' statement

      ```html
      swith(express_here) {
        case 'case result': {
          // execute 
          [break]
        }
      }
      ```

      

  * 종류

    * if, else if, else

    * 소괄호 내부에는 조건을 넣고 중괄호 내부에는 실행할 코드를 넣습니다.

      ```html
      if (조건삽입) {
        // Brendan's code to execute 
      }
      
      else if (조건삽입) {
        // Brendan's code to execute
      }
      
      else {
        // Brendan's code to execute
      }
      ```

      

