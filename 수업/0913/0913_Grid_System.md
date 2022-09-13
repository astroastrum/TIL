## Pair Project

* flex-grow

  * grow는 `증대하다` 또는 `성장하다`라는 의미입니다. flex-grow는 크기를 비율로 증가시켜서 박스 안의 여백을 채우는 기능을 합니다. 

    ```css
    .growmore {
    flex-grow: 2;
    flex-grow: 2;
    }
    ```

* float
  * float은 `뜨다`라는 뜻입니다. 부력과 밀도 덕분에 배는 바다 위를 자유롭게 다니며 무역을 합니다. 배가 물 위에 뜨는 것이 전세계 무역을 가능하게 하는 것 처럼 float은 주변의 요소와 적당한 어울림을 가능하게 합니다.
* position
  * 상대 위치(relative position)
    * Self 기준
  * 절대 위치(absolute position)
    * 배치 기준은 상위 요소
  * 고정 위치(fixed position)
    * Viewport 기준
  * 정적 위치(static position)
    * 브라우저에 따라서 배치

* img-fluid

  * 반응형 이미지
    * 부모 요소에 맞추어 자동으로 이미지 크기를 조절해 줍니다.

* container

  * 웹 페이지의 컨테이너에 맞추어 크기를 지정합니다.
  * ex) 카드를 배치할 때 div.container로 감싸줍니다.

* container-fluid

  * 좌우 여백을 지정하지 않습니다.

* Row columns

  * 개수를 균등하게 배치

    ```html
    한 줄에 나란히 2개 배치
    <div class="row row-cols-2">
    </div>
    
    col-sm-6과 같은 칸수 변화는 개별적으로 지정할 수 있음
    ```

* Badge 

  * background colors(Bootstrap)
    * 상하좌우 배치는 position 사용

  