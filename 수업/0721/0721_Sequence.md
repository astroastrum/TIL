### 컨테이너(Container)

* 컨테이너에는 여러 개를 담을 수 있습니다. 

  ```python
  salad = 'carrot'
  salad1 = 'lettuce'
  salad2 = 'turkey'
  salad3 = 'tomato'
  salad4 = 'blueberry'
  salad5 = 'cheese'
  
  다양한 샐러드 재료들을 담았습니다.
  그런데 신선한 샐러드 재료들을 하나로 정리하기 위해서 리스트가 만들어졌습니다.
  
  ingredients = ['carrot', 'lettuce', 'turkey', 'tomato', 'blueberry',   'cheese'] 
  
  신선한 재료를 한 바구니에 담았습니다.
  이것을 리스트라고 합니다.
  
  당근에게 접근하고 싶을 때는 index(순서)를 사용합니다. 
  print(ingredients[0])
  하면 당근이 출력됩니다.
  
  그렇다면 샐러드 요리 순서와 같이 바구니에 담을 수는 없을까요?
  ingredients = {
      '1st': ['carrot', 'lettuce']
      '2nd': ['turkey', 'tomato']
      '3rd': ['blueberry',   'cheese']
  			}
  
  샐러드 재료와 요리 순서를 같이 담을 수 있습니다.
  이것을 딕셔너리라고 합니다.
  딕셔너리는 샐러드 재료와 요리 순서 같이 키와 값의 쌍입니다.
  그래서 키(요리 순서)로 접근할 수 있습니다.
  ```

  