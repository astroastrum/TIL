#### Git 기초 명령어 

- **git init**: 로컬 저장소를 만든다
- **git add**: 파일이나 폴더의 변경사항을 더한다
- **git commit -m '<커밋메시지>'**: 버전(커밋)을 기록한다
- **git status**: 파일의 상태를 알 수 있다
- **git log**: 파일의 버전을  볼 수 있다



#### :computer: Git 설정 파일

- 커밋을 하기 위해서 `사용자 정보 (commit author)`는 기본으로 설정해 놓아야 한다.

  - ```
    $ git config --global user.name "id"
     #깃아 만들어줘 --글로벌 사용자명 "id"
    $ git config --global user.email "email"
     #깃아 만들어줘 --글로벌 사용자 이메일 "email"
    ```



#### 원격 저장소 (Remote Repository)

* Push : 개인 전용 저장소의 버전을 Github으로 보내는 것: $ git push <원격저장소이름><브랜치이름>
  * ex) 지역에 사는 사람은 맥북 관리가 제대로 되지 않아서 수도권에 있는 애플 서비스센터로 보낸다.

* Pull : Github의 버전을 개인 전용 저장소로 가져오는 것: $git pull <원격저장소이름><브랜치이름>
  * ex) 관리를 받은 맥북을 다시 돌려 받는다.



