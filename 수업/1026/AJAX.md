## AJAX

* 비동기식 Asynchronous

  * 요청 보내고 응답 기다리지 않고 다음 코드가 실행됨

* 시작

  ```python
  python test.py
  
  pip install requests
  
  # console
  const request = new XMLHttpRequest()
  const URL = 'https:/jsonplaceholder.typicode.com/todos/1'
  request.open('GET', URL)
  request.send()
  const todo = request.response
  consol.log(todo)
  
  todo
  
  
  # Javascript 특징
  Call Stack
  	먼저 쌓인 것이 먼저 나가지 않음
  Task Queue
  	들어온 순서대로 나감
  
      
      
  console.log('hi')
  # 몇초가 지나면 ~ 동작
  setTimeout(function() {
      console.log('작업중')
  })
  console.log('bye')
  
  
  
  원래 실행 순서
  1. console.log('hi')
  2. setTimeout (setTimeout이 Web Apis에 던져져 있음)
  3. console.log 실행
  
  
  
  test.py에서
  파이썬에서는 요청이 도착할때까지 (10초)기다렸다가 response에 저장하고 그 다음을 실행
  
  import time
  
  print('hi')
  time.sleep(10)
  print('bye')
  
  
  
  
  실제 실행 순서 (EventLoop 형식으로 동작됨)
  1. console.log('hi')
  2. console.log 실행
  3. setTimeout (완료되면 Callback Queue로 넘겨짐, Call Stack 비어져있으면 Callback Queue에서 올려짐)
  
  
  JS는
  요청이 도착하는 것 안 기다림(그냥 Web API에 던져놓음)
  그리고 그냥 다음을 실행해버림
  그리고 도착하면 무엇인가를 함
  
  
  ```

  ![](AJAX.assets/loupe.png)

  

* Axios

  ```python
  # xhr보다 Axios가 훨씬 사용하기 편함
  <script>
  const URL = 'http://jsonplaceholder.typicode.com/todos/1'
  여기로 요청을 보내서 도착하면
  
  then 이라고 하는 곳에 있는 함수를 실행시켜줄게
  실패하면 catch에 있는 함수를 실행시켜줄게
  axios.get(URL)
  	.then(res => console.log(res.data.title))
      .catch(err => console.log('Error!'))
      
  </script>
  
  
  Javascript 코드를 사용하기 위해서는 먼저
  Axios Doc에가서 CDN을 가져온다.
  Axios Docs 링크에서 https://axios-http.com/kr/docs/intro
  
  jsDelivr CDN 사용하기:
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      
  또는
  unpkg CDN 사용하기:
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
      
      
  
      
  # axios 01
  
  axios.html에
  <!DOCTYPE html>
  <html lang="ko">
  
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>실습</title>
    {% bootstrap_css %}
    {% block css %}{% endblock css %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
  </head>
  
  <body>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
  	# body 태그를 선택하고
  	const body = document.querySelector('body')
      const title = document.createElement('h1')
      title.innerText = 'AJAX'
      body.appendChild(title)
      
      const URL = 'http://jsonplaceholder.typicode.com/todos/1'
      axios.get(URL)
        # 응답이 오면 응답을 넘겨 받아서 
        .then(response => console.log(response))
        # 에러가 들어올 것이다
        .catch(err => console.log('${err}!!!'))
      console.log('안녕 장고! 콘솔창에 JSON 값을 출력했구나')
    </script>
  </body>
  
  </html>
  
  
  
  
  
  # axios 02
  
  const body = document.querySelector('body')
      const title = document.createElement('h1')
      title.innerText = 'AJAX'
      body.appendChild(title)
  
   
      const URL = 'http://jsonplaceholder.typicode.com/todos/1'
      axios.get(URL) 
        .then(response => {
          const p = document.createElement('p')
          p.innerText = response.data.title
          body.appendChild(p)
        })
        .catch(err => console.log('${err}!!!'))
      console.log('안녕 장고! 콘솔창에 JSON 값을 출력했구나')
      
      
      
      
  # axios 3
  
  <button>클릭할때마다 delectur aut autem 추가됨</button>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      const body = document.querySelector('body')
      const title = document.createElement('h1')
      title.innerText = 'AJAX'
      body.appendChild(title)
  
      const button = document.querySelector('button')
      button.addEventListener('click', function() {
        const URL = 'http://jsonplaceholder.typicode.com/todos/1'
        axios.get(URL) 
          .then(response => {
            const h2 = document.createElement('h2')
            h2.innerText = response.data.title
            body.appendChild(h2)
            const p = document.createElement('p')
            p.innerText = response.data.userId
            body.appendChild(p)
          })
          .catch(err => console.log('${err}!!!'))   
      })
      
      
  
  비동기는 버튼을 하나 눌렀더니 비동기 요청이 간다. 응답한 결과 자체가 html이 아니라 JSON을 주고 응답을 JSON으로 가지고 와서 원래 있었던 곳에서 DOM 조작으로 바꾸어 버린다. 사용자는 같은 화면을 보고 있지만 화면이 변하고 내가 무언가를 한 결과를 받아 볼 수 있다. 화면이 있는데 특정 부분만 키워나가고 클라이언트 측에서 조작해서 서버는 편리하다. 대표적인 예는 구글 map이다.
  
  ```

  

