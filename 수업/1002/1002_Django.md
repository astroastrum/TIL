## Django Gitignore

* Gitignore

  ```django
  source venv/Scripts/activate
  
  django-admin startproject [프로젝트 이름]
  
  git init
  
  
  .gitignore 파일을 생성
  gitignore 파일안에 [가상환경 폴더 이름]/
  예) vevn/
  
  
  pip freeze > requirements.txt
  
  git add .
  
  git commit -m ''
  
  git remote add origin [깃허브주소]
  
  git push -u origin master
  ```

* 기존 remote 삭제 명령어

  ```django
  git remote -v
  
  git remote rm origin
  
  git remote add origin [깃허브 주소]
  ```

  