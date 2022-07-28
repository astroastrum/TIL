## 입력

### Input()

* dailycoding이라는 단어를 받으려면 iput() 함수를 사용해야 합니다. input() 함수가 실행되면 우리가 제어권을 갖게 되고 이 상태에서 dailycoding을 받고 입력된 dailycoding이 word에 저장됩니다.

  ```python
  word = input()
  >>> dailycoding
  
  word = "dailycoding"
  ```



### Map함수

* Map함수를 사용하면 자유자재로 입력을 받을 수 있습니다.

  ```python
  j = input()
  # j라는 변수에 문자열을 입력 받을 수 있습니다
  
  a = int(input())
  s = float(input())
  # integer(int)를 붙이면 문자열에서 type casting(형 변환)을 하게 됩니다.
  # 많은 숫자가 아닌 딱 하나의 숫자만 입력 받을 수 있습니다
  # 많은 숫자는 어떻게 받을 수 있을까요?
  
  j, a = map(int, input().split())
  # input을 문자열로 받습니다. split()을 하게되면 각각의 글자별로 분리됩니다. 그리고 각각 정수형으로 바꿔서 저장을 하는 것 입니다.
  s, h, k = map(float, input().split())
  # 이렇게 많은 숫자를 입력 받을 수 있습니다
  
  ```

  

* Map함수는 Python의 내장 함수입니다.

  * Map함수의 구조는 

    * map(function, iterable) 

    * map(함수이름, 순회가능한 집합형 데이터 구조)

      ```python
      map(int, ["7", "8", "9"])  # "7", "8", "9"에 int 적용
      >>> 정수 7, 8, 9 
      ```

      

## 출력

### print

* 콤마(,)를 사용해서 (j, a)를 담으면 공백으로 출력됩니다.

  ```python
  j = "july"
  a = "awesome"
  
  print(j, a)
  >>> july awesome
  ```

  

### 선택인자 end

* end가 움직이면 개행(줄바꿈)을 하지 않고 end에 붙어있는 어떤것이 오작교가 되어 print()의 출력을 이어줍니다.

  ```python
  j = "july"
  a = "awesome"
  
  print(a, end="@")
  print(b)
  >>> july@awesome
  ```

  



### 선택인자 sep

* sep(seperator)은 개행의 효과를 가지고 있습니다.

  ```python
  print(m, a, sep="\n")
  >>> july
  >>> awesome
  ```

  

