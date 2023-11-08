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



# 4. DB 모델링(dbdiagram.io)
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

#### 회원 탈퇴
<div align="center">
  <img src="./mysite/리드미 자료/회원탈퇴.gif" width="80%">
</div>

- 탈퇴 시 로그아웃 상태가 되며, 메인 페이지로 이동합니다.
- 탈퇴한 유저가 작성한 게시물과 댓글 또한 모두 삭제됩니다.
- 경고 메세지를 통해 의사를 재확인하며, 실수를 방지합니다.
  
## 6-2. 블로그(Blog)
#### 게시물 작성
<div align="center">
  <img src="./mysite/리드미 자료/게시물 작성하기.gif" width="80%">
</div>

- 제목(Title), 내용(Content), 대표 이미지(Head image), 파일 업로드(File upload), 카테고리(Category)를 형식으로 가지고 있습니다.
- 대표 이미지(Head image) 업로드 시 메인 페이지에서 글의 썸네일 이미지로 나타납니다.
- 제목과 내용은 필수로 입력해야 합니다.
- 게시물은 조회수를 기록하며, 업로드 시간과 작성자가 저장됩니다.
#### 게시물 수정, 삭제
<div align="center">
  <img src="./mysite/리드미 자료/게시글 수정, 삭제.gif" width="80%">
</div>

- 본인이 작성한 게시물은 수정과 삭제를 할 수 있습니다.
#### 댓글
<div align="center">
  <img src="./mysite/리드미 자료/댓글 작성과 수정, 삭제.gif" width="80%">
</div>

- 로그인한 사용자는 게시글에 댓글을 작성할 수 있습니다.
- 또한, 본인이 작성한 댓글이라면 수정과 삭제 할 수 있습니다.
<div align="center">
  <img src="./mysite/리드미 자료/다른 계정에서의 댓글, 포스트 수정 불가..gif" width="50%">
</div>

- 본인의 게시물과 댓글에만 수정과 삭제 버튼이 나타납니다.
#### 카테고리
<div align="center">
  <img src="./mysite/리드미 자료/카테고리.gif" width="80%">
</div>

- 게시물 작성 시 등록했던 카테고리를 이용해 분류를 할 수 있습니다.
#### 검색
<div align="center">
  <img src="./mysite/리드미 자료/검색.gif" width="80%">
</div>

- 검색어 입력 후 엔터키를 사용하여 특정 게시물을 검색할 수 있습니다.
- 검색어는 제목(Title), 글의 내용(Content), 카테고리(Category) 입니다.
- 미인증 사용자도 사용할 수 있습니다.
#### 404, 500 페이지
<div align="center">
  <img src="./mysite/리드미 자료/404, 500.gif" width="80%">
</div>

- 비정상적인 접근에 나타나는 페이지입니다. (삭제된 페이지 또는, 유효하지 않은 주소 등의 존재하지 않는 페이지)
# 7. 수정사항
- 개발 도중 main 앱을 사용하지 않고, blog의 메인 페이지와 병합하는 것으로 계획을 변경하였습니다. 하여, RedirectView를 사용해 기본 url을 '/blog/'로 할당하였습니다.

# 8. 프로젝트를 마치며
- Django를 사용한 첫 프로젝트를 진행하면서 막막했고 스스로 많이 부족하다 느꼈습니다. 그러나 처음 기획했던 것들을 하나씩 해결해 나가면서 성취감과 흥미를 얻어 프로젝트에 더 몰입할 수 있었습니다.
- 초반 단계의 기획과 WBS의 중요성을 실감할 수 있었습니다. 시간에 쫓기거나, 무엇을 해야 하는지 혼란스러워하던 상황들이 많이 줄었고 조금 더 짜임새 있는 프로젝트를 할 수 있었습니다.



