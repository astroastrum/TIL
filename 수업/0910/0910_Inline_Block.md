## Inline and Block

* Inline

  * 인라인은 `직렬의` 또는 `일렬로 늘어선`이라는 뜻입니다. 보통 마트에서 계산하려고 줄 서 있을 때 "Are you in line?" (줄 서고 계신 건가요?)라고 묻기도 합니다. 이와 같이 인라인의 중요한 특징은 **한 줄로 나란히 줄서기** 입니다.

    ```javascript
    display: Are you in line?
    inline element: Yes, I am in the line.
    ```

  * Inline Element

    * ```html
      <a>
      ```

    * ```html
      <span>
      ```

    * ```html
      <em>
      ```

  * Inline 특징

    * Width와 Height을 설정해도 적용되지 않습니다.
      * 적용되지 않는 이유는 태그가 정하는 공간만 인정하기 때문입니다.
    * Margin과 Padding 속성은 좌우 간격만 허용합니다.



* Block

  * Block Element

    * ```html
      <div></div>
      ```

    * ```html
      <h1></h1>
      ```

    * ```html
      <p></p>
      ```

  * Block 특징
    * Width, Height, Padding, Margin 모두 허용



* display: inline-block

  * 한줄에 나란히 줄서는 것을 허용하고 width, height, padding, margin 모두 정할 수 있습니다. block과 inline의 법을 반영한 것입니다.

  * Inline-block Element

    * ```html
      <select>
      ```

    * ```html
      <input>
      ```

    * ```html
      <button>
      ```

      