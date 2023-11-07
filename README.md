# Mobile game blog
- 다양한 모바일 게임의 개인적인 감상과 평가를 작성하며, 서로 정보를 공유하는 블로그

# 1. 프로젝트 소개
  
## 개발 기간
2023.10.26 ~ 2023.11.07

## 설명
- 글 작성, 삭제, 수정, 조회, 댓글 등 블로그 형식을 기반으로 제작된 커뮤니티 서비스
- 회원가입 한 사용자는 게시물과 댓글 작성 가능
- 게임 분류 별 카테고리와 검색 기능을 사용하여 정보를 보다 쉽게 얻을 수 있습니다.


# 2. 개발 기술 및 환경
## 2-1 개발 기술
#### [기술 - BE]
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">  
<br>
#### [기술 - FE]
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

## 2-2 개발 환경
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

# 3. DB



# 4. WBS




# 5. 아키텍처

## 파일트리
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
