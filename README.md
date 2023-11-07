# Mobile game blog
- 다양한 모바일 게임의 개인적인 감상과 평가를 작성하며, 서로 정보를 공유하는 블로그입니다.

# 1. 프로젝트 소개
  
### 개발 기간
2023.10.26 ~ 2023.11.07

## WBS
<div align="center">
  <img src="./mysite/리드미 자료/WBS.png" width="60%">
</div>

### 기능 소개
- 글 작성, 삭제, 수정, 조회, 댓글 등 블로그 형식을 기반으로 제작된 커뮤니티 서비스
- 회원가입 한 사용자는 게시물과 댓글 작성 가능
- 게임 분류 별 카테고리와 검색 기능을 사용하여 정보를 보다 쉽게 얻을 수 있습니다.


# 2. 개발 기술 및 환경
### 2-1 개발 기술
#### [기술 - BE]
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">  
<br>
#### [기술 - FE]
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

### 2-2 개발 환경
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

# 3. 구조 설계
<div align="center">
  <img src="./mysite/리드미 자료/기획 마인드맵.png" width="60%">
</div>



# 4. 데이터베이스 모델링(dbdiagram.io)
<div align="center">
  <img src="./mysite/리드미 자료/DB.png" width="60%">
</div>



# 5. 프로젝트 구조
### 5-1. Directory 구조
___
```
📦 
├─ README.md
└─ mysite
   ├─ accounts
   │  ├─ __init__.py
   │  ├─ __pycache__
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ forms.py
   │  ├─ migrations
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   │
   ├─ blog
   │  ├─ __init__.py
   │  ├─ __pycache__
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ forms.py
   │  ├─ migrations
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   │
   ├─ db.sqlite3
   │
   ├─ main
   │  ├─ __init__.py
   │  ├─ __pycache__
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   │
   ├─ manage.py
   │
   ├─ media
   │  └─ blog
   │     ├─ files
   │     └─ images
   │
   ├─ projectblog
   │  ├─ __init__.py
   │  ├─ __pycache__
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   │
   └─ templates
      ├─ 404.html
      ├─ 500.html
      ├─ accounts
      │  ├─ change_password.html
      │  ├─ login.html
      │  ├─ profile.html
      │  ├─ signup.html
      │  └─ update.html
      ├─ base.html
      ├─ blog
      │  ├─ comment_form.html
      │  ├─ post_detail.html
      │  ├─ post_form.html
      │  └─ post_list.html
      └─ main
         ├─ about.html
         ├─ contact.html
         └─ index.html
```
### 5-2. URL 구조
<div align="center">
  <img src="./mysite/리드미 자료/AccountsURL.png" width="60%">
  <img src="./mysite/리드미 자료/BlogURL.png" width="60%">
</div>

# 6. 구현
## 6-1. 인증 및 사용자(Accounts)
#### 회원가입 및 로그인
<div align="center">
  <img src="./mysite/리드미 자료/회원가입, 로그인.gif" width="80%">
</div>
<p></p>
<div align="center">
  <img src="./mysite/리드미 자료/비회원 상단 바.png" width="100%">
</div>
<div align="center">
  <img src="./mysite/리드미 자료/회원 상단 바.png" width="100%">
</div>
<p></p>

- 로그인 전과 후의 상단 바 변화입니다.
- 회원 가입 시 완료되었다는 메시지와 함께 로그인 페이지로 이동합니다.
- 미인증 회원이 프로필과 글 작성에 비정상 접근 시 로그인 페이지로 이동합니다.
#### 프로필 페이지와 회원 정보 수정
<div align="center">
  <img src="./mysite/리드미 자료/프로필, 회원정보 수정.gif" width="80%">
</div>

#### 비밀번호 변경
<div align="center">
  <img src="./mysite/리드미 자료/비밀번호 변경.gif" width="80%">
</div>

- 옳지 않은 작성 시 알림 메세지로 확인할 수 있으며, 페이지가 이동하지 않습니다.
- 정상적으로 입력 후 변경되었다는 메세지와 함께 프로필 페이지로 이동합니다.

#### 회원탈퇴
<div align="center">
  <img src="./mysite/리드미 자료/회원탈퇴.gif" width="80%">
</div>

- 탈퇴 시 로그아웃 상태가 되며, 메인 페이지로 이동합니다.
- 클릭 실수를 방지하기 위해 경고 메세지가 나옵니다.
  
## 6-2. 블로그(Blog)
#### 게시물 작성
<div align="center">
  <img src="./mysite/리드미 자료/게시물 작성하기.gif" width="80%">
</div>
