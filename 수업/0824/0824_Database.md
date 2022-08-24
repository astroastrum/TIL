## Python

* **객체란?**

  * 객체는 **파이썬의 모든것**이며 **속성과 메소드**를 가지고 있습니다.

* 클래스란?

  * 학교에는 교실, 과학실, 음악실, 체육관 등 독립된 공간이 존재합니다. 이러한 공간과 같이 프로그래머가 조작할 수 있는 독립된 공간이 있습니다. 이렇게 틀을 만들어 놓은 것을 Class라고 합니다.

  * Class의 구조

    * ```python
      class 클래스 이름:
          클래스 멤버 정의
          클래스 메소드 정의
          
          
      # Class 구조 예시
      class Music:
          var = '도레미파솔라시도'
          def playMusic(self):
              print(self.var)
      ```

  * **Class를 인스턴스 객체로 만들기**

    * '도레미파솔라시도' 음계를 악보에 그린다고 해서 음계가 실행이 되는 것은 아닙니다. 음계를 실행하려면 피아노의 건반이 만들어져 있어야 합니다. 이와 같이, Class도 실제로 실행을 하려면 인스턴스 객체로 만들어야 실행이 가능합니다.

    * 인스턴스 객체로 만들기 위해서는 먼저 인스턴스 객체를 만들어야 합니다. 그 다음에는 멤버와 메소드를 호출해야 완성이 됩니다.

      ```python
      class Music:
          var = '도레미파솔라시도'
          def playMusic(self):
              print(self.var)
      
      obj = Music()		# 인스턴스 객체를 먼저 만듭니다
      print(obj.var)
      obj.playMusic()
      ```

      

  * 클래스 메소드

    * Class 내부에 어떠한 함수가 있나요? def로 이미 만들어진 함수를 클래스 메소드라고 합니다.

      ```python
      class Music:
          var = '도레미파솔라시도'
          def playMusic(self):
              print(self.var)
      
      obj = Music()		
      print(obj.var)
      obj.playMusic()
      ```

      



## Object Relational Mapping (ORM)

* 데이터베이스를 객체로 관리하는 것입니다.

* SQL문은 이렇게 작성을 했었습니다.

  ```python
  CREATE TABLE Users(
  	id Primary Key,
  	FirstName
      Lastname  
  );
  ```

* 이와 같은 동일한 문법을 파이썬에서는 Class를 사용해서 생성한 것을 db에 담습니다.

  ```python
  Class Users(blogers.posting)
  	title = blogers.space
  ```

  