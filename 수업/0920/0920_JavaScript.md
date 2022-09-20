## JavaScript

* 배열(Arrays)

  * 특징

    * 배열을 조작하고 싶을 때 사용합니다.

    * 키와 속성을 가진 객체입니다.

    * 0과 index를 사용해 어떤 값에 다가갈 수 있습니다.

    * array.length는 배열의 길이를 알 수 있는 어떤 것입니다.

      ```javascript
      const numbers = [3, 5, 7, 8, 9, 10]
      
      console.log(numbers[1]) // 5
      console.log(numbers.length) // 6
      ```

      

  * 배열의 중요한 메서드 종류

    * array.reverse()

      * 순서를 뒤집어서 나열합니다.

        ```javascript
        const numbers = [3, 5, 7, 8, 9, 10]
        numbers.reverse()
        console.log(numbers) // [10, 9, 8, 7, 5, 3]
        ```

      

    * filter

      * 원하는 요소들을 구분하여 덩어리로 출력해 줍니다. (필터링) 즉, 콜백 함수의 반환 값이 True일 경우에만 필터링을 해줍니다.

        ```javascript
        const numbers = [2, 5, 6, 7, 8, 9, 10]
        
        const evenNums = numbers.filter((num, index) => {
            return num % 2
        })
        
        console.log(evenNumbs) // 2, 6, 8, 10
        ```

        