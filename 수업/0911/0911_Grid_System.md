## Grid System

* 그리드 컨테이너 (Grid Container)

  * 부모 요소 

* 그리드 아이템 (Grid Item)

  * 자식 요소 

* Grid System 어떻게 시작하는가?

  ```css
  .container {
      display: grid;
  }
  ```





## Grid Breakpoints and Container Widths

* Grid Options

  ```html
  px-lg
  ```

  * Extra Small
    * Extra Small과 Extra Large는 웹의 breakpoint로 적합하지 않습니다.
  * Small

  * Medium

  * Large

  * Extra Large

* Bootstrap **공백** 조절하기
  * py 
    * Padding Y축 = Top, Bottom
  * px
    * Padding X축 = Left, Right



## Header

* 웹 페이지를 열면 바로 마주하는 부분(도입부) 입니다.
  * 그래서 로고, 제목 요소( h1~h6) 등을 사용합니다.





## Grid System Practice (Grid Options)

* Grid System은 다양한 화면크기(desktop, tablet, mobile)에 맞추어 요소들을 배치할 수 있습니다.

  * **단계적**으로 **Grid Options** 이해하기

    * 먼저 `.col-size-n`을 알면 Grid System을 자유롭게 조정할 수 있습니다.

      1. ```html
         .col-size-n이란?
         
         화면크기가 size 이상이면 n칸을 가집니다.
         size 이하면 column의 모든 칸(가로)이 화면을 가득(full) 채웁니다.
         ```

      2. ```html
         .col-4
         한 row(수평 방향으로)에 4칸씩 가집니다.
         ```

      3. ```html
         .col-sm-3
         화면크기가 small 이상이면 한 row의 3칸을 가지고
         이하면 전체화면의 가로를 가집니다.
         ```

      4. ```html
         col-md-3
         화면크기가 medium 이상이면 한 row의 3칸을 가집니다.
         ```

      5. ```html
         col-6 col-md-3
         화면크기가 medium 이상이면 한 row의 3칸을 가지고
         이하면 6칸을 가집니다.
         ```

         

  